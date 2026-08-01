import datetime as dt
import random

import pytest

from lottery_guru.data.sources import Draw
from lottery_guru.games import GAMES
from lottery_guru.strategies import REGISTRY, run_strategy, seeded_rng
from lottery_guru.strategies import llm as llm_strategy


def make_history(game_key: str, n: int = 120) -> list[Draw]:
    rng = random.Random(42)
    game = GAMES[game_key]
    out = []
    for i in range(n):
        if game.kind == "jackpot":
            nums = tuple(sorted(rng.sample(range(1, game.pick_max + 1), game.pick_count)))
            special = rng.randint(1, game.special_max)
        else:
            nums = tuple(rng.randint(0, 9) for _ in range(game.pick_count))
            special = None
        out.append(Draw(date=f"2025-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}",
                        draw_time="main", numbers=nums, special=special))
    return out


@pytest.mark.parametrize("game_key", list(GAMES))
def test_all_applicable_strategies_produce_valid_tickets(game_key):
    game = GAMES[game_key]
    history = make_history(game_key)
    for name, (_, applicable) in REGISTRY.items():
        if not applicable(game):
            continue
        rng = seeded_rng(name, game_key, "2026-07-25", "main")
        pred = run_strategy(name, game, history, rng)
        assert len(pred.numbers) == game.pick_count
        for n in pred.numbers:
            assert game.pick_min <= n <= game.pick_max
        if game.kind == "jackpot":
            assert len(set(pred.numbers)) == game.pick_count  # no duplicates
            assert pred.numbers == tuple(sorted(pred.numbers))
            assert 1 <= pred.special <= game.special_max
        else:
            assert pred.special is None


def test_predictions_are_deterministic_per_seed():
    game = GAMES["powerball"]
    history = make_history("powerball")
    for name, (_, applicable) in REGISTRY.items():
        if not applicable(game):
            continue
        a = run_strategy(name, game, history, seeded_rng(name, "powerball", "2026-07-25", "main"))
        b = run_strategy(name, game, history, seeded_rng(name, "powerball", "2026-07-25", "main"))
        assert a == b, name


def test_unpopular_avoids_birthday_heavy_tickets():
    game = GAMES["powerball"]
    history = make_history("powerball")
    pred = run_strategy("unpopular", game, history,
                        seeded_rng("unpopular", "powerball", "2026-07-25", "main"))
    assert sum(1 for n in pred.numbers if n > 31) >= 3


def test_llm_sanitize_recovers_from_garbage():
    game = GAMES["powerball"]
    rng = random.Random(1)
    pred = llm_strategy.sanitize(game, [1, 1, 999, -4, 2], 500, rng)
    assert len(pred.numbers) == 5
    assert len(set(pred.numbers)) == 5
    assert all(1 <= n <= 69 for n in pred.numbers)
    assert 1 <= pred.special <= 26

    game3 = GAMES["ny_numbers"]
    pred3 = llm_strategy.sanitize(game3, [11, 3], None, rng)
    assert len(pred3.numbers) == 3
    assert all(0 <= n <= 9 for n in pred3.numbers)


def test_predictions_only_cover_games_drawing_that_day():
    """No arm may predict a drawing that will not occur (and none may be missed)."""
    from lottery_guru.games import GAMES, draws_on

    for offset in range(14):  # two full weeks covers every game's schedule
        date = dt.date(2026, 8, 1) + dt.timedelta(days=offset)
        scheduled = {(g.key, t) for g, t in draws_on(date)}
        for game in GAMES.values():
            drawing_today = date.weekday() in game.draw_weekdays
            for draw_time in game.draw_times:
                assert ((game.key, draw_time) in scheduled) == drawing_today, (
                    f"{game.key}/{draw_time} on {date} ({date:%a})")
        # jackpot games never share a day, so a day is never empty of NY draws
        assert scheduled, f"no drawings computed for {date}"
