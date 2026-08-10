"""`highest-frequency`: rank numbers by how many *other arms* picked them.

This is a consensus (ensemble) arm, not a draw-frequency one — `hot` ranks
numbers by how often they were actually DRAWN; this ranks them by how often
they were PREDICTED today by the rest of the portfolio, `random` included.

Tallies are strictly per drawing: one game, one draw_time, one date. Numbers
from a Powerball ticket never count toward a Win 4 prediction, and midday
never counts toward evening — the pools are different sizes and the draws are
independent.

Expected result: chance. Averaging predictors that each sit at chance cannot
manufacture signal; agreement between them is itself noise. The arm measures
that, which is the point.
"""
from __future__ import annotations

import random
from collections import Counter
from collections.abc import Sequence

from ..games import Game

NAME = "highest-frequency"

# (numbers, special) as produced by the other arms for the same drawing
Peer = tuple[Sequence[int], int | None]


def _rank(candidates: list[int], tally: Counter, rng: random.Random) -> list[int]:
    """Most-picked first. Ties (the common case) broken by the seeded RNG.

    With ~7 arms picking 5 of 69, most numbers are picked once or not at all,
    so tie-breaking decides most of the ticket. Shuffling first and then
    stable-sorting by count keeps that deterministic per
    (strategy, game, date, draw_time) without biasing toward low numbers.
    """
    order = list(candidates)
    rng.shuffle(order)
    return sorted(order, key=lambda n: -tally[n])


def predict(game: Game, peers: list[Peer], rng: random.Random):
    """Return (numbers, special) — the most-agreed-upon ticket for this drawing."""
    if game.kind == "jackpot":
        tally = Counter(
            n for numbers, _ in peers for n in set(numbers)
            if isinstance(n, int) and game.pick_min <= n <= game.pick_max
        )
        pool = list(range(game.pick_min, game.pick_max + 1))
        numbers = tuple(sorted(_rank(pool, tally, rng)[: game.pick_count]))

        if game.special_max is None:  # FL-style jackpot games have no special ball
            return numbers, None
        special_tally = Counter(
            s for _, s in peers
            if isinstance(s, int) and 1 <= s <= game.special_max
        )
        special = _rank(list(range(1, game.special_max + 1)), special_tally, rng)[0]
        return numbers, special

    # digit games: order matters and digits repeat, so tally per position
    digits = []
    for position in range(game.pick_count):
        tally = Counter(
            numbers[position] for numbers, _ in peers
            if len(numbers) > position and isinstance(numbers[position], int)
            and 0 <= numbers[position] <= 9
        )
        digits.append(_rank(list(range(10)), tally, rng)[0])
    return tuple(digits), None
