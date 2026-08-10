"""Game definitions and draw-schedule logic."""
from __future__ import annotations

import datetime as dt
from dataclasses import dataclass


@dataclass(frozen=True)
class Game:
    key: str
    display: str
    kind: str  # "jackpot" (unordered picks + special ball) or "digit" (ordered digits)
    pick_count: int  # white balls picked, or number of digit positions
    pick_max: int  # highest white ball (1..pick_max), or 9 for digits (0..9)
    pick_min: int  # 1 for jackpot games, 0 for digit games
    special_max: int | None  # special-ball range (1..special_max), None for digit games
    draw_weekdays: tuple[int, ...]  # 0=Mon .. 6=Sun
    draw_times: tuple[str, ...]  # "main" or ("midday", "evening")
    socrata_dataset: str | None = None  # NY Open Data source (data.ny.gov)
    fl_pdf_stem: str | None = None  # Florida Lottery source (files.floridalottery.com/exptkt/)
    era_start: str | None = None  # first date (ISO) of the current rule era; None = no rule changes


GAMES: dict[str, Game] = {
    "powerball": Game(
        key="powerball",
        display="Powerball",
        kind="jackpot",
        pick_count=5,
        pick_max=69,
        pick_min=1,
        special_max=26,
        draw_weekdays=(0, 2, 5),  # Mon/Wed/Sat
        draw_times=("main",),
        socrata_dataset="d6yy-54nr",
        era_start="2015-10-07",  # 5/69 + 1/26 era
    ),
    "megamillions": Game(
        key="megamillions",
        display="Mega Millions",
        kind="jackpot",
        pick_count=5,
        pick_max=70,  # 5/70 + 1/24 era (since Apr 2025) — never pool stats across eras
        pick_min=1,
        special_max=24,
        draw_weekdays=(1, 4),  # Tue/Fri
        draw_times=("main",),
        socrata_dataset="5xaw-6ayf",
        era_start="2025-04-08",  # 5/70 + 1/24 era
    ),
    "ny_numbers": Game(
        key="ny_numbers",
        display="NY Numbers (Pick 3)",
        kind="digit",
        pick_count=3,
        pick_max=9,
        pick_min=0,
        special_max=None,
        draw_weekdays=(0, 1, 2, 3, 4, 5, 6),
        draw_times=("midday", "evening"),
        socrata_dataset="hsys-3def",
    ),
    "ny_win4": Game(
        key="ny_win4",
        display="NY Win 4",
        kind="digit",
        pick_count=4,
        pick_max=9,
        pick_min=0,
        special_max=None,
        draw_weekdays=(0, 1, 2, 3, 4, 5, 6),
        draw_times=("midday", "evening"),
        socrata_dataset="hsys-3def",
    ),
    # Florida games come from the official PDF history files (no Socrata portal
    # exists for FL). Jackpot-style FL games have no special ball: special_max
    # is None and every arm must handle that.
    "fl_fantasy5": Game(
        key="fl_fantasy5",
        display="FL Fantasy 5",
        kind="jackpot",
        pick_count=5,
        pick_max=36,
        pick_min=1,
        special_max=None,
        draw_weekdays=(0, 1, 2, 3, 4, 5, 6),
        draw_times=("midday", "evening"),
        fl_pdf_stem="ff",
        era_start="2023-03-20",  # midday drawing added; evening-only before
    ),
    "fl_lotto": Game(
        key="fl_lotto",
        display="Florida Lotto",
        kind="jackpot",
        pick_count=6,
        pick_max=53,
        pick_min=1,
        special_max=None,
        draw_weekdays=(2, 5),  # Wed/Sat
        draw_times=("main",),
        fl_pdf_stem="l6",
        era_start="1999-10-24",  # 6/53 era (6/49 before)
    ),
    "fl_jtp": Game(
        key="fl_jtp",
        display="FL Jackpot Triple Play",
        kind="jackpot",
        pick_count=6,
        pick_max=46,
        pick_min=1,
        special_max=None,
        draw_weekdays=(1, 4),  # Tue/Fri
        draw_times=("main",),
        fl_pdf_stem="jtp",
        era_start="2019-02-01",
    ),
    "fl_pick2": Game(
        key="fl_pick2",
        display="FL Pick 2",
        kind="digit",
        pick_count=2,
        pick_max=9,
        pick_min=0,
        special_max=None,
        draw_weekdays=(0, 1, 2, 3, 4, 5, 6),
        draw_times=("midday", "evening"),
        fl_pdf_stem="p2",
    ),
    "fl_pick3": Game(
        key="fl_pick3",
        display="FL Pick 3",
        kind="digit",
        pick_count=3,
        pick_max=9,
        pick_min=0,
        special_max=None,
        draw_weekdays=(0, 1, 2, 3, 4, 5, 6),
        draw_times=("midday", "evening"),
        fl_pdf_stem="p3",
    ),
    "fl_pick4": Game(
        key="fl_pick4",
        display="FL Pick 4",
        kind="digit",
        pick_count=4,
        pick_max=9,
        pick_min=0,
        special_max=None,
        draw_weekdays=(0, 1, 2, 3, 4, 5, 6),
        draw_times=("midday", "evening"),
        fl_pdf_stem="p4",
    ),
    "fl_pick5": Game(
        key="fl_pick5",
        display="FL Pick 5",
        kind="digit",
        pick_count=5,
        pick_max=9,
        pick_min=0,
        special_max=None,
        draw_weekdays=(0, 1, 2, 3, 4, 5, 6),
        draw_times=("midday", "evening"),
        fl_pdf_stem="p5",
    ),
}

# The GPU-backed llm-tuned arm deploys only on days one of these games draws.
# Deliberately NOT "every jackpot-kind game": FL Fantasy 5 draws daily, and
# gating on kind would silently grow GPU spend from 5 to 7 days a week.
TUNED_ARM_GAMES = ("powerball", "megamillions")

# Mega Millions changed to 5/70 + 1/24 in April 2025. Stats must not pool across eras.
MEGAMILLIONS_ERA_START = dt.date(2025, 4, 8)


def draws_on(date: dt.date) -> list[tuple[Game, str]]:
    """Return (game, draw_time) pairs that have a drawing on `date`."""
    out: list[tuple[Game, str]] = []
    for game in GAMES.values():
        if date.weekday() in game.draw_weekdays:
            for t in game.draw_times:
                out.append((game, t))
    return out
