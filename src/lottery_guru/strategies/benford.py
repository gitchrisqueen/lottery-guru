"""Benford's-law strategy — a deliberately wrong control arm.

The folk claim: winning numbers' leading digits should follow Benford
(P(d) = log10(1 + 1/d), so ~30% start with 1). Benford applies to data
spanning orders of magnitude from multiplicative processes; numbers drawn
uniformly from a small bounded range are the textbook COUNTEREXAMPLE.
The arm exists precisely because its premise is falsifiable and false: it
scores candidate tickets by closeness to Benford and should sit exactly at
chance, making it a useful negative baseline for the whole portfolio.
"""
from __future__ import annotations

import math
import random

from ..data.sources import Draw
from ..games import Game

CANDIDATES = 100

BENFORD = {d: math.log10(1 + 1 / d) for d in range(1, 10)}


def _benford_distance(numbers: list[int]) -> float:
    counts = {d: 0 for d in range(1, 10)}
    for n in numbers:
        counts[int(str(n)[0])] += 1
    total = len(numbers)
    return sum((counts[d] / total - BENFORD[d]) ** 2 for d in range(1, 10))


def predict(game: Game, history: list[Draw], rng: random.Random):
    best, best_dist = None, float("inf")
    for _ in range(CANDIDATES):
        candidate = sorted(rng.sample(range(game.pick_min, game.pick_max + 1), game.pick_count))
        dist = _benford_distance(candidate)
        if dist < best_dist:
            best, best_dist = candidate, dist
    special = rng.randint(1, game.special_max) if game.special_max else None
    return best, special
