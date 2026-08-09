"""Moon-phase strategy — astrology-flavored picks, honestly labeled.

Believers hold that lunar phase governs luck (play on a full moon, let the
phase choose your numbers). Mechanically this arm is a seeded RNG wearing a
costume: the lunar phase angle — computed offline from the synodic month, no
ephemeris or network — is folded into the seed, and the picks are uniform.
That IS the point: it demonstrates that a mystical selection rule is
indistinguishable from `random`, which is exactly what the scoreboard should
show.

The phase is computed for the day after the newest draw in history (the
drawing being predicted, to within data lag), keeping the arm a pure
function of its inputs.
"""
from __future__ import annotations

import datetime as dt
import random

from ..data.sources import Draw
from ..games import Game

SYNODIC_MONTH = 29.530588853  # days
KNOWN_NEW_MOON = dt.date(2000, 1, 6)  # 18:14 UTC, close enough for a costume


def phase_angle(date: dt.date) -> float:
    """Lunar phase angle in degrees: 0 = new, 180 = full."""
    days = (date - KNOWN_NEW_MOON).days
    return (days % SYNODIC_MONTH) / SYNODIC_MONTH * 360.0


def predict(game: Game, history: list[Draw], rng: random.Random):
    if history:
        target = dt.date.fromisoformat(history[-1].date) + dt.timedelta(days=1)
    else:
        target = KNOWN_NEW_MOON
    angle = phase_angle(target)
    lunar = random.Random(rng.getrandbits(64) ^ int(angle * 1000))
    if game.kind == "jackpot":
        numbers = sorted(lunar.sample(range(game.pick_min, game.pick_max + 1), game.pick_count))
    else:
        numbers = [lunar.randint(0, 9) for _ in range(game.pick_count)]
    special = lunar.randint(1, game.special_max) if game.special_max else None
    return numbers, special
