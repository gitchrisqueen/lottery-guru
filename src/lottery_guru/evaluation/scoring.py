"""Score predictions against actual drawings, vs the exact null hypothesis.

Jackpot games: white-ball matches follow Hypergeometric(N=pick_max, K=pick_count,
n=pick_count). Powerball null: E[white matches] = 25/69 ≈ 0.3623, var ≈ 0.3242.
Digit games: per-position matches follow Binomial(pick_count, 1/10).
"""
from __future__ import annotations

import math

from ..games import Game


def score(game: Game, pred_numbers: list[int], pred_special, actual_numbers: list[int], actual_special) -> dict:
    if game.kind == "jackpot":
        matches = len(set(pred_numbers) & set(actual_numbers))
        special_hit = int(pred_special is not None and pred_special == actual_special)
        return {"matches": matches, "special_hit": special_hit, "straight": int(matches == game.pick_count and special_hit == 1)}
    matches = sum(1 for a, b in zip(pred_numbers, actual_numbers) if a == b)
    return {"matches": matches, "special_hit": 0, "straight": int(list(pred_numbers) == list(actual_numbers))}


def null_moments(game: Game) -> tuple[float, float]:
    """(expected matches, variance of matches) per draw under the null."""
    if game.kind == "jackpot":
        n_total, k = game.pick_max, game.pick_count
        mean = k * k / n_total
        var = (k * k / n_total) * ((n_total - k) / n_total) * ((n_total - k) / (n_total - 1))
        return mean, var
    p = 1 / 10
    return game.pick_count * p, game.pick_count * p * (1 - p)


def special_null_p(game: Game) -> float:
    return 1 / game.special_max if game.special_max else 0.0


def aggregate(game: Game, scores: list[dict]) -> dict:
    """Cumulative stats for one (strategy, game) arm vs the null."""
    n = len(scores)
    if n == 0:
        return {"n": 0}
    observed = sum(s["matches"] for s in scores)
    mean, var = null_moments(game)
    expected = mean * n
    sd = math.sqrt(var * n) if var > 0 else 0.0
    z = (observed - expected) / sd if sd > 0 else 0.0
    p_value = math.erfc(abs(z) / math.sqrt(2))  # two-sided normal approximation
    out = {
        "n": n,
        "observed_matches": observed,
        "expected_matches": round(expected, 3),
        "z": round(z, 3),
        "p_value": round(p_value, 4),
        "straights": sum(s["straight"] for s in scores),
    }
    if game.special_max:
        sp_observed = sum(s["special_hit"] for s in scores)
        out["special_hits"] = sp_observed
        out["special_expected"] = round(special_null_p(game) * n, 3)
    return out
