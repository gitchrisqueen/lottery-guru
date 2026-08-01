"""Hosted fine-tuning via Fireworks.ai LoRA. Runs anywhere (CI).

This is the hosted alternative to the local MLX path (train_mlx.py): upload
the exported chat JSONL as a dataset, run a supervised fine-tuning (LoRA)
job, and record the resulting model name in data/finetune/fireworks.json so
the `llm-tuned` arm can call it through the OpenAI-compatible inference
endpoint. Training cost: ~$0.50/M training tokens.

Serving: Fireworks does not serve LoRA fine-tunes serverlessly — inference
needs an on-demand (dedicated GPU) deployment billed while it exists. The
monthly workflow deploys ephemerally (train → deploy → predict → teardown),
and the record's "deployed" flag tells the daily loop whether the tuned arm
is currently callable.

Env:
    FIREWORKS_API_KEY      required (Bearer auth)
    FIREWORKS_ACCOUNT_ID   optional (the account slug in resource names;
                           auto-resolved from the API key when unset)
    LOTTERY_GURU_FT_BASE_MODEL   optional base-model override

The monthly workflow gates on ≥60 scored days (PLAN.md M4): below the gate,
train() skips cleanly so the cron stays green while history accumulates.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import time
from pathlib import Path

import requests

from ..data import store

API_BASE = "https://api.fireworks.ai/v1"
DEFAULT_BASE_MODEL = "accounts/fireworks/models/qwen3-8b"
DEFAULT_LORA_RANK = 8
# Tried in order until one is accepted AND has quota (Tier 2 grants B200-class
# quota; A100 quota is 0 on this account). LOTTERY_GURU_FT_ACCELERATOR overrides.
ACCELERATOR_CANDIDATES = (
    "NVIDIA_B200_180GB",
    "NVIDIA_H200_141GB",
    "NVIDIA_H100_80GB",
    "NVIDIA_A100_80GB",
)
DEFAULT_PRECISION = "BF16"
POLL_SECONDS = 30
JOB_TIMEOUT_SECONDS = 3 * 3600
DEPLOY_TIMEOUT_SECONDS = 1800


def api_key() -> str | None:
    return os.environ.get("FIREWORKS_API_KEY")


_resolved_account: str | None = None


def account_id() -> str | None:
    return os.environ.get("FIREWORKS_ACCOUNT_ID") or _resolved_account


def _ensure_account() -> str:
    """Return the account slug, resolving it from the API key if needed."""
    global _resolved_account
    acct = account_id()
    if acct:
        return acct
    try:
        resp = requests.get(f"{API_BASE}/accounts", headers=_headers(), timeout=60)
        accounts = _check(resp).json().get("accounts", [])
        _resolved_account = accounts[0]["name"].split("/")[-1]
    except Exception as exc:
        raise SystemExit(
            f"could not auto-resolve the Fireworks account id ({exc}); "
            "set the FIREWORKS_ACCOUNT_ID env var / repo secret"
        ) from exc
    print(f"resolved Fireworks account: {_resolved_account}")
    return _resolved_account


def available() -> bool:
    return bool(api_key())


def base_model() -> str:
    return os.environ.get("LOTTERY_GURU_FT_BASE_MODEL", DEFAULT_BASE_MODEL)


def record_path() -> Path:
    return store.DATA_DIR / "finetune" / "fireworks.json"


def load_record() -> dict | None:
    path = record_path()
    if not path.exists():
        return None
    return json.loads(path.read_text())


def save_record(record: dict) -> None:
    path = record_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=1) + "\n")


def scored_days() -> int:
    """Days with at least one scored prediction — the fine-tune gate metric."""
    return sum(1 for date in store.all_dates("evaluations")
               if store.load_json_list("evaluations", date))


def _headers() -> dict:
    return {"Authorization": f"Bearer {api_key()}"}


def _check(resp: requests.Response) -> requests.Response:
    """raise_for_status, but keep the response body — it carries the real reason."""
    if resp.status_code >= 400:
        raise RuntimeError(f"HTTP {resp.status_code} for {resp.url}: {resp.text[:1000]}")
    return resp


def _state(resource: dict) -> str:
    """Normalize 'JOB_STATE_COMPLETED' / 'COMPLETED' / 'READY' style enums."""
    state = resource.get("state", "")
    for prefix in ("JOB_STATE_", "STATE_"):
        if state.startswith(prefix):
            state = state[len(prefix):]
    return state


def _dataset_state(acct: str, dataset_id: str) -> str | None:
    resp = requests.get(
        f"{API_BASE}/accounts/{acct}/datasets/{dataset_id}",
        headers=_headers(), timeout=60,
    )
    if resp.status_code == 404:
        return None
    return _state(_check(resp).json())


def _upload_dataset(dataset_id: str, jsonl_path: Path) -> str:
    """Create a dataset, upload the JSONL, wait until READY. Returns its name.

    Rerun-safe: a dataset that already exists and is READY (e.g. from a failed
    prior run the same day) is reused as-is.
    """
    acct = account_id()
    name = f"accounts/{acct}/datasets/{dataset_id}"
    if _dataset_state(acct, dataset_id) == "READY":
        print(f"dataset {dataset_id} already READY — reusing")
        return name
    example_count = sum(1 for line in jsonl_path.read_text().splitlines() if line.strip())
    resp = requests.post(
        f"{API_BASE}/accounts/{acct}/datasets",
        headers=_headers(),
        json={
            "datasetId": dataset_id,
            "dataset": {"userUploaded": {}, "exampleCount": str(example_count)},
        },
        timeout=60,
    )
    if resp.status_code != 409:  # 409 = exists but not READY; try the upload again
        _check(resp)
    with jsonl_path.open("rb") as fh:
        _check(requests.post(
            f"{API_BASE}/accounts/{acct}/datasets/{dataset_id}:upload",
            headers=_headers(),
            files={"file": (jsonl_path.name, fh, "application/jsonl")},
            timeout=300,
        ))
    deadline = time.monotonic() + 600
    while time.monotonic() < deadline:
        state = _dataset_state(acct, dataset_id)
        if state == "READY":
            return name
        if state in ("FAILED", "UNSPECIFIED", None):
            raise RuntimeError(f"dataset {dataset_id} entered state {state}")
        time.sleep(POLL_SECONDS)
    raise TimeoutError(f"dataset {dataset_id} not READY after 600s")


def _start_job(dataset_name: str, eval_dataset_name: str | None,
               output_model_id: str, epochs: int | None) -> str:
    acct = account_id()
    body: dict = {
        "baseModel": base_model(),
        "dataset": dataset_name,
        "outputModel": f"accounts/{acct}/models/{output_model_id}",
        # explicit LoRA — omitting loraRank means full-parameter tuning,
        # which most base models reject ("model is not tunable")
        "loraRank": int(os.environ.get("LOTTERY_GURU_FT_LORA_RANK", DEFAULT_LORA_RANK)),
    }
    if eval_dataset_name:
        body["evaluationDataset"] = eval_dataset_name
    if epochs:
        body["epochs"] = epochs
    url = f"{API_BASE}/accounts/{acct}/supervisedFineTuningJobs"
    resp = requests.post(url, headers=_headers(), json=body, timeout=60)
    if resp.status_code == 400 and eval_dataset_name:
        # the optional evaluation dataset is the most likely rejected field —
        # retry without it rather than losing the run
        print(f"WARNING: job creation 400 ({resp.text[:300]}); retrying without evaluationDataset")
        body.pop("evaluationDataset")
        resp = requests.post(url, headers=_headers(), json=body, timeout=60)
    return _check(resp).json()["name"]


def _wait_for_job(job_name: str) -> dict:
    deadline = time.monotonic() + JOB_TIMEOUT_SECONDS
    while time.monotonic() < deadline:
        resp = requests.get(f"{API_BASE}/{job_name}", headers=_headers(), timeout=60)
        job = _check(resp).json()
        state = _state(job)
        if state == "COMPLETED":
            return job
        if state in ("FAILED", "CANCELLED", "DELETING"):
            raise RuntimeError(f"fine-tuning job {job_name} ended in state {state}: "
                               f"{job.get('status', job.get('error', ''))}")
        print(f"job {job_name}: {state or 'PENDING'} ...")
        time.sleep(POLL_SECONDS)
    raise TimeoutError(f"fine-tuning job {job_name} still running after {JOB_TIMEOUT_SECONDS}s")


def deploy(model_name: str) -> str:
    """Create an on-demand deployment for the tuned model and wait until READY.

    Fireworks no longer serves LoRA fine-tunes serverlessly — they need a
    dedicated (on-demand) deployment, billed by GPU time while it exists.
    Callers should tear it down when done (see teardown()).
    """
    override = os.environ.get("LOTTERY_GURU_FT_ACCELERATOR")
    candidates = (override,) if override else ACCELERATOR_CANDIDATES
    resp = None
    for accelerator in candidates:
        resp = requests.post(
            f"{API_BASE}/accounts/{account_id()}/deployments",
            headers=_headers(),
            json={
                "baseModel": model_name,
                "acceleratorType": accelerator,  # required for non-embeddings engines
                "precision": os.environ.get("LOTTERY_GURU_FT_PRECISION", DEFAULT_PRECISION),
            },
            timeout=60,
        )
        if resp.status_code < 400:
            break
        print(f"accelerator {accelerator} rejected ({resp.status_code}: {resp.text[:200]})")
    name = _check(resp).json()["name"]
    print(f"created deployment {name}, waiting for READY ...")
    deadline = time.monotonic() + DEPLOY_TIMEOUT_SECONDS
    while time.monotonic() < deadline:
        resp = requests.get(f"{API_BASE}/{name}", headers=_headers(), timeout=60)
        state = _state(_check(resp).json())
        if state == "READY":
            return name
        if state in ("FAILED", "DELETING"):
            raise RuntimeError(f"deployment {name} entered state {state}")
        print(f"deployment {name}: {state or 'PENDING'} ...")
        time.sleep(POLL_SECONDS)
    raise TimeoutError(f"deployment {name} not READY after {DEPLOY_TIMEOUT_SECONDS}s")


def teardown() -> bool:
    """Delete the deployment recorded in fireworks.json to stop GPU billing.

    Idempotent: no record, no deployment, or already-deleted all no-op.
    """
    record = load_record()
    if not record or not record.get("deployment"):
        print("no active deployment on record")
        return False
    name = record["deployment"]
    resp = requests.delete(
        f"{API_BASE}/{name}", headers=_headers(),
        # a recently-used deployment refuses deletion without this
        params={"ignoreChecks": "true", "ignore_checks": "true"},
        timeout=60,
    )
    if resp.status_code != 404:
        _check(resp)
    record["deployed"] = False
    record["last_deployment"] = record.pop("deployment")
    save_record(record)
    print(f"deleted deployment {name}")
    return True


def train(data_dir: str = "finetune_data", epochs: int | None = None,
          min_scored_days: int = 0, run_date: dt.date | None = None) -> str | None:
    """Full hosted fine-tune. Returns the tuned model name, or None if gated."""
    if not available():
        raise SystemExit("FIREWORKS_API_KEY must be set")
    _ensure_account()
    days = scored_days()
    if days < min_scored_days:
        print(f"skipping fine-tune: {days} scored days < gate of {min_scored_days}")
        return None

    run_date = run_date or dt.date.today()
    tag = run_date.isoformat()

    # Rerun-safe: if today's model already trained (e.g. a prior run failed
    # after training), skip straight to deployment instead of paying to retrain.
    existing = load_record()
    if existing and existing.get("model", "").endswith(tag):
        if existing.get("deployed"):
            print(f"model {existing['model']} already trained and deployed today")
        else:
            print(f"model {existing['model']} already trained today — deploying it")
            _deploy_and_record(existing)
        return existing["model"]

    train_path = Path(data_dir) / "train.jsonl"
    valid_path = Path(data_dir) / "valid.jsonl"
    if not train_path.exists():
        raise SystemExit(f"{train_path} not found — run `lottery-guru finetune export` first")

    print(f"uploading train dataset ({train_path}) ...")
    dataset_name = _upload_dataset(f"lottery-guru-train-{tag}", train_path)
    eval_dataset_name = None
    if valid_path.exists() and valid_path.stat().st_size > 0:
        print(f"uploading validation dataset ({valid_path}) ...")
        eval_dataset_name = _upload_dataset(f"lottery-guru-valid-{tag}", valid_path)

    output_model_id = f"lottery-guru-{tag}"
    job_name = _start_job(dataset_name, eval_dataset_name, output_model_id, epochs)
    print(f"started {job_name}, polling every {POLL_SECONDS}s ...")
    job = _wait_for_job(job_name)

    model_name = job.get("outputModel") or f"accounts/{account_id()}/models/{output_model_id}"
    record = {
        "model": model_name,
        "base_model": base_model(),
        "job": job_name,
        "dataset": dataset_name,
        "evaluation_dataset": eval_dataset_name,
        "deployed": False,
        "scored_days": days,
        "trained_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    }
    save_record(record)  # persist the training result before risking deployment
    _deploy_and_record(record)
    print(f"tuned model: {model_name} (record: {record_path()})")
    return model_name


def _deploy_and_record(record: dict) -> None:
    """Deploy the record's model and mark it servable; a failure only warns."""
    model_name = record["model"]
    try:
        deployment = deploy(model_name)
    except Exception as exc:
        print(f"WARNING: deployment failed ({exc}); the tuned model exists but is not servable "
              f"until deployed (lottery-guru finetune deploy)")
    else:
        record.update({
            "deployed": True,
            "deployment": deployment,
            "inference_model": f"{model_name}#{deployment}",
        })
        save_record(record)
