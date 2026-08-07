"""Fireworks hosted fine-tuning — gate, record, and (mocked) API orchestration."""
import datetime as dt
import json

import pytest

from lottery_guru.data import store
from lottery_guru.finetune import fireworks


@pytest.fixture
def env(monkeypatch, tmp_path):
    monkeypatch.setattr(store, "DATA_DIR", tmp_path / "data")
    monkeypatch.setenv("FIREWORKS_API_KEY", "fw-key")
    monkeypatch.setenv("FIREWORKS_ACCOUNT_ID", "acct")
    monkeypatch.delenv("LOTTERY_GURU_FT_BASE_MODEL", raising=False)
    monkeypatch.delenv("LOTTERY_GURU_FT_LORA_RANK", raising=False)
    monkeypatch.delenv("LOTTERY_GURU_FT_ACCELERATOR", raising=False)
    monkeypatch.delenv("LOTTERY_GURU_FT_PRECISION", raising=False)
    monkeypatch.setattr(fireworks.time, "sleep", lambda s: None)
    return tmp_path


def _write_scored_days(n):
    for i in range(n):
        date = (dt.date(2026, 1, 1) + dt.timedelta(days=i)).isoformat()
        store.save_json_list("evaluations", date, [{"strategy": "random", "score": {}}])


def test_record_round_trip(env):
    assert fireworks.load_record() is None
    fireworks.save_record({"model": "accounts/acct/models/m1"})
    assert fireworks.load_record()["model"] == "accounts/acct/models/m1"


def test_scored_days_counts_only_nonempty(env):
    _write_scored_days(3)
    store.save_json_list("evaluations", "2026-02-01", [])  # empty day doesn't count
    assert fireworks.scored_days() == 3


def test_state_normalization():
    assert fireworks._state({"state": "JOB_STATE_COMPLETED"}) == "COMPLETED"
    assert fireworks._state({"state": "READY"}) == "READY"
    assert fireworks._state({}) == ""


def test_train_requires_api_key(env, monkeypatch):
    monkeypatch.delenv("FIREWORKS_API_KEY")
    with pytest.raises(SystemExit):
        fireworks.train()


def test_account_id_auto_resolved(env, monkeypatch):
    monkeypatch.delenv("FIREWORKS_ACCOUNT_ID")
    monkeypatch.setattr(fireworks, "_resolved_account", None)
    monkeypatch.setattr(fireworks.requests, "get", lambda url, **k: _Resp(
        {"accounts": [{"name": "accounts/my-slug"}]}))
    assert fireworks._ensure_account() == "my-slug"
    assert fireworks.account_id() == "my-slug"
    monkeypatch.setattr(fireworks, "_resolved_account", None)


def test_account_resolution_failure_is_clear(env, monkeypatch):
    monkeypatch.delenv("FIREWORKS_ACCOUNT_ID")
    monkeypatch.setattr(fireworks, "_resolved_account", None)

    def boom(*a, **k):
        raise RuntimeError("HTTP 401")

    monkeypatch.setattr(fireworks.requests, "get", boom)
    with pytest.raises(SystemExit, match="FIREWORKS_ACCOUNT_ID"):
        fireworks._ensure_account()


def test_gate_skips_without_network(env, monkeypatch):
    _write_scored_days(10)

    def boom(*a, **k):
        raise AssertionError("network call during gated skip")

    monkeypatch.setattr(fireworks.requests, "post", boom)
    monkeypatch.setattr(fireworks.requests, "get", boom)
    assert fireworks.train(min_scored_days=60) is None
    assert fireworks.load_record() is None


class _Resp:
    def __init__(self, payload=None, status_code=200):
        self._payload = payload or {}
        self.status_code = status_code
        self.url = "https://api.fireworks.ai/test"
        self.text = json.dumps(self._payload)

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self):
        return self._payload


def test_train_happy_path(env, monkeypatch):
    _write_scored_days(70)
    data_dir = env / "finetune_data"
    data_dir.mkdir()
    example = json.dumps({"messages": [{"role": "user", "content": "x"}]})
    (data_dir / "train.jsonl").write_text(example + "\n")
    (data_dir / "valid.jsonl").write_text(example + "\n")

    calls = []

    def fake_post(url, **kwargs):
        calls.append(("POST", url, kwargs.get("json")))
        if url.endswith("/supervisedFineTuningJobs"):
            return _Resp({"name": "accounts/acct/supervisedFineTuningJobs/j1"})
        if url.endswith("/deployments"):
            return _Resp({"name": "accounts/acct/deployments/dep1"})
        return _Resp()

    def fake_get(url, **kwargs):
        calls.append(("GET", url, None))
        if "supervisedFineTuningJobs" in url:
            return _Resp({"state": "JOB_STATE_COMPLETED",
                          "outputModel": "accounts/acct/models/lottery-guru-2026-08-01"})
        return _Resp({"state": "READY"})

    monkeypatch.setattr(fireworks.requests, "post", fake_post)
    monkeypatch.setattr(fireworks.requests, "get", fake_get)

    model = fireworks.train(data_dir=str(data_dir), min_scored_days=60,
                            run_date=dt.date(2026, 8, 1))
    assert model == "accounts/acct/models/lottery-guru-2026-08-01"

    job_bodies = [body for method, url, body in calls
                  if method == "POST" and url.endswith("/supervisedFineTuningJobs")]
    assert job_bodies == [{
        "baseModel": fireworks.DEFAULT_BASE_MODEL,
        "dataset": "accounts/acct/datasets/lottery-guru-train-2026-08-01",
        "evaluationDataset": "accounts/acct/datasets/lottery-guru-valid-2026-08-01",
        "outputModel": "accounts/acct/models/lottery-guru-2026-08-01",
        "loraRank": 8,
    }]
    deploys = [body for method, url, body in calls
               if method == "POST" and url.endswith("/deployments")]
    assert deploys == [{"baseModel": "accounts/acct/models/lottery-guru-2026-08-01",
                        "acceleratorType": fireworks.ACCELERATOR_CANDIDATES[0],
                        "precision": fireworks.DEFAULT_PRECISION}]

    record = fireworks.load_record()
    assert record["model"] == "accounts/acct/models/lottery-guru-2026-08-01"
    assert record["deployed"] is True
    assert record["deployment"] == "accounts/acct/deployments/dep1"
    assert record["inference_model"] == (
        "accounts/acct/models/lottery-guru-2026-08-01#accounts/acct/deployments/dep1")
    assert record["scored_days"] == 70


def test_train_reuses_same_day_model_without_retraining(env, monkeypatch):
    fireworks.save_record({
        "model": "accounts/acct/models/lottery-guru-2026-08-01",
        "deployed": False,
    })
    posts = []

    def fake_post(url, **kwargs):
        posts.append(url)
        assert "supervisedFineTuningJobs" not in url, "must not retrain same-day model"
        if url.endswith("/deployments"):
            return _Resp({"name": "accounts/acct/deployments/dep2"})
        return _Resp()

    monkeypatch.setattr(fireworks.requests, "post", fake_post)
    monkeypatch.setattr(fireworks.requests, "get",
                        lambda url, **k: _Resp({"state": "READY"}))
    model = fireworks.train(run_date=dt.date(2026, 8, 1))
    assert model == "accounts/acct/models/lottery-guru-2026-08-01"
    record = fireworks.load_record()
    assert record["deployed"] is True
    assert record["deployment"] == "accounts/acct/deployments/dep2"


def test_deploy_falls_through_accelerator_candidates(env, monkeypatch):
    attempts = []

    def fake_post(url, **kwargs):
        accel = kwargs["json"]["acceleratorType"]
        attempts.append(accel)
        if accel == fireworks.ACCELERATOR_CANDIDATES[2]:  # third candidate has quota
            return _Resp({"name": "accounts/acct/deployments/dep3"})
        return _Resp({"message": "no quota"}, status_code=429)

    monkeypatch.setattr(fireworks.requests, "post", fake_post)
    monkeypatch.setattr(fireworks.requests, "get",
                        lambda url, **k: _Resp({"state": "READY"}))
    assert fireworks.deploy("accounts/acct/models/m1") == "accounts/acct/deployments/dep3"
    assert attempts == list(fireworks.ACCELERATOR_CANDIDATES[:3])


def test_deploy_falls_through_when_accepted_deployment_then_fails(env, monkeypatch):
    """A GPU class that runs out of capacity accepts, then FAILs minutes later."""
    created, deleted = [], []

    def fake_post(url, **kwargs):
        accel = kwargs["json"]["acceleratorType"]
        created.append(accel)
        return _Resp({"name": f"accounts/acct/deployments/dep-{len(created)}"})

    def fake_get(url, **kwargs):
        if url.endswith("dep-1"):  # first candidate dies after being accepted
            return _Resp({"state": "FAILED", "status": {"message": "out of capacity"}})
        return _Resp({"state": "READY"})

    monkeypatch.setattr(fireworks.requests, "post", fake_post)
    monkeypatch.setattr(fireworks.requests, "get", fake_get)
    monkeypatch.setattr(fireworks.requests, "delete",
                        lambda url, **k: (deleted.append(url), _Resp())[1])

    assert fireworks.deploy("accounts/acct/models/m1") == "accounts/acct/deployments/dep-2"
    assert created == list(fireworks.ACCELERATOR_CANDIDATES[:2])
    # the dead deployment is deleted immediately, not left for the nightly sweep
    assert deleted == [f"{fireworks.API_BASE}/accounts/acct/deployments/dep-1"]


def test_deploy_failure_is_logged_with_its_reason(env, monkeypatch):
    from lottery_guru.finetune import usage

    monkeypatch.setattr(fireworks.requests, "post", lambda url, **k: _Resp(
        {"name": "accounts/acct/deployments/dead"}))
    monkeypatch.setattr(fireworks.requests, "get", lambda url, **k: _Resp(
        {"state": "FAILED", "status": {"message": "no B200 capacity in GLOBAL"}}))
    monkeypatch.setattr(fireworks.requests, "delete", lambda url, **k: _Resp())
    monkeypatch.setenv("LOTTERY_GURU_FT_ACCELERATOR", "NVIDIA_B200_180GB")

    with pytest.raises(RuntimeError, match="could not bring up a deployment"):
        fireworks.deploy("accounts/acct/models/m1")

    rows = usage.read_log()
    assert [row["event"] for row in rows] == ["deployment_failed"]
    assert rows[0]["accelerator"] == "NVIDIA_B200_180GB"
    assert "no B200 capacity in GLOBAL" in rows[0]["error"]
    assert usage.summary()["logged_failures"] == 1


def test_deploy_reports_every_candidate_it_tried(env, monkeypatch):
    monkeypatch.setattr(fireworks.requests, "post",
                        lambda url, **k: _Resp({"message": "no quota"}, status_code=429))
    with pytest.raises(RuntimeError) as excinfo:
        fireworks.deploy("accounts/acct/models/m1")
    for accelerator in fireworks.ACCELERATOR_CANDIDATES:
        assert accelerator in str(excinfo.value)


def test_status_message_survives_the_shapes_fireworks_uses():
    assert fireworks._status_message({"statusMessage": "boom"}) == "boom"
    assert fireworks._status_message({"status": {"message": "boom"}}) == "boom"
    assert fireworks._status_message({"status": "boom"}) == "boom"
    assert fireworks._status_message({"state": "FAILED"}) == ""
    assert fireworks._status_message(None) == ""


def test_deploy_reuses_live_deployment_instead_of_double_billing(env, monkeypatch):
    fireworks.save_record({
        "model": "accounts/acct/models/m1",
        "deployed": True,
        "deployment": "accounts/acct/deployments/live1",
    })

    def boom_post(*a, **k):
        raise AssertionError("must not create a second deployment")

    monkeypatch.setattr(fireworks.requests, "post", boom_post)
    monkeypatch.setattr(fireworks.requests, "get",
                        lambda url, **k: _Resp({"state": "READY"}))
    assert fireworks.deploy("accounts/acct/models/m1") == "accounts/acct/deployments/live1"


def test_teardown_sweeps_orphaned_lottery_guru_deployments(env, monkeypatch):
    # no record at all — the only trace of the leak is on Fireworks' side
    deleted = []
    monkeypatch.setattr(fireworks.requests, "get", lambda url, **k: _Resp({"deployments": [
        {"name": "accounts/acct/deployments/orphan",
         "baseModel": "accounts/acct/models/lottery-guru-2026-08-01"},
        {"name": "accounts/acct/deployments/someone-elses",
         "baseModel": "accounts/acct/models/unrelated-project"},
    ]}))
    monkeypatch.setattr(fireworks.requests, "delete",
                        lambda url, **k: (deleted.append(url), _Resp())[1])
    fireworks.teardown()
    assert deleted == [f"{fireworks.API_BASE}/accounts/acct/deployments/orphan"]


def test_teardown_warns_but_does_not_raise_when_delete_fails(env, monkeypatch, capsys):
    fireworks.save_record({
        "model": "accounts/acct/models/m1",
        "deployed": True,
        "deployment": "accounts/acct/deployments/stuck",
    })
    monkeypatch.setattr(fireworks.requests, "delete",
                        lambda url, **k: _Resp({"message": "nope"}, status_code=500))
    monkeypatch.setattr(fireworks.requests, "get",
                        lambda url, **k: _Resp({"deployments": []}))
    assert fireworks.teardown() is False
    out = capsys.readouterr().out
    assert "may still be running and billing" in out
    # record still says deployed so the leak stays visible rather than silently cleared
    assert fireworks.load_record()["deployment"] == "accounts/acct/deployments/stuck"


def test_teardown_deletes_deployment_and_flips_record(env, monkeypatch):
    fireworks.save_record({
        "model": "accounts/acct/models/m1",
        "deployed": True,
        "deployment": "accounts/acct/deployments/dep1",
        "inference_model": "accounts/acct/models/m1#accounts/acct/deployments/dep1",
    })
    deleted = []

    def fake_delete(url, **kwargs):
        deleted.append((url, kwargs.get("params", {})))
        return _Resp()

    monkeypatch.setattr(fireworks.requests, "delete", fake_delete)
    monkeypatch.setattr(fireworks.requests, "get",
                        lambda url, **k: _Resp({"deployments": []}))
    assert fireworks.teardown() is True
    url, params = deleted[0]
    assert url == f"{fireworks.API_BASE}/accounts/acct/deployments/dep1"
    assert params.get("ignoreChecks") == "true"  # recently-used deployments refuse deletion otherwise
    record = fireworks.load_record()
    assert record["deployed"] is False
    assert "deployment" not in record
    assert record["last_deployment"] == "accounts/acct/deployments/dep1"
    # idempotent second call
    assert fireworks.teardown() is False


def test_job_create_retries_without_eval_dataset(env, monkeypatch):
    bodies = []

    def fake_post(url, **kwargs):
        body = kwargs.get("json")
        if url.endswith("/supervisedFineTuningJobs"):
            bodies.append(dict(body))
            if "evaluationDataset" in body:
                return _Resp({"error": "unknown field evaluationDataset"}, status_code=400)
            return _Resp({"name": "accounts/acct/supervisedFineTuningJobs/j1"})
        return _Resp()

    monkeypatch.setattr(fireworks.requests, "post", fake_post)
    name = fireworks._start_job("accounts/acct/datasets/d1",
                                "accounts/acct/datasets/d2", "out-model", None)
    assert name == "accounts/acct/supervisedFineTuningJobs/j1"
    assert "evaluationDataset" in bodies[0] and "evaluationDataset" not in bodies[1]


def test_train_failed_job_raises(env, monkeypatch):
    _write_scored_days(70)
    data_dir = env / "finetune_data"
    data_dir.mkdir()
    (data_dir / "train.jsonl").write_text('{"messages": []}\n')

    def fake_post(url, **kwargs):
        if url.endswith("/supervisedFineTuningJobs"):
            return _Resp({"name": "accounts/acct/supervisedFineTuningJobs/j1"})
        return _Resp()

    def fake_get(url, **kwargs):
        if "supervisedFineTuningJobs" in url:
            return _Resp({"state": "JOB_STATE_FAILED", "status": "boom"})
        return _Resp({"state": "READY"})

    monkeypatch.setattr(fireworks.requests, "post", fake_post)
    monkeypatch.setattr(fireworks.requests, "get", fake_get)
    with pytest.raises(RuntimeError, match="FAILED"):
        fireworks.train(data_dir=str(data_dir))
    assert fireworks.load_record() is None
