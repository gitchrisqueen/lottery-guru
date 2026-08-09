"""Render REPORT.md — the leaderboard of strategies vs the null hypothesis."""
from __future__ import annotations

import datetime as dt
from collections import defaultdict
from pathlib import Path

from ..data import store
from ..games import GAMES
from . import monitors, scoring


def build_report() -> str:
    # gather all evaluations grouped by (game, strategy)
    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for date in store.all_dates("evaluations"):
        for ev in store.load_json_list("evaluations", date):
            grouped[(ev["game"], ev["strategy"])].append(ev["score"])

    lines = [
        "# Lottery Guru — Strategy Leaderboard",
        "",
        f"_Generated {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}. "
        "Null hypothesis: no strategy beats chance. A strategy is only interesting if "
        "|z| stays large as n grows — expect them all to converge to z ≈ 0._",
        "",
    ]
    for game_key, game in GAMES.items():
        arms = {s: sc for (g, s), sc in grouped.items() if g == game_key}
        if not arms:
            continue
        mean, _ = scoring.null_moments(game)
        lines.append(f"## {game.display}")
        lines.append("")
        lines.append(f"Null expectation: {mean:.4f} matches per prediction.")
        lines.append("")
        lines.append("| Strategy | n | Observed | Expected | z | p | Straights |")
        lines.append("|---|---|---|---|---|---|---|")
        rows = []
        for strategy, scores in arms.items():
            agg = scoring.aggregate(game, scores)
            rows.append((agg.get("z", 0), strategy, agg))
        for _, strategy, agg in sorted(rows, reverse=True):
            lines.append(
                f"| {strategy} | {agg['n']} | {agg['observed_matches']} | "
                f"{agg['expected_matches']} | {agg['z']} | {agg['p_value']} | {agg['straights']} |"
            )
        lines.append("")
    if len(lines) <= 4:
        lines.append("_No scored predictions yet — the daily loop hasn't produced results._")
        lines.append("")
    lines.extend(monitors.render_lines())
    return "\n".join(lines) + "\n"


def write_report(path: str = "REPORT.md") -> None:
    Path(path).write_text(build_report())
