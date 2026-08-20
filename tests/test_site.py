import json

import pytest

from lottery_guru.data import store
from lottery_guru.evaluation import board, monitors, report, site


@pytest.fixture
def data_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(store, "DATA_DIR", tmp_path / "data")
    return tmp_path


def seed_evaluations():
    store.save_json_list("evaluations", "2026-07-25", [
        {"game": "ny_numbers", "draw_time": "midday", "strategy": "hot",
         "numbers": [1, 2, 3], "special": None, "actual_numbers": [1, 2, 3],
         "actual_special": None, "score": {"matches": 3, "special_hit": 0, "straight": 1}},
        {"game": "powerball", "draw_time": "main", "strategy": "random",
         "numbers": [1, 2, 3, 4, 5], "special": 7, "actual_numbers": [9, 8, 7, 6, 5],
         "actual_special": 7, "score": {"matches": 1, "special_hit": 1, "straight": 0}},
    ])


def test_scoreboard_payload_matches_board_ranking(data_dir):
    seed_evaluations()
    payload = site.scoreboard_payload()
    # same ranking the markdown scoreboard produces: hot outranks random
    names = [s["strategy"] for s in payload["strategies"]]
    assert names == ["hot", "random"]
    # cross-check numbers against board.strategy_totals directly
    per_strategy, overall = board.strategy_totals()
    hot = payload["strategies"][0]
    assert hot["n"] == per_strategy["hot"]["n"]
    assert hot["observed"] == per_strategy["hot"]["observed"]
    # payload is pre-rounded to the markdown's display precision (+.2f)
    z = board.z_score(per_strategy["hot"]["observed"], per_strategy["hot"]["expected"],
                      per_strategy["hot"]["var"])
    assert hot["z"] == float(f"{z:.2f}")
    assert payload["overall"]["n"] == overall["n"] == 2
    assert payload["overall"]["days"] == 1


def test_predictions_payload_carries_raw_numbers_not_markdown(data_dir):
    pred = {"game": "ny_numbers", "draw_time": "evening", "strategy": "hot",
            "numbers": [1, 2, 3], "special": None}
    store.save_json_list("predictions", "2026-07-26", [pred])
    store.save_json_list("evaluations", "2026-07-26", [{
        **pred, "actual_numbers": [1, 9, 3], "actual_special": None,
        "score": {"matches": 2, "special_hit": 0, "straight": 0},
    }])
    payload = site.predictions_payload()
    assert payload["date"] == "2026-07-26"
    [group] = payload["groups"]
    assert group["game"] == "ny_numbers"
    assert group["draw_time"] == "evening"
    assert group["scored"] is True
    [row] = group["rows"]
    assert row["predicted_numbers"] == [1, 2, 3]  # a real list, not "`1` `2` `3`"
    assert row["actual_numbers"] == [1, 9, 3]
    assert row["matches"] == 2


def test_predictions_payload_unscored_rows_have_null_actuals(data_dir):
    store.save_json_list("predictions", "2026-07-26", [
        {"game": "ny_numbers", "draw_time": "midday", "strategy": "random",
         "numbers": [4, 5, 6], "special": None},
    ])
    [group] = site.predictions_payload()["groups"]
    assert group["scored"] is False
    assert group["rows"][0]["actual_numbers"] is None
    assert group["rows"][0]["matches"] is None


def test_leaderboard_payload_all_games_sorted_by_z(data_dir):
    seed_evaluations()
    payload = site.leaderboard_payload()
    games = payload["games"]
    assert set(games) == {"ny_numbers", "powerball"}
    assert games == report.leaderboard_data()
    for entry in games.values():
        zs = [r["z"] for r in entry["rows"]]
        assert zs == sorted(zs, reverse=True)
        assert entry["null_expectation"] > 0


def test_monitors_payload_numeric_and_matches_monitors_rows(data_dir):
    payload = site.monitors_payload()
    assert payload["rows"] == monitors.rows()
    pb = next(r for r in payload["rows"] if r["game"] == "powerball")
    assert pb["combinations"] == 292_201_338
    assert pb["rolldown_defect"] is False
    assert "never prediction" in payload["note"]


def test_board_data_render_board_consistency(data_dir):
    """render_board() must be a pure formatter over board_data()."""
    pred = {"game": "powerball", "draw_time": "main", "strategy": "random",
            "numbers": [4, 12, 33, 41, 52], "special": 9}
    store.save_json_list("predictions", "2026-07-26", [pred])
    out = board.render_board()
    data = board.board_data()
    assert "Predictions for 2026-07-26" in out
    assert data["groups"][0]["rows"][0]["predicted_numbers"] == [4, 12, 33, 41, 52]
    assert "`04` `12` `33` `41` `52` + `09`" in out


def test_build_writes_expected_tree(data_dir, tmp_path):
    seed_evaluations()
    out = site.build(out_dir=tmp_path / "dist")
    assert (out / "index.html").exists()
    assert (out / "assets" / "style.css").exists()
    assert (out / "assets" / "app.js").exists()
    for name in site.PAYLOAD_NAMES:
        payload = json.loads((out / "data" / f"{name}.json").read_text())
        assert "generated_at" in payload


def test_empty_data_produces_valid_empty_payloads(data_dir):
    assert site.scoreboard_payload()["strategies"] == []
    assert site.predictions_payload()["groups"] == []
    assert site.leaderboard_payload()["games"] == {}


def test_shell_text_has_no_predictive_claims():
    """CLAUDE.md hard rule: never imply predictions can beat the lottery."""
    banned = ("guaranteed", "beat the odds", "winning system", "will win",
              "improve your odds", "pick winners")
    for path in site.TEMPLATE_DIR.rglob("*"):
        if path.is_file():
            text = path.read_text().lower()
            for phrase in banned:
                assert phrase not in text, f"{path.name} contains banned phrase: {phrase!r}"
