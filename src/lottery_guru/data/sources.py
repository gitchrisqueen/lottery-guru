"""Fetch and normalize drawing results.

Primary source: NY Open Data (Socrata, data.ny.gov) — free, no auth, nightly
batch ~07:30-09:00 UTC. Optional SOCRATA_APP_TOKEN env var lifts throttling.
Secondary: Texas Lottery CSVs, used as an integrity cross-check for Powerball.
"""
from __future__ import annotations

import csv
import io
import os
from dataclasses import dataclass, asdict

import requests

from ..games import Game

SOCRATA_BASE = "https://data.ny.gov/resource"
TX_POWERBALL_CSV = (
    "https://www.texaslottery.com/export/sites/lottery/Games/"
    "Powerball/Winning_Numbers/powerball.csv"
)
TIMEOUT = 30


@dataclass(frozen=True)
class Draw:
    date: str  # YYYY-MM-DD
    draw_time: str  # "main" | "midday" | "evening"
    numbers: tuple[int, ...]
    special: int | None

    def to_dict(self) -> dict:
        d = asdict(self)
        d["numbers"] = list(self.numbers)
        return d

    @staticmethod
    def from_dict(d: dict) -> "Draw":
        return Draw(
            date=d["date"],
            draw_time=d["draw_time"],
            numbers=tuple(d["numbers"]),
            special=d.get("special"),
        )


def _socrata_get(dataset: str, limit: int) -> list[dict]:
    params = {"$order": "draw_date DESC", "$limit": str(limit)}
    token = os.environ.get("SOCRATA_APP_TOKEN")
    headers = {"X-App-Token": token} if token else {}
    resp = requests.get(
        f"{SOCRATA_BASE}/{dataset}.json", params=params, headers=headers, timeout=TIMEOUT
    )
    resp.raise_for_status()
    return resp.json()


def fetch_draws(game: Game, limit: int = 200) -> list[Draw]:
    rows = _socrata_get(game.socrata_dataset, limit)
    parser = _PARSERS[game.key]
    draws: list[Draw] = []
    for row in rows:
        draws.extend(parser(row))
    return draws


def _date_of(row: dict) -> str:
    return row["draw_date"][:10]


def _parse_powerball(row: dict) -> list[Draw]:
    parts = [int(x) for x in row["winning_numbers"].split()]
    # 6 space-separated numbers; the 6th is the Powerball
    if len(parts) != 6:
        return []
    return [Draw(_date_of(row), "main", tuple(sorted(parts[:5])), parts[5])]


def _parse_megamillions(row: dict) -> list[Draw]:
    whites = [int(x) for x in row["winning_numbers"].split()]
    if len(whites) != 5 or "mega_ball" not in row:
        return []
    return [Draw(_date_of(row), "main", tuple(sorted(whites)), int(row["mega_ball"]))]


def _parse_digits(row: dict, midday_key: str, evening_key: str, n_digits: int) -> list[Draw]:
    out = []
    for key, draw_time in ((midday_key, "midday"), (evening_key, "evening")):
        val = row.get(key)
        if val and len(val) == n_digits and val.isdigit():
            out.append(Draw(_date_of(row), draw_time, tuple(int(c) for c in val), None))
    return out


def _parse_ny_numbers(row: dict) -> list[Draw]:
    return _parse_digits(row, "midday_daily", "evening_daily", 3)


def _parse_ny_win4(row: dict) -> list[Draw]:
    return _parse_digits(row, "midday_win_4", "evening_win_4", 4)


_PARSERS = {
    "powerball": _parse_powerball,
    "megamillions": _parse_megamillions,
    "ny_numbers": _parse_ny_numbers,
    "ny_win4": _parse_ny_win4,
}


def cross_check_powerball(draws_by_date: dict[str, Draw]) -> list[str]:
    """Diff recent NY-sourced Powerball draws against the Texas Lottery CSV.

    Returns a list of human-readable mismatch warnings (empty = all good).
    """
    try:
        resp = requests.get(TX_POWERBALL_CSV, timeout=TIMEOUT)
        resp.raise_for_status()
    except requests.RequestException as exc:
        return [f"TX cross-check unavailable: {exc}"]

    warnings: list[str] = []
    checked = 0
    # Row format: Powerball,M,D,Y,w1,w2,w3,w4,w5 (unordered),PB,multiplier
    for row in csv.reader(io.StringIO(resp.text)):
        if len(row) < 10 or row[0] != "Powerball":
            continue
        try:
            date = f"{int(row[3]):04d}-{int(row[1]):02d}-{int(row[2]):02d}"
            whites = tuple(sorted(int(x) for x in row[4:9]))
            pb = int(row[9])
        except ValueError:
            continue
        ours = draws_by_date.get(date)
        if ours is None:
            continue
        checked += 1
        if ours.numbers != whites or ours.special != pb:
            warnings.append(
                f"Powerball {date}: NY={list(ours.numbers)}+{ours.special} "
                f"TX={list(whites)}+{pb}"
            )
        if checked >= 20:
            break
    return warnings
