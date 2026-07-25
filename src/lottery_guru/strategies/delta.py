"""Delta system: model gaps between adjacent sorted winning numbers.

The delta distribution is real but is exactly what uniform sampling produces —
this arm exists to demonstrate that it confers no edge.
"""
from __future__ import annotations

import random

from ..data.sources import Draw
from ..games import Game


def predict(game: Game, history: list[Draw], rng: random.Random):
    deltas: list[int] = []
    for d in history[-500:]:
        nums = sorted(d.numbers)
        deltas.append(nums[0])  # first number counts as delta from 0
        deltas.extend(b - a for a, b in zip(nums, nums[1:]))
    if not deltas:
        deltas = list(range(1, 16))

    for _ in range(1000):
        picks = []
        total = 0
        ok = True
        for _ in range(game.pick_count):
            delta_val = max(1, rng.choice(deltas))
            total += delta_val
            if total > game.pick_max:
                ok = False
                break
            picks.append(total)
        if ok and len(set(picks)) == game.pick_count:
            special = rng.randint(1, game.special_max) if game.special_max else None
            return sorted(picks), special
    # fallback: uniform random
    numbers = sorted(rng.sample(range(game.pick_min, game.pick_max + 1), game.pick_count))
    special = rng.randint(1, game.special_max) if game.special_max else None
    return numbers, special
