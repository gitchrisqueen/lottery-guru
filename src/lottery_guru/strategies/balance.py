"""Balanced / anti-balanced pair — the "winning tickets look average" claim.

Folk advice says real draws have mid-range sums and a 3:2 odd/even split.
That is true only because those bands contain more combinations; every single
combination is equiprobable, so filtering to the band buys nothing — while
herding you toward the crowd's favorite shapes (worse split risk).

`balanced` implements the folk filter; `antibalanced` inverts it (extreme
sums or single-parity tickets, which the crowd avoids). Expected result:
both at chance on match counts; any daylight between them would be a finding.
"""
from __future__ import annotations

import random

from ..data.sources import Draw
from ..games import Game

ATTEMPTS = 200


def _sum_bounds(game: Game) -> tuple[float, float]:
    lo = sum(range(game.pick_min, game.pick_min + game.pick_count))
    hi = sum(range(game.pick_max - game.pick_count + 1, game.pick_max + 1))
    return lo, hi


def _sample(game: Game, rng: random.Random) -> list[int]:
    return sorted(rng.sample(range(game.pick_min, game.pick_max + 1), game.pick_count))


def _pick_special(game: Game, rng: random.Random) -> int | None:
    return rng.randint(1, game.special_max) if game.special_max else None


def predict_balanced(game: Game, history: list[Draw], rng: random.Random):
    lo, hi = _sum_bounds(game)
    mid, band = (lo + hi) / 2, (hi - lo) * 0.15
    odd_ok = {game.pick_count // 2, (game.pick_count + 1) // 2}
    candidate = _sample(game, rng)
    for _ in range(ATTEMPTS):
        candidate = _sample(game, rng)
        odd = sum(1 for n in candidate if n % 2)
        if abs(sum(candidate) - mid) <= band and odd in odd_ok:
            break
    return candidate, _pick_special(game, rng)


def predict_antibalanced(game: Game, history: list[Draw], rng: random.Random):
    lo, hi = _sum_bounds(game)
    mid, band = (lo + hi) / 2, (hi - lo) * 0.20
    candidate = _sample(game, rng)
    for _ in range(ATTEMPTS):
        candidate = _sample(game, rng)
        odd = sum(1 for n in candidate if n % 2)
        if abs(sum(candidate) - mid) > band or odd in (0, game.pick_count):
            break
    return candidate, _pick_special(game, rng)
