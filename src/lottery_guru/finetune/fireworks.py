"""Hosted fine-tuning via Fireworks.ai serverless LoRA. Runs anywhere (CI).

This is the hosted alternative to the local MLX path (train_mlx.py): upload
the exported chat JSONL as a dataset, run a supervised fine-tuning (LoRA)
job, and record the resulting model name in data/finetune/fireworks.json so
the daily loop's `llm-tuned` arm can call it through the OpenAI-compatible
inference endpoint. Cost: ~$0.50/M training tokens (<$1/run at this dataset
size).

Env:
    FIREWORKS_API_KEY      required (Bearer auth)
    FIREWORKS_ACCOUNT_ID   required (the account slug in resource names)
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
DEFAULT_BASE_MODEL = "accounts/fireworks/models/llama-v3p1-8b-instruct"
POLL_SECONDS = 30
JOB_TIMEOUT_SECONDS = 3 * 3600


def api_key() -> str | None:
    return os.environ.get("FIREWORKS_API_KEY")


def account_id() -> str | None:
    return os.environ.get("FIREWORKS_ACCOUNT_ID")


def available() -> bool:
    return bool(api_key() and account_id())


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


def _state(resource: dict) -> str:
    """Normalize 'JOB_STATE_COMPLETED' / 'COMPLETED' / 'READY' style enums."""
    state = resource.get("state", "")
    for prefix in ("JOB_STATE_", "STATE_"):
        if state.startswith(prefix):
            state = state[len(prefix):]
    return state


def _upload_dataset(dataset_id: str, jsonl_path: Path) -> str:
    """Create a dataset, upload the JSONL, wait until READY. Returns its name."""
    acct = account_id()
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
    # 409 = already exists (rerun of a failed job) — safe to re-upload
    if resp.status_code != 409:
        resp.raise_for_status()
    with jsonl_path.open("rb") as fh:
        resp = requests.post(
            f"{API_BASE}/accounts/{acct}/datasets/{dataset_id}:upload",
            headers=_headers(),
            files={"file": (jsonl_path.name, fh, "application/jsonl")},
            timeout=300,
        )
    resp.raise_for_status()
    deadline = time.monotonic() + 600
    while time.monotonic() < deadline:
        resp = requests.get(
            f"{API_BASE}/accounts/{acct}/datasets/{dataset_id}",
            headers=_headers(), timeout=60,
        )
        resp.raise_for_status()
        state = _state(resp.json())
        if state == "READY":
            return f"accounts/{acct}/datasets/{dataset_id}"
        if state in ("FAILED", "UNSPECIFIED"):
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
    }
    if eval_dataset_name:
        body["evaluationDataset"] = eval_dataset_name
    if epochs:
        body["epochs"] = epochs
    resp = requests.post(
        f"{API_BASE}/accounts/{acct}/supervisedFineTuningJobs",
        headers=_headers(), json=body, timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["name"]


def _wait_for_job(job_name: str) -> dict:
    deadline = time.monotonic() + JOB_TIMEOUT_SECONDS
    while time.monotonic() < deadline:
        resp = requests.get(f"{API_BASE}/{job_name}", headers=_headers(), timeout=60)
        resp.raise_for_status()
        job = resp.json()
        state = _state(job)
        if state == "COMPLETED":
            return job
        if state in ("FAILED", "CANCELLED", "DELETING"):
            raise RuntimeError(f"fine-tuning job {job_name} ended in state {state}: "
                               f"{job.get('status', job.get('error', ''))}")
        print(f"job {job_name}: {state or 'PENDING'} ...")
        time.sleep(POLL_SECONDS)
    raise TimeoutError(f"fine-tuning job {job_name} still running after {JOB_TIMEOUT_SECONDS}s")


def _deploy_serverless(model_name: str) -> bool:
    """Best-effort serverless LoRA deployment so inference can reach the model.

    Some base models are auto-servable; on others this call is required. A
    failure here should not lose the training run, so it only warns.
    """
    try:
        resp = requests.post(
            f"{API_BASE}/accounts/{account_id()}/deployedModels",
            headers=_headers(), json={"model": model_name}, timeout=60,
        )
        if resp.status_code == 409:  # already deployed
            return True
        resp.raise_for_status()
        return True
    except Exception as exc:
        print(f"WARNING: serverless deploy of {model_name} failed ({exc}); "
              f"deploy manually with: firectl deploy {model_name}")
        return False


def train(data_dir: str = "finetune_data", epochs: int | None = None,
          min_scored_days: int = 0, run_date: dt.date | None = None) -> str | None:
    """Full hosted fine-tune. Returns the tuned model name, or None if gated."""
    if not available():
        raise SystemExit("FIREWORKS_API_KEY and FIREWORKS_ACCOUNT_ID must be set")
    days = scored_days()
    if days < min_scored_days:
        print(f"skipping fine-tune: {days} scored days < gate of {min_scored_days}")
        return None

    run_date = run_date or dt.date.today()
    tag = run_date.isoformat()
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
    deployed = _deploy_serverless(model_name)
    save_record({
        "model": model_name,
        "base_model": base_model(),
        "job": job_name,
        "dataset": dataset_name,
        "evaluation_dataset": eval_dataset_name,
        "deployed": deployed,
        "scored_days": days,
        "trained_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    })
    print(f"tuned model: {model_name} (record: {record_path()})")
    return model_name
