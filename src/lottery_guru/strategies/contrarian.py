"""Clotfelter-contrarian strategy — play numbers that just hit.

Clotfelter & Cook (Management Science, 1993) measured the gambler's fallacy
in a real daily numbers game: money bet on a number FALLS sharply right after
it is drawn and takes months to recover. So recently drawn numbers are
under-bet by the public, and in any parimutuel or jackpot-splitting game,
betting them buys the same odds with fewer co-winners. Match-count scoring
expects chance — the (unmeasured here) claim is split-risk, like `unpopular`.
"""
from __future__ import annotations

import random

from ..data.sources import Draw
from ..games import Game

RECENT = 3  # draws whose numbers the public is currently avoiding


def predict(game: Game, history: list[Draw], rng: random.Random):
    recent = history[-RECENT:]
    if game.kind == "jackpot":
        pool = sorted({n for d in recent for n in d.numbers
                       if game.pick_min <= n <= game.pick_max})
        rng.shuffle(pool)
        numbers = pool[: game.pick_count]
        if len(numbers) < game.pick_count:  # thin history: fill uniformly
            rest = [n for n in range(game.pick_min, game.pick_max + 1) if n not in numbers]
            numbers += rng.sample(rest, game.pick_count - len(numbers))
        specials = [d.special for d in recent if d.special is not None]
        if game.special_max is None:
            special = None
        else:
            special = rng.choice(specials) if specials else rng.randint(1, game.special_max)
        return sorted(numbers), special

    digits = []
    for position in range(game.pick_count):
        seen = [d.numbers[position] for d in recent if len(d.numbers) > position]
        digits.append(rng.choice(seen) if seen else rng.randint(0, 9))
    return digits, None
