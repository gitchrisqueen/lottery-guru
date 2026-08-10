"""The `highest-frequency` consensus arm."""
import random

import pytest

from lottery_guru.games import GAMES
from lottery_guru.strategies import consensus, seeded_rng


def _rng(game_key="powerball"):
    return seeded_rng(consensus.NAME, game_key, "2026-08-01", "main")


@pytest.mark.parametrize("game_key", list(GAMES))
def test_produces_valid_tickets(game_key):
    game = GAMES[game_key]
    if game.kind == "jackpot":
        peers = [((1, 2, 3, 4, 5), 7), ((1, 2, 9, 10, 11), 7), ((1, 40, 41, 42, 43), 3)]
    else:
        peers = [((1, 2, 3, 4)[: game.pick_count], None),
                 ((1, 5, 3, 9)[: game.pick_count], None)]
    numbers, special = consensus.predict(game, peers, _rng(game_key))
    assert len(numbers) == game.pick_count
    assert all(game.pick_min <= n <= game.pick_max for n in numbers)
    if game.kind == "jackpot" and game.special_max is not None:
        assert len(set(numbers)) == game.pick_count
        assert numbers == tuple(sorted(numbers))
        assert 1 <= special <= game.special_max
    elif game.kind == "jackpot":  # FL-style jackpot game without a special ball
        assert len(set(numbers)) == game.pick_count
        assert numbers == tuple(sorted(numbers))
        assert special is None
    else:
        assert special is None


def test_most_picked_numbers_win():
    game = GAMES["powerball"]
    # 1 picked by all three, 2 by two, 3 by two; the rest once
    peers = [((1, 2, 3, 61, 62), 9), ((1, 2, 3, 63, 64), 9), ((1, 55, 56, 57, 58), 4)]
    numbers, special = consensus.predict(game, peers, _rng())
    assert {1, 2, 3}.issubset(numbers)
    assert special == 9  # picked twice vs once


def test_digit_games_tally_per_position():
    game = GAMES["ny_numbers"]
    # position 0 is 7 twice; position 1 is 4 twice; position 2 all distinct
    peers = [((7, 4, 1), None), ((7, 4, 2), None), ((3, 9, 8), None)]
    numbers, _ = consensus.predict(game, peers, _rng("ny_numbers"))
    assert numbers[0] == 7
    assert numbers[1] == 4


def test_deterministic_for_the_same_drawing_and_peers():
    game = GAMES["powerball"]
    peers = [((5, 6, 7, 8, 9), 1), ((10, 11, 12, 13, 14), 2)]
    a = consensus.predict(game, peers, _rng())
    b = consensus.predict(game, peers, _rng())
    assert a == b


def test_untallied_numbers_do_not_collapse_to_the_lowest():
    """Numbers nobody picked all tie at zero. Filling those slots by numeric
    order would quietly make the arm a constant, so ties use the seeded RNG."""
    game = GAMES["powerball"]
    picks = {
        consensus.predict(game, [], seeded_rng(consensus.NAME, "powerball", f"2026-08-{d:02d}", "main"))[0]
        for d in range(1, 15)
    }
    assert len(picks) > 1
    assert (1, 2, 3, 4, 5) not in picks


def test_a_single_peer_is_echoed_exactly():
    """One arm predicting means unanimous agreement with that arm."""
    game = GAMES["powerball"]
    numbers, special = consensus.predict(game, [((60, 61, 62, 63, 64), 20)], _rng())
    assert numbers == (60, 61, 62, 63, 64)
    assert special == 20


def test_no_peers_still_yields_a_valid_ticket():
    game = GAMES["powerball"]
    numbers, special = consensus.predict(game, [], _rng())
    assert len(set(numbers)) == game.pick_count
    assert 1 <= special <= game.special_max


def test_ignores_out_of_range_peer_values():
    game = GAMES["powerball"]
    peers = [((999, -1, 70, 5, 5), 99), ((5, 6, 7, 8, 9), 3)]
    numbers, special = consensus.predict(game, peers, _rng())
    assert all(1 <= n <= 69 for n in numbers)
    assert 5 in numbers  # the one number both peers agree on survives
    assert 1 <= special <= 26
