"""The deploy guard that decides whether we pay for a GPU today."""
import pytest

from lottery_guru.cli import main
from lottery_guru.data import store
from lottery_guru.finetune import fireworks

SUNDAY = "2026-08-02"   # no TUNED_ARM_GAMES drawing (NY + FL dailies only)
MONDAY = "2026-08-03"   # Powerball


@pytest.fixture
def env(monkeypatch, tmp_path):
    monkeypatch.setattr(store, "DATA_DIR", tmp_path / "data")
    monkeypatch.setenv("FIREWORKS_API_KEY", "fw-key")
    monkeypatch.setenv("FIREWORKS_ACCOUNT_ID", "acct")
    return tmp_path


@pytest.fixture
def deployed(monkeypatch):
    """Stand in for a successful deployment, recording the calls."""
    calls = []

    def fake(record):
        calls.append(record)
        record.update({"deployed": True, "deployment": "accounts/acct/deployments/d1"})
        fireworks.save_record(record)

    monkeypatch.setattr(fireworks, "_deploy_and_record", fake)
    return calls


def test_no_gpu_on_non_tuned_days(env, deployed, capsys):
    fireworks.save_record({"model": "accounts/acct/models/m1"})
    assert main(["finetune", "deploy", "--only-if-drawings", "tuned", "--date", SUNDAY]) == 0
    assert deployed == []  # the whole point: no GPU billed
    assert "no tuned drawings" in capsys.readouterr().out


def test_gpu_on_tuned_game_days(env, deployed):
    fireworks.save_record({"model": "accounts/acct/models/m1"})
    assert main(["finetune", "deploy", "--only-if-drawings", "tuned", "--date", MONDAY]) == 0
    assert len(deployed) == 1


def test_jackpot_kind_gate_now_includes_fl_daily_games(env, deployed):
    """FL Fantasy 5 is jackpot-kind and draws every day, so the old 'jackpot'
    gate would deploy on Sunday too — which is why daily.yml uses 'tuned'."""
    fireworks.save_record({"model": "accounts/acct/models/m1"})
    assert main(["finetune", "deploy", "--only-if-drawings", "jackpot", "--date", SUNDAY]) == 0
    assert len(deployed) == 1


def test_bare_flag_still_deploys_on_ny_only_days(env, deployed):
    """Without a kind, any drawing qualifies — and NY games draw every day."""
    fireworks.save_record({"model": "accounts/acct/models/m1"})
    assert main(["finetune", "deploy", "--only-if-drawings", "--date", SUNDAY]) == 0
    assert len(deployed) == 1


def test_no_tuned_model_exits_cleanly(env, monkeypatch, capsys):
    monkeypatch.setattr(fireworks, "_deploy_and_record",
                        lambda r: pytest.fail("must not deploy without a model"))
    assert main(["finetune", "deploy", "--only-if-drawings", "jackpot", "--date", MONDAY]) == 0
    assert "no tuned model" in capsys.readouterr().out


def test_failed_deployment_reports_nonzero(env, monkeypatch):
    fireworks.save_record({"model": "accounts/acct/models/m1"})
    monkeypatch.setattr(fireworks, "_deploy_and_record", lambda r: None)  # leaves deployed unset
    assert main(["finetune", "deploy", "--date", MONDAY]) == 1
