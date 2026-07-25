"""Positional digit-frequency strategy for Pick 3 / Win 4 style games."""
from __future__ import annotations

import random
from collections import Counter

from ..data.sources import Draw
from ..games import Game

WINDOW = 200


def predict(game: Game, history: list[Draw], rng: random.Random):
    recent = history[-WINDOW:]
    numbers = []
    for pos in range(game.pick_count):
        counts: Counter[int] = Counter(d.numbers[pos] for d in recent if len(d.numbers) > pos)
        if counts:
            digits = list(range(10))
            weights = [counts.get(d, 0) + 1 for d in digits]  # +1 smoothing
            numbers.append(rng.choices(digits, weights=weights, k=1)[0])
        else:
            numbers.append(rng.randint(0, 9))
    return numbers, None
