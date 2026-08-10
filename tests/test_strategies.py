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
            special = rng.randint(1, game.special_max) if game.special_max else None
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
            if game.special_max is None:  # FL-style: no special ball
                assert pred.special is None
            else:
                assert 1 <= pred.special <= game.special_max
        else:
            assert pred.special is None


@pytest.mark.parametrize("game_key", list(GAMES))
def test_strategies_survive_an_empty_history(game_key):
    """A game can be registered before any of its draws have been pulled — a
    FL feed can soft-fail for days, and store.load_draws() returns [] for a
    file that does not exist yet. Every arm must still produce a valid ticket
    rather than break that morning's loop."""
    game = GAMES[game_key]
    for name, (_, applicable) in REGISTRY.items():
        if not applicable(game):
            continue
        pred = run_strategy(name, game, [], seeded_rng(name, game_key, "2026-08-10", "main"))
        assert len(pred.numbers) == game.pick_count, name
        for n in pred.numbers:
            assert game.pick_min <= n <= game.pick_max, name
        if game.kind == "jackpot":
            assert len(set(pred.numbers)) == game.pick_count, name


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


def test_contrarian_replays_recently_drawn_numbers():
    game = GAMES["powerball"]
    history = make_history("powerball")
    recent = {n for d in history[-3:] for n in d.numbers}
    pred = run_strategy("contrarian", game, history,
                        seeded_rng("contrarian", "powerball", "2026-07-25", "main"))
    assert set(pred.numbers) <= recent  # 3 draws x 5 numbers is a big enough pool


def test_birthday_stays_in_the_date_range():
    game = GAMES["powerball"]
    history = make_history("powerball")
    pred = run_strategy("birthday", game, history,
                        seeded_rng("birthday", "powerball", "2026-07-25", "main"))
    assert all(1 <= n <= 31 for n in pred.numbers)


def test_balanced_and_antibalanced_bracket_the_sum_band():
    from lottery_guru.strategies.balance import _sum_bounds

    game = GAMES["powerball"]
    history = make_history("powerball")
    lo, hi = _sum_bounds(game)
    mid = (lo + hi) / 2
    for date in (f"2026-07-{d:02d}" for d in range(1, 11)):
        bal = run_strategy("balanced", game, history, seeded_rng("balanced", "powerball", date, "main"))
        odd = sum(1 for n in bal.numbers if n % 2)
        assert abs(sum(bal.numbers) - mid) <= (hi - lo) * 0.15
        assert odd in (2, 3)
        anti = run_strategy("antibalanced", game, history,
                            seeded_rng("antibalanced", "powerball", date, "main"))
        anti_odd = sum(1 for n in anti.numbers if n % 2)
        assert abs(sum(anti.numbers) - mid) > (hi - lo) * 0.20 or anti_odd in (0, 5)


def test_skiphit_carries_repeats_from_the_last_draw():
    game = GAMES["powerball"]
    history = make_history("powerball")
    pred = run_strategy("skiphit", game, history,
                        seeded_rng("skiphit", "powerball", "2026-07-25", "main"))
    assert len(set(pred.numbers) & set(history[-1].numbers)) >= 1


def test_benford_prefers_benford_shaped_tickets():
    from lottery_guru.strategies.benford import _benford_distance

    game = GAMES["powerball"]
    history = make_history("powerball")
    pred = run_strategy("benford", game, history,
                        seeded_rng("benford", "powerball", "2026-07-25", "main"))
    baseline = random.Random(7)
    uniform_dists = [
        _benford_distance(sorted(baseline.sample(range(1, 70), 5))) for _ in range(50)
    ]
    assert _benford_distance(list(pred.numbers)) <= sum(uniform_dists) / len(uniform_dists)


def test_persistent_plays_the_same_ticket_forever():
    game = GAMES["powerball"]
    history = make_history("powerball")
    tickets = {
        run_strategy("persistent", game, history,
                     seeded_rng("persistent", "powerball", f"2026-07-{d:02d}", "main"))
        for d in range(1, 15)
    }
    assert len(tickets) == 1
    # ...but differs per game
    other = run_strategy("persistent", GAMES["megamillions"], make_history("megamillions"),
                         seeded_rng("persistent", "megamillions", "2026-07-01", "main"))
    assert next(iter(tickets)).numbers != other.numbers


def test_moonphase_epoch_is_a_new_moon():
    from lottery_guru.strategies.moonphase import KNOWN_NEW_MOON, phase_angle

    assert phase_angle(KNOWN_NEW_MOON) == 0.0
    assert 0.0 <= phase_angle(dt.date(2026, 7, 25)) < 360.0


def test_numerology_reduction_rules():
    from lottery_guru.strategies.numerology import name_number, reduce_number

    assert reduce_number(29) == 11  # 2+9 -> master number, preserved
    assert reduce_number(1997) == 8  # 1+9+9+7=26 -> 2+6
    assert 1 <= name_number("LOTTERY GURU") <= 33


def test_dreambook_plays_a_lexicon_gig():
    from lottery_guru.strategies.dreambook import _LEXICON

    game = GAMES["ny_numbers"]
    history = make_history("ny_numbers")
    pred = run_strategy("dreambook", game, history,
                        seeded_rng("dreambook", "ny_numbers", "2026-07-25", "midday"))
    assert any(list(pred.numbers) == gig[:3] for gig in _LEXICON.values())


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


def test_tuned_arm_draw_days_are_exactly_the_gpu_days():
    """The daily loop only deploys the tuned model when a TUNED_ARM_GAMES game
    draws (Powerball Mon/Wed/Sat, Mega Millions Tue/Fri). Sun/Thu keep the GPU
    off — FL Fantasy 5 is jackpot-kind and draws daily, so gating on kind
    would silently grow GPU spend to 7 days a week."""
    from lottery_guru.games import GAMES, TUNED_ARM_GAMES, draws_on

    tuned_days = {
        dt.date(2026, 8, 3) + dt.timedelta(days=i)  # Mon .. Sun
        for i in range(7)
        if any(g.key in TUNED_ARM_GAMES
               for g, _ in draws_on(dt.date(2026, 8, 3) + dt.timedelta(days=i)))
    }
    assert {d.weekday() for d in tuned_days} == {0, 1, 2, 4, 5}  # Mon,Tue,Wed,Fri,Sat
    # every day still has digit-game drawings, so the rest of the loop must run daily
    for i in range(7):
        date = dt.date(2026, 8, 3) + dt.timedelta(days=i)
        assert any(g.kind == "digit" for g, _ in draws_on(date)), date
