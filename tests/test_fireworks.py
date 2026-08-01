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
    }]
    deploys = [body for method, url, body in calls if url.endswith("/deployedModels")]
    assert deploys == [{"model": "accounts/acct/models/lottery-guru-2026-08-01"}]

    record = fireworks.load_record()
    assert record["model"] == "accounts/acct/models/lottery-guru-2026-08-01"
    assert record["deployed"] is True
    assert record["scored_days"] == 70


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
