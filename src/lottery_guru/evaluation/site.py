"""Static dashboard: JSON payloads + a checked-in HTML/CSS/JS shell.

Reuses board.py / report.py / monitors.py's data functions — never re-derives
statistics, so the site's numbers are provably identical to REPORT.md and
PREDICTIONS.md. The output directory (default dist/) is a build artifact like
a wheel, not committed; data/*.json under store.DATA_DIR stays the single
source of truth.

No build step: the shell in site_assets/ is copied byte-for-byte — no npm,
no bundler, no templating.
"""
from __future__ import annotations

import datetime as dt
import json
import shutil
from pathlib import Path

from ..games import GAMES
from . import board, monitors, report

TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "site_assets"

PAYLOAD_NAMES = ("scoreboard", "predictions", "leaderboard", "monitors", "meta")

MONITORS_NOTE = (
    "The only people who ever reliably made money on lotteries exploited "
    "payout structure — roll-down caps (Cash WinFall) or jackpots exceeding "
    "the cost of every combination (Mandel) — never prediction. These "
    "monitors check the tracked games for those defects; “no "
    "opportunity” is the expected, and real, result."
)


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def scoreboard_payload() -> dict:
    per_strategy, overall = board.strategy_totals()
    strategies = []
    ranked = sorted(
        per_strategy.items(),
        key=lambda kv: board.z_score(kv[1]["observed"], kv[1]["expected"], kv[1]["var"]),
        reverse=True,
    )
    # Rounded in Python to the exact precision the markdown scoreboard
    # displays (f"{...:.1f}" / f"{...:.2f}"), so the client never re-rounds —
    # Python's round() is banker's rounding while JS toLocaleString rounds
    # half-away-from-zero, and re-rounding would let the two surfaces diverge.
    for name, row in ranked:
        z = board.z_score(row["observed"], row["expected"], row["var"])
        strategies.append(
            {
                "strategy": name,
                "n": row["n"],
                "observed": row["observed"],
                "expected": float(f"{row['expected']:.1f}"),
                "hit_rate": float(f"{row['observed'] / row['n']:.2f}") if row["n"] else 0.0,
                "z": float(f"{z:.2f}"),
                "best": row["best"],
                "best_game": row["best_game"],
                "straights": row["straights"],
                "special_hits": row["special_hits"],
            }
        )
    overall_z = board.z_score(overall["observed"], overall["expected"], overall["var"])
    return {
        "generated_at": _now(),
        "overall": {
            "n": overall["n"],
            "observed": overall["observed"],
            "expected": float(f"{overall['expected']:.1f}"),
            "days": overall["days"],
            "z": float(f"{overall_z:.2f}"),
        },
        "strategies": strategies,
    }


def predictions_payload(date: str | None = None) -> dict:
    data = board.board_data(date)
    return {"generated_at": _now(), **data}


def leaderboard_payload() -> dict:
    return {"generated_at": _now(), "games": report.leaderboard_data()}


def monitors_payload() -> dict:
    return {"generated_at": _now(), "note": MONITORS_NOTE, "rows": monitors.rows()}


def meta_payload() -> dict:
    return {
        "generated_at": _now(),
        "games": [
            {"key": g.key, "display": g.display, "kind": g.kind}
            for g in GAMES.values()
        ],
    }


def write_json(out_dir: Path) -> dict[str, Path]:
    """Write every payload to out_dir/data/<name>.json; returns the paths."""
    payloads = {
        "scoreboard": scoreboard_payload(),
        "predictions": predictions_payload(),
        "leaderboard": leaderboard_payload(),
        "monitors": monitors_payload(),
        "meta": meta_payload(),
    }
    data_dir = out_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    paths = {}
    for name, payload in payloads.items():
        path = data_dir / f"{name}.json"
        path.write_text(json.dumps(payload, indent=1) + "\n")
        paths[name] = path
    return paths


def copy_shell(out_dir: Path) -> None:
    shutil.copytree(TEMPLATE_DIR, out_dir, dirs_exist_ok=True)


def build(out_dir: str | Path = "dist") -> Path:
    """Copy the static shell and write fresh JSON payloads beside it."""
    out = Path(out_dir)
    copy_shell(out)
    write_json(out)
    return out
