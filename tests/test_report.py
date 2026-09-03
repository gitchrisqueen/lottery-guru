import pytest

from lottery_guru.data import store
from lottery_guru.evaluation import report


@pytest.fixture
def data_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(store, "DATA_DIR", tmp_path / "data")
    return tmp_path


def _eval(strategy, matches=0):
    return {"game": "ny_numbers", "draw_time": "midday", "strategy": strategy,
            "numbers": [1, 2, 3], "special": None, "actual_numbers": [1, 2, 3],
            "actual_special": None,
            "score": {"matches": matches, "special_hit": 0, "straight": 0}}


def seed_small_and_large_arms():
    # `hot` sits one draw under the rule, `random` exactly on it.
    store.save_json_list("evaluations", "2026-07-25",
                         [_eval("hot", 3)] * (report.MIN_N - 1)
                         + [_eval("random", 1)] * report.MIN_N)


def test_min_n_boundary():
    assert report.MIN_N == 50
    assert report.insufficient_sample(report.MIN_N - 1)
    assert not report.insufficient_sample(report.MIN_N)


def test_leaderboard_data_flags_small_arms_without_dropping_them(data_dir):
    seed_small_and_large_arms()
    rows = {r["strategy"]: r for r in report.leaderboard_data()["ny_numbers"]["rows"]}
    assert set(rows) == {"hot", "random"}
    assert rows["hot"]["n"] == report.MIN_N - 1
    assert rows["hot"]["insufficient_sample"] is True
    assert rows["random"]["insufficient_sample"] is False
    # z/p are still computed for the flagged arm — flagged, not hidden
    assert rows["hot"]["z"] > 3
    assert "p_value" in rows["hot"]


def test_build_report_marks_small_arms_and_states_rule(data_dir):
    seed_small_and_large_arms()
    out = report.build_report()
    # the rule is stated once, in the header, before any game section
    assert f"fewer than {report.MIN_N} scored draws" in out
    assert out.index("fewer than") < out.index("## NY Numbers")
    # the small arm is rendered, with its n and z, and carries the marker
    hot_line = next(l for l in out.splitlines() if l.startswith("| hot"))
    assert report.INSUFFICIENT_MARKER in hot_line
    assert f"| {report.MIN_N - 1} |" in hot_line
    assert "_" in hot_line.split("|")[5]  # z cell is italicised (flagged)
    # the adequately sampled arm is rendered plain
    random_line = next(l for l in out.splitlines() if l.startswith("| random"))
    assert report.INSUFFICIENT_MARKER not in random_line
    assert "_" not in random_line.split("|")[5]


def test_build_report_empty(data_dir):
    out = report.build_report()
    assert "No scored predictions yet" in out
    assert "Exploit watch" in out
