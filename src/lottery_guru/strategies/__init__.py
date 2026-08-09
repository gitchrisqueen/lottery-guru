"""Prediction strategies.

Every strategy is a hypothesis to falsify. Each takes the game, the historical
draws (oldest→newest), and a seeded RNG, and returns a Prediction. All are
deterministic per (strategy, game, date, draw_time) via the seed.
"""
from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass

from ..data.sources import Draw
from ..games import Game

from . import baselines, delta, positional, unpopular  # noqa: E402


@dataclass(frozen=True)
class Prediction:
    numbers: tuple[int, ...]
    special: int | None


def seeded_rng(strategy: str, game_key: str, date: str, draw_time: str) -> random.Random:
    digest = hashlib.sha256(f"{strategy}:{game_key}:{date}:{draw_time}".encode()).digest()
    return random.Random(int.from_bytes(digest[:8], "big"))


# name -> (predict_fn, applicable_fn)
REGISTRY = {
    "random": (baselines.predict_random, lambda g: True),
    "hot": (baselines.predict_hot, lambda g: True),
    "cold": (baselines.predict_cold, lambda g: True),
    "delta": (delta.predict, lambda g: g.kind == "jackpot"),
    "positional": (positional.predict, lambda g: g.kind == "digit"),
    # needs headroom above the birthday range — on FL Fantasy 5 (5/36) the
    # ">31" filter would collapse it to a near-constant 32-36 ticket
    "unpopular": (unpopular.predict, lambda g: g.kind == "jackpot" and g.pick_max - 31 >= 2 * g.pick_count),
}


def statistical_strategies(game: Game) -> list[str]:
    return [name for name, (_, applicable) in REGISTRY.items() if applicable(game)]


def run_strategy(name: str, game: Game, history: list[Draw], rng: random.Random) -> Prediction:
    predict_fn, applicable = REGISTRY[name]
    if not applicable(game):
        raise ValueError(f"strategy {name} not applicable to {game.key}")
    numbers, special = predict_fn(game, history, rng)
    return Prediction(numbers=tuple(numbers), special=special)
