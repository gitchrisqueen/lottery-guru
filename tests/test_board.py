import pytest

from lottery_guru.data import store
from lottery_guru.evaluation import board


@pytest.fixture
def data_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(store, "DATA_DIR", tmp_path / "data")
    return tmp_path


def test_format_numbers_jackpot_and_digit():
    assert board.format_numbers("powerball", [4, 12, 33], 9) == "`04` `12` `33` + `09`"
    assert board.format_numbers("ny_numbers", [5, 6, 6], None) == "`5` `6` `6`"


def test_render_board_without_results(data_dir):
    store.save_json_list("predictions", "2026-07-26", [
        {"game": "ny_numbers", "draw_time": "midday", "strategy": "random",
         "numbers": [1, 2, 3], "special": None},
    ])
    out = board.render_board()
    assert "Predictions for 2026-07-26" in out
    assert "NY Numbers (Pick 3) — midday" in out
    assert "| `random` | `1` `2` `3` |" in out
    assert "Actual" not in out


def test_render_board_with_results_shows_actual_and_matches(data_dir):
    pred = {"game": "ny_numbers", "draw_time": "evening", "strategy": "hot",
            "numbers": [1, 2, 3], "special": None}
    store.save_json_list("predictions", "2026-07-26", [pred])
    store.save_json_list("evaluations", "2026-07-26", [{
        **pred,
        "actual_numbers": [1, 9, 3],
        "actual_special": None,
        "score": {"matches": 2, "special_hit": 0, "straight": 0},
    }])
    out = board.render_board()
    assert "| Strategy | Predicted | Actual | Matches |" in out
    assert "`1` `9` `3`" in out
    assert "| 2 |" in out


def test_render_board_empty(data_dir):
    assert "No predictions recorded yet" in board.render_board()


def test_scoreboard_pools_games_and_ranks(data_dir):
    store.save_json_list("evaluations", "2026-07-25", [
        {"game": "ny_numbers", "draw_time": "midday", "strategy": "hot",
         "numbers": [1, 2, 3], "special": None, "actual_numbers": [1, 2, 3],
         "actual_special": None, "score": {"matches": 3, "special_hit": 0, "straight": 1}},
        {"game": "powerball", "draw_time": "main", "strategy": "random",
         "numbers": [1, 2, 3, 4, 5], "special": 7, "actual_numbers": [9, 8, 7, 6, 5],
         "actual_special": 7, "score": {"matches": 1, "special_hit": 1, "straight": 0}},
    ])
    out = board.render_scoreboard()
    assert "2** predictions scored" in out
    assert "`hot`" in out and "`random`" in out
    # hot went 3-for-3 on a 0.3-expectation game, so it must outrank random
    assert out.index("`hot`") < out.index("`random`")
    assert "Best single" in out


def test_scoreboard_empty(data_dir):
    assert "No predictions scored yet" in board.render_scoreboard()


def test_update_readme_splices_both_sections(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text(
        "# Title\n\n"
        f"{board.START_MARKER}\nold board\n{board.END_MARKER}\n\n"
        f"{board.SCOREBOARD_START}\nold stats\n{board.SCOREBOARD_END}\n\ntail\n"
    )
    changed = board.update_readme("NEW BOARD\n", scoreboard="NEW STATS\n", path=str(readme))
    text = readme.read_text()
    assert changed
    assert "NEW BOARD" in text and "NEW STATS" in text
    assert "old board" not in text and "old stats" not in text
    assert text.startswith("# Title") and text.rstrip().endswith("tail")


def test_update_readme_is_idempotent(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text(f"{board.START_MARKER}\nX\n{board.END_MARKER}\n")
    assert board.update_readme("X\n", path=str(readme)) is False


def test_update_readme_without_markers_is_noop(tmp_path):
    readme = tmp_path / "README.md"
    readme.write_text("# No markers here\n")
    assert board.update_readme("body\n", path=str(readme)) is False
    assert readme.read_text() == "# No markers here\n"
