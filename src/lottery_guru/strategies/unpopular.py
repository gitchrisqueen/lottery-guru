"""Unpopular-numbers strategy — the one arm with defensible EV logic.

Match odds are identical to random by design; the payoff is a lower expected
number of co-winners (humans over-pick birthdays <=31, sequences, and grid
patterns — Israeli lottery study of ~800M manual picks). Its edge is invisible
to match-count scoring and only shows in modeled jackpot-share.
"""
from __future__ import annotations

import random

from ..data.sources import Draw
from ..games import Game


def _popularity_penalty(numbers: list[int]) -> float:
    penalty = 0.0
    for n in numbers:
        if n <= 12:
            penalty += 2.0  # day-and-month range, heavily over-picked
        elif n <= 31:
            penalty += 1.0  # birthday range
    diffs = {b - a for a, b in zip(numbers, numbers[1:])}
    if len(diffs) == 1:
        penalty += 5.0  # arithmetic progression (1-2-3-4-5, 5-10-15-20-25, ...)
    if any(n % 7 == 0 for n in numbers):
        penalty += 0.2 * sum(1 for n in numbers if n % 7 == 0)  # "lucky 7" multiples
    return penalty


def predict(game: Game, history: list[Draw], rng: random.Random):
    best = None
    best_penalty = float("inf")
    for _ in range(50):
        candidate = sorted(rng.sample(range(game.pick_min, game.pick_max + 1), game.pick_count))
        if sum(1 for n in candidate if n > 31) < 3:
            continue  # require most numbers above the birthday range
        p = _popularity_penalty(candidate)
        if p < best_penalty:
            best, best_penalty = candidate, p
    if best is None:
        best = sorted(rng.sample(range(32, game.pick_max + 1), game.pick_count))
    special = rng.randint(1, game.special_max) if game.special_max else None
    return best, special
