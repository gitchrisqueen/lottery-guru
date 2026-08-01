"""Track what this project actually costs on Fireworks, committed to the repo.

Two independent sources, because neither alone is sufficient:

1. **Fireworks `billingUsage`** (GET /v1/accounts/{id}/billingUsage) — metered
   quantities: accelerator-seconds, tokens. Authoritative, but it reports
   *quantities, not dollars*: rated dollar totals live behind GetBillingSummary,
   which is CLI-only today. It can also lag behind live usage.
2. **Our own deployment lifetimes** — measured locally when teardown deletes a
   deployment. Immediate, and it is the dominant cost driver (a dedicated GPU
   bills for as long as it exists), so it catches a leak the same day rather
   than whenever billing catches up.

Append-only JSONL at data/usage/fireworks.jsonl — one line per event, so daily
commits never conflict. Failures are logged too: a silent gap in a cost log is
worse than a visible error.
"""
from __future__ import annotations

import datetime as dt
import json

import requests

from ..data import store
from . import fireworks

API_BASE = fireworks.API_BASE
GROUP_BY = ("deployment_name", "accelerator_type")


def log_path():
    return store.DATA_DIR / "usage" / "fireworks.jsonl"


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def append(record: dict) -> dict:
    """Append one event to the usage log."""
    path = log_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")
    return record


def read_log() -> list[dict]:
    path = log_path()
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def fetch_billing_usage(start: dt.datetime, end: dt.datetime) -> dict:
    """GET billingUsage for a window, grouped by deployment and accelerator."""
    acct = fireworks._ensure_account()
    url = f"{API_BASE}/accounts/{acct}/billingUsage"
    params = [("startTime", start.isoformat().replace("+00:00", "Z")),
              ("endTime", end.isoformat().replace("+00:00", "Z"))]
    grouped = params + [("groupBy", g) for g in GROUP_BY]
    resp = requests.get(url, headers=fireworks._headers(), params=grouped, timeout=60)
    if resp.status_code == 400:
        # unknown groupBy dimension — the ungrouped totals are still worth having
        print(f"WARNING: grouped billingUsage rejected ({resp.text[:200]}); retrying ungrouped")
        resp = requests.get(url, headers=fireworks._headers(), params=params, timeout=60)
    return fireworks._check(resp).json()


def log_billing_usage(days: int = 1) -> dict:
    """Record metered usage for the last `days` days. Never raises."""
    end = dt.datetime.now(dt.timezone.utc)
    start = end - dt.timedelta(days=days)
    base = {"logged_at": _now(), "event": "billing_usage", "source": "billingUsage",
            "window_start": start.isoformat(), "window_end": end.isoformat()}
    if not fireworks.available():
        return append({**base, "error": "FIREWORKS_API_KEY not set"})
    try:
        return append({**base, "usage": fetch_billing_usage(start, end)})
    except Exception as exc:
        print(f"WARNING: could not fetch billingUsage: {exc}")
        return append({**base, "error": str(exc)[:500]})


def log_deployment_lifetime(record: dict, deleted: bool) -> dict | None:
    """Record how long a deployment existed — the GPU-time we were billed for.

    `record` is the fireworks.json entry as it stood before teardown cleared it.
    """
    name = record.get("deployment") or record.get("last_deployment")
    if not name:
        return None
    started = record.get("deployed_at")
    seconds = None
    if started:
        try:
            seconds = round(
                (dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(started))
                .total_seconds(), 1)
        except ValueError:
            pass
    return append({
        "logged_at": _now(),
        "event": "deployment_torn_down" if deleted else "deployment_teardown_failed",
        "deployment": name,
        "model": record.get("model"),
        "accelerator": record.get("accelerator"),
        "deployed_at": started,
        "billable_seconds": seconds,
    })


def summary() -> dict:
    """Totals across the committed log — GPU-seconds we know we paid for."""
    seconds, sessions, failures = 0.0, 0, 0
    for row in read_log():
        if row.get("event") == "deployment_torn_down":
            sessions += 1
            seconds += row.get("billable_seconds") or 0
        elif row.get("event") == "deployment_teardown_failed" or row.get("error"):
            failures += 1
    return {"deployment_sessions": sessions,
            "billable_seconds": round(seconds, 1),
            "billable_hours": round(seconds / 3600, 3),
            "logged_failures": failures}
