"""FL PDF parser tests against real pdftotext extracts (tests/fixtures/fl/).

Fixtures were captured by .github/workflows/fl-source-spike.yml from the live
files and contain each file's newest page plus its oldest (last) page, so both
the current format and the oldest era's format are covered. Network-free.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from lottery_guru.data import florida
from lottery_guru.games import GAMES

FIXTURES = Path(__file__).parent / "fixtures" / "fl"

FL_GAMES = [k for k, g in GAMES.items() if g.fl_pdf_stem]


def load(stem: str) -> str:
    return (FIXTURES / f"{stem}.txt").read_text()


@pytest.mark.parametrize("game_key", FL_GAMES)
def test_parses_valid_draws_from_fixture(game_key):
    game = GAMES[game_key]
    draws = florida.parse_text(game, load(game.fl_pdf_stem))
    assert len(draws) >= 40  # every fixture holds pages of history
    for d in draws:
        assert len(d.numbers) == game.pick_count
        assert all(game.pick_min <= n <= game.pick_max for n in d.numbers)
        assert d.special is None
        assert d.draw_time in ("main", "midday", "evening")
        year = int(d.date[:4])
        assert 1988 <= year <= 2100
    if game.kind == "jackpot":
        for d in draws:
            assert sorted(d.numbers) == list(d.numbers)
            assert len(set(d.numbers)) == game.pick_count


def test_fantasy5_known_rows():
    draws = florida.parse_text(GAMES["fl_fantasy5"], load("ff"))
    by_key = {(d.date, d.draw_time): d.numbers for d in draws}
    assert by_key[("2026-08-08", "evening")] == (2, 10, 15, 16, 32)
    assert by_key[("2026-08-08", "midday")] == (4, 6, 10, 19, 21)
    # oldest era: evening-only, 5/26 matrix, 19xx century rule
    assert by_key[("1995-01-26", "evening")] == (9, 14, 18, 19, 22)


def test_lotto_keeps_main_and_drops_double_play():
    draws = florida.parse_text(GAMES["fl_lotto"], load("l6"))
    by_date = {d.date: d.numbers for d in draws}
    assert by_date["2026-08-08"] == (3, 11, 20, 25, 40, 42)  # LOTTO row
    assert (3, 7, 13, 16, 37, 44) not in by_date.values()  # its LOTTO DP twin
    # unlabeled 6/49-era row from the last page (1988)
    assert by_date["1988-10-29"] == (4, 8, 24, 34, 43, 45)
    # one main draw per date — DP rows must not leak in
    assert len(draws) == len(by_date)


def test_jtp_known_row():
    draws = florida.parse_text(GAMES["fl_jtp"], load("jtp"))
    by_date = {d.date: d.numbers for d in draws}
    assert by_date["2026-08-07"] == (3, 22, 26, 34, 37, 38)


def test_pick3_strips_fireball_and_keeps_order():
    draws = florida.parse_text(GAMES["fl_pick3"], load("p3"))
    by_key = {(d.date, d.draw_time): d.numbers for d in draws}
    assert by_key[("2026-08-08", "evening")] == (6, 4, 3)  # order preserved, FB 2 dropped
    assert by_key[("2026-07-13", "midday")] == (7, 9, 3)  # middle page column
    assert by_key[("2026-06-16", "evening")] == (5, 0, 0)  # right page column


def test_pick2_parses_pre_fireball_rows():
    draws = florida.parse_text(GAMES["fl_pick2"], load("p2"))
    by_key = {(d.date, d.draw_time): d.numbers for d in draws}
    assert by_key[("2016-10-18", "evening")] == (7, 1)  # 2016 row, no FB column


def test_limit_caps_parsed_draws():
    draws = florida.parse_text(GAMES["fl_fantasy5"], load("ff"), limit=10)
    assert len(draws) == 10


def test_fetch_stops_reading_pages_once_the_limit_is_met(monkeypatch):
    """The daily pull needs ~200 draws from files up to 130 pages long.
    Layout extraction costs seconds per page, so it must stop early."""
    pages = [p for p in load("ff").split("Draw Date   Draw Type") if p.strip()]
    assert len(pages) > 1, "fixture should span more than one page"
    read = []

    def fake_pages(pdf_bytes):
        for i, page in enumerate(pages):
            read.append(i)
            yield page

    monkeypatch.setattr(florida, "_download", lambda stem: b"%PDF-fake")
    monkeypatch.setattr(florida, "iter_page_texts", fake_pages)
    draws = florida.fetch_draws(GAMES["fl_fantasy5"], limit=5)
    assert len(draws) == 5
    assert read == [0]  # stopped after the first page satisfied the limit


def test_fetch_reads_every_page_when_the_limit_is_high(monkeypatch):
    pages = [p for p in load("ff").split("Draw Date   Draw Type") if p.strip()]
    read = []

    def fake_pages(pdf_bytes):
        for i, page in enumerate(pages):
            read.append(i)
            yield page

    monkeypatch.setattr(florida, "_download", lambda stem: b"%PDF-fake")
    monkeypatch.setattr(florida, "iter_page_texts", fake_pages)
    draws = florida.fetch_draws(GAMES["fl_fantasy5"], limit=100_000)
    assert read == list(range(len(pages)))  # nothing skipped
    assert len(draws) >= 40
