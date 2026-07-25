import math

from lottery_guru.evaluation import scoring
from lottery_guru.games import GAMES


def test_powerball_null_moments():
    mean, var = scoring.null_moments(GAMES["powerball"])
    # E = 25/69, var checked against exact hypergeometric PMF
    assert math.isclose(mean, 25 / 69, rel_tol=1e-9)
    assert math.isclose(var, 0.31629, abs_tol=1e-4)


def test_pick3_null_moments():
    mean, var = scoring.null_moments(GAMES["ny_numbers"])
    assert math.isclose(mean, 0.3)
    assert math.isclose(var, 3 * 0.1 * 0.9)


def test_jackpot_scoring_counts_set_matches():
    game = GAMES["powerball"]
    s = scoring.score(game, [1, 2, 3, 4, 5], 10, [3, 4, 5, 60, 61], 10)
    assert s["matches"] == 3
    assert s["special_hit"] == 1
    assert s["straight"] == 0


def test_jackpot_straight():
    game = GAMES["powerball"]
    s = scoring.score(game, [1, 2, 3, 4, 5], 10, [5, 4, 3, 2, 1], 10)
    assert s["matches"] == 5 and s["straight"] == 1


def test_digit_scoring_is_positional():
    game = GAMES["ny_numbers"]
    s = scoring.score(game, [1, 2, 3], None, [1, 3, 2], None)
    assert s["matches"] == 1  # only position 0 matches
    assert s["straight"] == 0
    s2 = scoring.score(game, [7, 7, 7], None, [7, 7, 7], None)
    assert s2["matches"] == 3 and s2["straight"] == 1


def test_aggregate_z_near_zero_for_expected_performance():
    game = GAMES["ny_numbers"]
    # 100 predictions each with exactly the expected 0.3 matches on average
    scores = [{"matches": 1, "special_hit": 0, "straight": 0}] * 30 + \
             [{"matches": 0, "special_hit": 0, "straight": 0}] * 70
    agg = scoring.aggregate(game, scores)
    assert agg["n"] == 100
    assert abs(agg["z"]) < 0.01
    assert agg["p_value"] > 0.9
