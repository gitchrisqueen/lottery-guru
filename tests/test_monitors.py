"""Exploit-watch monitor math."""
from lottery_guru.evaluation import monitors
from lottery_guru.games import GAMES


def test_powerball_combination_count_is_exact():
    # C(69,5) * 26 — the published 1-in-292,201,338 jackpot odds
    assert monitors.combinations(GAMES["powerball"]) == 292_201_338


def test_no_special_ball_games_multiply_by_one():
    assert monitors.combinations(GAMES["fl_lotto"]) == 22_957_480  # C(53,6)
    assert monitors.combinations(GAMES["fl_fantasy5"]) == 376_992  # C(36,5)


def test_break_even_exceeds_buyout_cost():
    for key in ("powerball", "megamillions", "fl_lotto", "fl_jtp", "fl_fantasy5"):
        game = GAMES[key]
        assert monitors.break_even_jackpot(game) > monitors.buyout_cost(game)


def test_render_covers_every_jackpot_game():
    text = "\n".join(monitors.render_lines())
    for game in GAMES.values():
        assert (game.display in text) == (game.kind == "jackpot")
