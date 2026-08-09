"""Source-layer dispatch and the daily pull's per-game soft-fail. Network-free."""
import dataclasses

import pytest
import requests

from lottery_guru import predictor
from lottery_guru.data import florida, sources, store
from lottery_guru.games import GAMES


def test_fetch_draws_dispatches_socrata_games(monkeypatch):
    rows = [{"draw_date": "2026-08-05T00:00:00.000",
             "winning_numbers": "10 20 30 40 50 6"}]
    monkeypatch.setattr(sources, "_socrata_get", lambda dataset, limit: rows)
    draws = sources.fetch_draws(GAMES["powerball"], limit=5)
    assert draws[0].numbers == (10, 20, 30, 40, 50)
    assert draws[0].special == 6


def test_fetch_draws_dispatches_fl_games(monkeypatch):
    sentinel = [sources.Draw("2026-08-08", "evening", (1, 2, 3, 4, 5), None)]
    monkeypatch.setattr(florida, "fetch_draws", lambda game, limit: sentinel)
    assert sources.fetch_draws(GAMES["fl_fantasy5"], limit=5) == sentinel


def test_fetch_draws_rejects_sourceless_games():
    orphan = dataclasses.replace(GAMES["powerball"], socrata_dataset=None, fl_pdf_stem=None)
    with pytest.raises(ValueError, match="no data source"):
        sources.fetch_draws(orphan, limit=5)


def test_pull_soft_fails_per_game(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(store, "DATA_DIR", tmp_path / "data")

    def fake_fetch(game, limit):
        if game.key == "fl_lotto":
            raise RuntimeError("WAF said no")
        return [sources.Draw("2026-08-08", game.draw_times[0],
                             tuple(range(game.pick_min, game.pick_min + game.pick_count)),
                             1 if game.special_max else None)]

    monkeypatch.setattr(sources, "fetch_draws", fake_fetch)
    monkeypatch.setattr(sources, "cross_check_powerball", lambda pb: [])
    added = predictor.pull(limit=5)
    assert "fl_lotto" not in added  # the failed game is skipped, not fatal
    assert added["powerball"] == 1  # every other game still merged
    assert added["fl_fantasy5"] == 1
    assert "WARNING: pull failed for fl_lotto" in capsys.readouterr().out


def test_fl_download_fails_over_to_the_mirror(monkeypatch):
    calls = []

    class FakeResponse:
        content = b"%PDF-fake"

        def raise_for_status(self):
            pass

    def fake_get(url, **kwargs):
        calls.append(url)
        if url.startswith(florida.PRIMARY_BASE):
            raise requests.ConnectionError("primary down")
        return FakeResponse()

    monkeypatch.setattr(florida.requests, "get", fake_get)
    assert florida._download("ff") == b"%PDF-fake"
    assert calls == [f"{florida.PRIMARY_BASE}/ff.pdf", f"{florida.MIRROR_BASE}/ff.pdf"]


def test_fl_download_reports_both_hosts_down(monkeypatch):
    def fake_get(url, **kwargs):
        raise requests.ConnectionError("down")

    monkeypatch.setattr(florida.requests, "get", fake_get)
    with pytest.raises(RuntimeError, match="unavailable on both hosts"):
        florida._download("ff")
