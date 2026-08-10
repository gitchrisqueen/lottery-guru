"""Birthday-numbers strategy — deliberately popular picks.

The mirror of `unpopular`: sample from the date range 1-31, weighted toward
1-12 (day-and-month numbers), the way self-pickers demonstrably play. Match
odds are chance by design; the hypothesis under test is that this ticket
shape maximizes expected jackpot/prize SHARING (see the 110-way second-tier
split of 2005-03-30, docs/UNORTHODOX.md). Together with `unpopular` it
brackets the conscious-selection effect.
"""
from __future__ import annotations

import random

from ..data.sources import Draw
from ..games import Game

DATE_MAX = 31


def _weighted_sample(rng: random.Random, pool: list[int], weights: list[float], k: int) -> list[int]:
    chosen: list[int] = []
    pool, weights = list(pool), list(weights)
    for _ in range(k):
        total = sum(weights)
        r = rng.random() * total
        acc = 0.0
        for i, w in enumerate(weights):
            acc += w
            if r <= acc:
                chosen.append(pool.pop(i))
                weights.pop(i)
                break
    return chosen


def predict(game: Game, history: list[Draw], rng: random.Random):
    pool = list(range(game.pick_min, min(DATE_MAX, game.pick_max) + 1))
    weights = [3.0 if n <= 12 else 1.0 for n in pool]  # months+days over-weighted
    numbers = sorted(_weighted_sample(rng, pool, weights, game.pick_count))
    if game.special_max is None:
        special = None
    else:
        spool = list(range(1, game.special_max + 1))
        sweights = [3.0 if n <= 12 else 1.0 if n <= DATE_MAX else 0.25 for n in spool]
        special = _weighted_sample(rng, spool, sweights, 1)[0]
    return numbers, special
