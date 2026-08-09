"""Pythagorean numerology strategy.

The classic system: map letters to digits (A=1..I=9, J=1..R=9, S=1..Z=8),
reduce sums to a root (preserving master numbers 11/22/33), and play numbers
derived from your name and birth date. The arm uses a fixed project persona —
name "Lottery Guru", birthdate 2026-07-01 (first commit) — plus the Personal
Day number for the drawing being predicted (the day after the newest draw in
history), so picks vary daily the way practitioners intend. Deterministic;
expected result: chance.
"""
from __future__ import annotations

import datetime as dt
import random

from ..data.sources import Draw
from ..games import Game

PERSONA_NAME = "LOTTERY GURU"
PERSONA_BIRTHDATE = dt.date(2026, 7, 1)

MASTER_NUMBERS = (11, 22, 33)


def _letter_value(ch: str) -> int:
    return (ord(ch) - ord("A")) % 9 + 1


def reduce_number(n: int) -> int:
    while n > 9 and n not in MASTER_NUMBERS:
        n = sum(int(d) for d in str(n))
    return n


def name_number(name: str) -> int:
    return reduce_number(sum(_letter_value(c) for c in name if c.isalpha()))


def life_path(date: dt.date) -> int:
    parts = [reduce_number(date.month), reduce_number(date.day), reduce_number(date.year)]
    return reduce_number(sum(parts))


def personal_day(life: int, date: dt.date) -> int:
    return reduce_number(life + date.month + date.day + reduce_number(date.year))


def predict(game: Game, history: list[Draw], rng: random.Random):
    if history:
        target = dt.date.fromisoformat(history[-1].date) + dt.timedelta(days=1)
    else:
        target = PERSONA_BIRTHDATE
    life = life_path(PERSONA_BIRTHDATE)
    roots = [name_number(PERSONA_NAME), life, personal_day(life, target)]

    if game.kind == "digit":
        # cycle the core numbers through the positions, reduced to one digit
        digits = [reduce_number(roots[i % len(roots)] + i) % 10 for i in range(game.pick_count)]
        return digits, None

    # expand the core numbers into the pool by successive multiples, the way
    # numerology guides pad a short list out to a full ticket
    span = game.pick_max - game.pick_min + 1
    numbers: list[int] = []
    step = 0
    while len(numbers) < game.pick_count:
        for root in roots:
            candidate = game.pick_min + (root * (step + 1) + step) % span
            if candidate not in numbers:
                numbers.append(candidate)
            if len(numbers) == game.pick_count:
                break
        step += 1
    special = None
    if game.special_max is not None:
        special = (personal_day(life, target) - 1) % game.special_max + 1
    return sorted(numbers), special
