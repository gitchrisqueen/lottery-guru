"""Human-readable prediction board.

Renders the most recent day's predictions as markdown tables (one per game and
draw time), writes PREDICTIONS.md, and splices the same content into README.md
between marker comments.
"""
from __future__ import annotations

import datetime as dt
import math
from collections import defaultdict
from pathlib import Path

from ..data import store
from ..games import GAMES
from . import scoring

START_MARKER = "<!-- PREDICTIONS:START -->"
END_MARKER = "<!-- PREDICTIONS:END -->"
SCOREBOARD_START = "<!-- SCOREBOARD:START -->"
SCOREBOARD_END = "<!-- SCOREBOARD:END -->"

DISCLAIMER = (
    "_These are experiment outputs, not advice. Every arm is expected to score "
    "at chance — see the [leaderboard](REPORT.md)._"
)


def format_numbers(game_key: str, numbers: list[int], special: int | None) -> str:
    game = GAMES[game_key]
    if game.kind == "jackpot":
        body = " ".join(f"`{n:02d}`" for n in numbers)
        return f"{body} + `{special:02d}`" if special is not None else body
    return " ".join(f"`{n}`" for n in numbers)


def latest_date() -> str | None:
    dates = store.all_dates("predictions")
    return dates[-1] if dates else None


def board_data(date: str | None = None) -> dict:
    """Structured predictions for one date — the data behind render_board().

    Returns {"date", "groups": [...]} where each group carries raw numbers
    (list[int] / int / None), never markdown-formatted strings.
    """
    date = date or latest_date()
    if date is None:
        return {"date": None, "groups": []}

    preds = store.load_json_list("predictions", date)
    evals = {
        (e["game"], e["draw_time"], e["strategy"]): e
        for e in store.load_json_list("evaluations", date)
    }

    # group by (game, draw_time) in game-config order
    groups: dict[tuple[str, str], list[dict]] = {}
    for p in preds:
        groups.setdefault((p["game"], p["draw_time"]), []).append(p)

    ordered = sorted(
        groups.items(),
        key=lambda kv: (list(GAMES).index(kv[0][0]), kv[0][1]),
    )

    out_groups = []
    for (game_key, draw_time), rows in ordered:
        game = GAMES[game_key]
        scored = any((game_key, draw_time, r["strategy"]) in evals for r in rows)
        out_rows = []
        for r in sorted(rows, key=lambda r: r["strategy"]):
            ev = evals.get((game_key, draw_time, r["strategy"]))
            row = {
                "strategy": r["strategy"],
                "predicted_numbers": r["numbers"],
                "predicted_special": r.get("special"),
                "actual_numbers": None,
                "actual_special": None,
                "matches": None,
                "special_hit": None,
                "straight": None,
            }
            if ev:
                s = ev["score"]
                row.update(
                    actual_numbers=ev["actual_numbers"],
                    actual_special=ev.get("actual_special"),
                    matches=s["matches"],
                    special_hit=s.get("special_hit", 0),
                    straight=s.get("straight", 0),
                )
            out_rows.append(row)
        out_groups.append(
            {
                "game": game_key,
                "display": game.display,
                "kind": game.kind,
                "draw_time": draw_time,
                "scored": scored,
                "rows": out_rows,
            }
        )
    return {"date": date, "groups": out_groups}


def render_board(date: str | None = None) -> str:
    data = board_data(date)
    date = data["date"]
    if date is None:
        return (
            f"### 🎟️ Latest predictions\n\n_No predictions recorded yet._\n"
        )

    lines = [
        f"### 🎟️ Predictions for {date}",
        "",
        DISCLAIMER,
        "",
    ]

    for group in data["groups"]:
        game_key = group["game"]
        draw_time = group["draw_time"]
        game = GAMES[game_key]
        heading = game.display if draw_time == "main" else f"{game.display} — {draw_time}"
        lines.append(f"**{heading}**")
        lines.append("")

        scored = group["scored"]
        if scored:
            lines.append("| Strategy | Predicted | Actual | Matches |")
            lines.append("|---|---|---|---|")
        else:
            lines.append("| Strategy | Predicted |")
            lines.append("|---|---|")

        for r in group["rows"]:
            predicted = format_numbers(
                game_key, r["predicted_numbers"], r["predicted_special"]
            )
            if scored and r["matches"] is not None:
                actual = format_numbers(
                    game_key, r["actual_numbers"], r["actual_special"]
                )
                marks = str(r["matches"])
                if game.special_max and r["special_hit"]:
                    marks += " +special"
                lines.append(f"| `{r['strategy']}` | {predicted} | {actual} | {marks} |")
            elif scored:
                lines.append(f"| `{r['strategy']}` | {predicted} | — | — |")
            else:
                lines.append(f"| `{r['strategy']}` | {predicted} |")
        lines.append("")

    if not data["groups"]:
        lines.append("_No drawings scheduled for this date._")
        lines.append("")

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines.append(f"<sub>Updated {stamp}</sub>")
    return "\n".join(lines) + "\n"


def strategy_totals() -> tuple[dict[str, dict], dict]:
    """Aggregate every scored prediction per strategy, pooling games correctly.

    Each (game, strategy) arm has its own null mean/variance, so observed,
    expected, and variance are summed across games before computing z.
    """
    per_strategy: dict[str, dict] = defaultdict(
        lambda: {"n": 0, "observed": 0, "expected": 0.0, "var": 0.0,
                 "best": 0, "best_game": "", "straights": 0, "special_hits": 0}
    )
    overall = {"n": 0, "observed": 0, "expected": 0.0, "var": 0.0, "days": 0}

    dates = store.all_dates("evaluations")
    overall["days"] = len(dates)
    for date in dates:
        for ev in store.load_json_list("evaluations", date):
            game = GAMES[ev["game"]]
            mean, var = scoring.null_moments(game)
            s = ev["score"]
            row = per_strategy[ev["strategy"]]
            row["n"] += 1
            row["observed"] += s["matches"]
            row["expected"] += mean
            row["var"] += var
            row["straights"] += s.get("straight", 0)
            row["special_hits"] += s.get("special_hit", 0)
            if s["matches"] > row["best"]:
                row["best"] = s["matches"]
                row["best_game"] = game.display
            overall["n"] += 1
            overall["observed"] += s["matches"]
            overall["expected"] += mean
            overall["var"] += var
    return per_strategy, overall


def z_score(observed: float, expected: float, var: float) -> float:
    sd = math.sqrt(var) if var > 0 else 0.0
    return (observed - expected) / sd if sd else 0.0


def render_scoreboard() -> str:
    per_strategy, overall = strategy_totals()
    if overall["n"] == 0:
        return (
            "### 📊 How it's performing\n\n"
            "_No predictions scored yet — stats appear once drawings come in._\n"
        )

    z_all = z_score(overall["observed"], overall["expected"], overall["var"])
    lines = [
        "### 📊 How it's performing",
        "",
        f"**{overall['n']}** predictions scored across **{overall['days']}** days. "
        f"Combined, they've hit **{overall['observed']}** numbers where pure chance "
        f"predicts **{overall['expected']:.1f}** "
        f"(z = **{z_all:+.2f}**).",
        "",
        "| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |",
        "|---|---|---|---|---|---|---|",
    ]
    ranked = sorted(
        per_strategy.items(),
        key=lambda kv: z_score(kv[1]["observed"], kv[1]["expected"], kv[1]["var"]),
        reverse=True,
    )
    for name, row in ranked:
        z = z_score(row["observed"], row["expected"], row["var"])
        rate = row["observed"] / row["n"] if row["n"] else 0.0
        best = f"{row['best']}" + (f" ({row['best_game']})" if row["best_game"] else "")
        lines.append(
            f"| `{name}` | {row['n']} | {row['observed']} | {row['expected']:.1f} | "
            f"{rate:.2f}/draw | {z:+.2f} | {best} |"
        )
    lines += [
        "",
        "_**Reading this:** `z` measures how far a strategy sits from pure chance in "
        "standard deviations. Values bouncing around 0 mean it is performing exactly as "
        "randomness predicts — which is the expected result. It would take a sustained "
        "|z| > 3 over many draws to suggest anything real, and no strategy is expected "
        "to get there._",
        "",
        f"<sub>Updated {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}</sub>",
    ]
    return "\n".join(lines) + "\n"


def write_board(path: str = "PREDICTIONS.md", date: str | None = None) -> str:
    body = render_board(date)
    Path(path).write_text(f"# Lottery Guru — Latest Predictions\n\n{body}")
    return body


def _splice(text: str, start: str, end: str, body: str) -> str:
    if start not in text or end not in text:
        return text
    head, rest = text.split(start, 1)
    _, tail = rest.split(end, 1)
    return f"{head}{start}\n{body}{end}{tail}"


def update_readme(body: str, scoreboard: str | None = None, path: str = "README.md") -> bool:
    """Splice board (and scoreboard) between marker comments. True if changed."""
    readme = Path(path)
    if not readme.exists():
        return False
    text = readme.read_text()
    updated = _splice(text, START_MARKER, END_MARKER, body)
    if scoreboard is not None:
        updated = _splice(updated, SCOREBOARD_START, SCOREBOARD_END, scoreboard)
    if updated == text:
        return False
    readme.write_text(updated)
    return True


def publish(date: str | None = None) -> None:
    body = write_board(date=date)
    update_readme(body, scoreboard=render_scoreboard())
