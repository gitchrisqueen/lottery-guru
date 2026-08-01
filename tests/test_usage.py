"""Fireworks usage/cost logging."""
import datetime as dt
import json

import pytest

from lottery_guru.data import store
from lottery_guru.finetune import fireworks, usage


class _Resp:
    def __init__(self, payload=None, status_code=200):
        self._payload = payload or {}
        self.status_code = status_code
        self.url = "https://api.fireworks.ai/test"
        self.text = json.dumps(self._payload)

    def json(self):
        return self._payload


@pytest.fixture
def env(monkeypatch, tmp_path):
    monkeypatch.setattr(store, "DATA_DIR", tmp_path / "data")
    monkeypatch.setenv("FIREWORKS_API_KEY", "fw-key")
    monkeypatch.setenv("FIREWORKS_ACCOUNT_ID", "acct")
    monkeypatch.setattr(fireworks.time, "sleep", lambda s: None)  # no real retry backoff
    return tmp_path


def test_billing_usage_request_shape(env, monkeypatch):
    captured = {}

    def fake_get(url, **kwargs):
        captured["url"] = url
        captured["params"] = kwargs["params"]
        return _Resp({"usage": [{"acceleratorSeconds": "312"}]})

    monkeypatch.setattr(usage.requests, "get", fake_get)
    usage.log_billing_usage(days=2)

    assert captured["url"].endswith("/accounts/acct/billingUsage")
    keys = [k for k, _ in captured["params"]]
    assert keys.count("groupBy") == len(usage.GROUP_BY)
    window = dict(captured["params"][:2])
    assert window["startTime"].endswith("Z") and window["endTime"].endswith("Z")

    logged = usage.read_log()[-1]
    assert logged["event"] == "billing_usage"
    assert logged["usage"]["usage"][0]["acceleratorSeconds"] == "312"


def test_grouped_request_falls_back_to_ungrouped(env, monkeypatch):
    calls = []

    def fake_get(url, **kwargs):
        calls.append(kwargs["params"])
        if any(k == "groupBy" for k, _ in kwargs["params"]):
            return _Resp({"message": "unknown dimension"}, status_code=400)
        return _Resp({"usage": []})

    monkeypatch.setattr(usage.requests, "get", fake_get)
    usage.log_billing_usage()
    assert len(calls) == 2
    assert not any(k == "groupBy" for k, _ in calls[1])
    assert "error" not in usage.read_log()[-1]


def test_api_failure_is_logged_not_swallowed(env, monkeypatch):
    def boom(*a, **k):
        raise RuntimeError("connection reset")

    monkeypatch.setattr(usage.requests, "get", boom)
    usage.log_billing_usage()  # must not raise — the daily loop depends on it
    row = usage.read_log()[-1]
    assert "connection reset" in row["error"]


def test_missing_key_is_logged_without_calling_the_api(env, monkeypatch):
    monkeypatch.delenv("FIREWORKS_API_KEY")

    def boom(*a, **k):
        raise AssertionError("must not call the API without a key")

    monkeypatch.setattr(usage.requests, "get", boom)
    usage.log_billing_usage()
    assert "FIREWORKS_API_KEY" in usage.read_log()[-1]["error"]


def test_deployment_lifetime_recorded_on_teardown(env, monkeypatch):
    started = dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=6)
    fireworks.save_record({
        "model": "accounts/acct/models/lottery-guru-2026-08-01",
        "deployed": True,
        "deployment": "accounts/acct/deployments/dep1",
        "deployed_at": started.isoformat(),
        "accelerator": "NVIDIA_B200_180GB",
    })
    monkeypatch.setattr(fireworks.requests, "delete", lambda url, **k: _Resp())
    monkeypatch.setattr(fireworks.requests, "get", lambda url, **k: _Resp({"deployments": []}))

    fireworks.teardown()

    row = usage.read_log()[-1]
    assert row["event"] == "deployment_torn_down"
    assert row["accelerator"] == "NVIDIA_B200_180GB"
    assert 300 < row["billable_seconds"] < 420  # ~6 minutes
    assert usage.summary() == {
        "deployment_sessions": 1,
        "billable_seconds": row["billable_seconds"],
        "billable_hours": round(row["billable_seconds"] / 3600, 3),
        "logged_failures": 0,
    }


def test_failed_teardown_is_recorded_as_a_cost_risk(env, monkeypatch):
    fireworks.save_record({
        "model": "accounts/acct/models/m1",
        "deployed": True,
        "deployment": "accounts/acct/deployments/stuck",
        "deployed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    })
    monkeypatch.setattr(fireworks.requests, "delete",
                        lambda url, **k: _Resp({"message": "no"}, status_code=500))
    monkeypatch.setattr(fireworks.requests, "get", lambda url, **k: _Resp({"deployments": []}))

    fireworks.teardown()

    row = usage.read_log()[-1]
    assert row["event"] == "deployment_teardown_failed"
    assert usage.summary()["logged_failures"] == 1
