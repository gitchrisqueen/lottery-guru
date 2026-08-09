"""Dream-book strategy — the Harlem numbers-game tradition, mechanized.

In the interwar numbers game (New York's *numbers*, Chicago's *policy*),
players converted dreams into daily 3-digit plays via published dream books —
Herbert Gladstone Parris's *H. P. Dream Book* (1926), *Policy Pete's* (1933),
*Aunt Sally's* before them. Dream books are natively Pick-3 instruments, so
this arm is restricted to digit games.

Mechanization: the day's "dream" is a symbol drawn (seeded, deterministic)
from a lexicon of traditional dream subjects; the symbol's fixed digits are
the play. The bundled lexicon uses the public-domain-era symbol list with
digits derived deterministically from each symbol — publishers' tables always
disagreed with one another, and the property under test is the ritual's
invariant (the same dream always yields the same number), not any one
publisher's table. Expected result: chance.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

from ..data.sources import Draw
from ..games import Game

_LEXICON_PATH = Path(__file__).with_name("dreambook_lexicon.json")
_LEXICON: dict[str, list[int]] = json.loads(_LEXICON_PATH.read_text())
_SYMBOLS = sorted(_LEXICON)


def predict(game: Game, history: list[Draw], rng: random.Random):
    symbol = rng.choice(_SYMBOLS)  # the day's dream
    gig = _LEXICON[symbol]
    return list(gig[: game.pick_count]), None
