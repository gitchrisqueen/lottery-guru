"""Skip-and-hit strategy — Gail Howard's flagship system, mechanized.

Howard's *Advantage Gold* claims each number has characteristic "skip"
behavior: track games-since-last-hit, play numbers whose current skip matches
their most frequent historical skip, and always carry one or two repeats from
the last drawing (her best-known rule: about half of winning numbers repeat
from the recent window). No independent review has found an edge; a fair
draw has geometric, memoryless skips. Expected result: chance.
"""
from __future__ import annotations

import random
from collections import Counter

from ..data.sources import Draw
from ..games import Game

REPEATS = 2  # numbers carried over from the last drawing


def _skip_score(appearances: list[int], n_draws: int) -> float:
    """|current skip - modal historical skip| — 0 means "due" by Howard's rule."""
    if len(appearances) < 2:
        return float("inf")
    gaps = Counter(b - a for a, b in zip(appearances, appearances[1:]))
    modal_gap = gaps.most_common(1)[0][0]
    current_skip = n_draws - appearances[-1]
    return abs(current_skip - modal_gap)


def _rank_by_skip(domain: list[int], appearances: dict[int, list[int]],
                  n_draws: int, rng: random.Random) -> list[int]:
    order = list(domain)
    rng.shuffle(order)  # deterministic tie-break
    return sorted(order, key=lambda n: _skip_score(appearances.get(n, []), n_draws))


def predict(game: Game, history: list[Draw], rng: random.Random):
    n_draws = len(history)
    if game.kind == "jackpot":
        appearances: dict[int, list[int]] = {}
        for idx, d in enumerate(history):
            for n in d.numbers:
                appearances.setdefault(n, []).append(idx)
        carried = []
        if history:
            last = [n for n in history[-1].numbers if game.pick_min <= n <= game.pick_max]
            carried = sorted(rng.sample(last, min(REPEATS, len(last), game.pick_count)))
        ranked = _rank_by_skip(
            [n for n in range(game.pick_min, game.pick_max + 1) if n not in carried],
            appearances, n_draws, rng)
        numbers = sorted(carried + ranked[: game.pick_count - len(carried)])

        if game.special_max is None:
            return numbers, None
        s_appearances: dict[int, list[int]] = {}
        for idx, d in enumerate(history):
            if d.special is not None:
                s_appearances.setdefault(d.special, []).append(idx)
        special = _rank_by_skip(list(range(1, game.special_max + 1)),
                                s_appearances, n_draws, rng)[0]
        return numbers, special

    digits = []
    for position in range(game.pick_count):
        appearances = {}
        for idx, d in enumerate(history):
            if len(d.numbers) > position:
                appearances.setdefault(d.numbers[position], []).append(idx)
        digits.append(_rank_by_skip(list(range(10)), appearances, n_draws, rng)[0])
    return digits, None
