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
    socrata_dataset: str
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
}

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
