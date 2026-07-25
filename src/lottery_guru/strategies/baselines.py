"""Random (the null), hot (frequency), and cold (overdue) strategies."""
from __future__ import annotations

import random
from collections import Counter

from ..data.sources import Draw
from ..games import Game

WINDOW = 100  # trailing draws used by frequency strategies


def _pick_special(game: Game, rng: random.Random, ranked: list[int] | None = None) -> int | None:
    if game.special_max is None:
        return None
    if ranked:
        return ranked[0]
    return rng.randint(1, game.special_max)


def predict_random(game: Game, history: list[Draw], rng: random.Random):
    if game.kind == "jackpot":
        numbers = sorted(rng.sample(range(game.pick_min, game.pick_max + 1), game.pick_count))
    else:
        numbers = [rng.randint(0, 9) for _ in range(game.pick_count)]
    return numbers, _pick_special(game, rng)


def _frequency_ranked(game: Game, history: list[Draw], rng: random.Random, reverse: bool):
    """Rank numbers by trailing-window frequency (reverse=False → hot first)."""
    recent = history[-WINDOW:]
    counts: Counter[int] = Counter()
    special_counts: Counter[int] = Counter()
    for d in recent:
        counts.update(d.numbers)
        if d.special is not None:
            special_counts.update([d.special])
    domain = list(range(game.pick_min, game.pick_max + 1))
    rng.shuffle(domain)  # random tie-break, deterministic per seed
    ranked = sorted(domain, key=lambda n: counts[n], reverse=not reverse)
    special_ranked = None
    if game.special_max is not None:
        sdomain = list(range(1, game.special_max + 1))
        rng.shuffle(sdomain)
        special_ranked = sorted(sdomain, key=lambda n: special_counts[n], reverse=not reverse)
    return ranked, special_ranked


def predict_hot(game: Game, history: list[Draw], rng: random.Random):
    ranked, special_ranked = _frequency_ranked(game, history, rng, reverse=False)
    return _from_ranked(game, ranked, special_ranked, history, rng)


def predict_cold(game: Game, history: list[Draw], rng: random.Random):
    """Longest-absent ('overdue') numbers — the gambler's-fallacy control arm."""
    last_seen: dict[int, int] = {}
    for idx, d in enumerate(history):
        for n in d.numbers:
            last_seen[n] = idx
    domain = list(range(game.pick_min, game.pick_max + 1))
    rng.shuffle(domain)
    ranked = sorted(domain, key=lambda n: last_seen.get(n, -1))  # oldest-seen first

    special_ranked = None
    if game.special_max is not None:
        s_last: dict[int, int] = {}
        for idx, d in enumerate(history):
            if d.special is not None:
                s_last[d.special] = idx
        sdomain = list(range(1, game.special_max + 1))
        rng.shuffle(sdomain)
        special_ranked = sorted(sdomain, key=lambda n: s_last.get(n, -1))
    return _from_ranked(game, ranked, special_ranked, history, rng)


def _from_ranked(game: Game, ranked: list[int], special_ranked, history, rng: random.Random):
    if game.kind == "jackpot":
        numbers = sorted(ranked[: game.pick_count])
    else:
        # digit games: positional variant handled elsewhere; here take overall top digits
        top = ranked[: game.pick_count]
        numbers = [top[i % len(top)] for i in range(game.pick_count)]
    special = special_ranked[0] if special_ranked else None
    return numbers, special
