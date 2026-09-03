"""Render REPORT.md — the leaderboard of strategies vs the null hypothesis."""
from __future__ import annotations

import datetime as dt
from collections import defaultdict
from pathlib import Path

from ..data import store
from ..games import GAMES
from . import monitors, scoring

# Minimum scored draws before an arm's z/p are worth reading. Below this the
# normal approximation is loose and a handful of lucky draws swings z past 2;
# such arms are flagged, never dropped — the data stays on the board.
MIN_N = 50
INSUFFICIENT_MARKER = f"(n<{MIN_N}, not yet interpretable)"


def insufficient_sample(n: int) -> bool:
    return n < MIN_N


def leaderboard_data() -> dict[str, dict]:
    """Per-game leaderboards — the data behind build_report().

    Returns {game_key: {"display", "null_expectation", "rows": [...]}} with
    rows sorted by z descending; each row is scoring.aggregate() output plus
    the strategy name and an ``insufficient_sample`` flag (n < MIN_N).
    """
    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for date in store.all_dates("evaluations"):
        for ev in store.load_json_list("evaluations", date):
            grouped[(ev["game"], ev["strategy"])].append(ev["score"])

    out: dict[str, dict] = {}
    for game_key, game in GAMES.items():
        arms = {s: sc for (g, s), sc in grouped.items() if g == game_key}
        if not arms:
            continue
        mean, _ = scoring.null_moments(game)
        rows = []
        for strategy, scores in arms.items():
            agg = scoring.aggregate(game, scores)
            rows.append((agg.get("z", 0), strategy, agg))
        out[game_key] = {
            "display": game.display,
            "kind": game.kind,
            "null_expectation": round(mean, 4),
            "rows": [
                {"strategy": strategy, **agg,
                 "insufficient_sample": insufficient_sample(agg["n"])}
                for _, strategy, agg in sorted(rows, reverse=True)
            ],
        }
    return out


def build_report() -> str:
    games = leaderboard_data()

    lines = [
        "# Lottery Guru — Strategy Leaderboard",
        "",
        f"_Generated {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}. "
        "Null hypothesis: no strategy beats chance. A strategy is only interesting if "
        "|z| stays large as n grows — expect them all to converge to z ≈ 0. "
        f"Arms with fewer than {MIN_N} scored draws are marked `{INSUFFICIENT_MARKER}`: "
        "their z and p are printed for completeness but are too noisy to read as "
        "evidence either way._",
        "",
    ]
    for game_key, entry in games.items():
        lines.append(f"## {entry['display']}")
        lines.append("")
        lines.append(f"Null expectation: {entry['null_expectation']:.4f} matches per prediction.")
        lines.append("")
        lines.append("| Strategy | n | Observed | Expected | z | p | Straights |")
        lines.append("|---|---|---|---|---|---|---|")
        for agg in entry["rows"]:
            if agg["insufficient_sample"]:
                name = f"{agg['strategy']} _{INSUFFICIENT_MARKER}_"
                z, p = f"_{agg['z']}_", f"_{agg['p_value']}_"
            else:
                name, z, p = agg["strategy"], agg["z"], agg["p_value"]
            lines.append(
                f"| {name} | {agg['n']} | {agg['observed_matches']} | "
                f"{agg['expected_matches']} | {z} | {p} | {agg['straights']} |"
            )
        lines.append("")
    if len(lines) <= 4:
        lines.append("_No scored predictions yet — the daily loop hasn't produced results._")
        lines.append("")
    lines.extend(monitors.render_lines())
    return "\n".join(lines) + "\n"


def write_report(path: str = "REPORT.md") -> None:
    Path(path).write_text(build_report())
