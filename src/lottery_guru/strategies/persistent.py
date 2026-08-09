"""Lustig-persistent strategy — one ticket per game, played forever.

Richard Lustig (seven Florida prizes, 1993-2010) preached picking a set of
numbers and never changing it. Persistence cannot change per-draw odds in a
memoryless game, which makes this the cleanest possible null arm: any
apparent streak is pure noise by construction.

Seeding note: this arm deliberately seeds from (strategy, game) ONLY —
excluding date and draw_time — because an unchanging ticket is the whole
hypothesis. It is still fully deterministic and reproducible; the passed
per-drawing rng is unused by design (documented exception in CLAUDE.md).
"""
from __future__ import annotations

import hashlib
import random

from ..data.sources import Draw
from ..games import Game


def _fixed_rng(game: Game) -> random.Random:
    digest = hashlib.sha256(f"persistent:{game.key}".encode()).digest()
    return random.Random(int.from_bytes(digest[:8], "big"))


def predict(game: Game, history: list[Draw], rng: random.Random):
    fixed = _fixed_rng(game)
    if game.kind == "jackpot":
        numbers = sorted(fixed.sample(range(game.pick_min, game.pick_max + 1), game.pick_count))
    else:
        numbers = [fixed.randint(0, 9) for _ in range(game.pick_count)]
    special = fixed.randint(1, game.special_max) if game.special_max else None
    return numbers, special
