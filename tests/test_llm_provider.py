from lottery_guru.data import store
from lottery_guru.finetune import fireworks
from lottery_guru.strategies import llm


def _clear(monkeypatch):
    for var in ("LOTTERY_GURU_LLM_PROVIDER", "OLLAMA_API_KEY", "OLLAMA_HOST",
                "ANTHROPIC_API_KEY", "LOTTERY_GURU_LLM_MODEL",
                "FIREWORKS_API_KEY", "FIREWORKS_ACCOUNT_ID"):
        monkeypatch.delenv(var, raising=False)


def test_no_credentials_means_no_provider(monkeypatch):
    _clear(monkeypatch)
    assert llm.provider() is None
    assert llm.available() is False


def test_ollama_auto_detected(monkeypatch):
    _clear(monkeypatch)
    monkeypatch.setenv("OLLAMA_API_KEY", "x")
    assert llm.provider() == "ollama"
    assert llm.available() is True
    assert llm.model_name("ollama") == "gpt-oss:20b"


def test_local_ollama_via_host(monkeypatch):
    _clear(monkeypatch)
    monkeypatch.setenv("OLLAMA_HOST", "http://localhost:11434")
    assert llm.provider() == "ollama"


def test_ollama_wins_when_both_present(monkeypatch):
    _clear(monkeypatch)
    monkeypatch.setenv("OLLAMA_API_KEY", "x")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "y")
    assert llm.provider() == "ollama"


def test_explicit_override(monkeypatch):
    _clear(monkeypatch)
    monkeypatch.setenv("OLLAMA_API_KEY", "x")
    monkeypatch.setenv("LOTTERY_GURU_LLM_PROVIDER", "anthropic")
    assert llm.provider() == "anthropic"


def test_model_override(monkeypatch):
    _clear(monkeypatch)
    monkeypatch.setenv("LOTTERY_GURU_LLM_MODEL", "qwen3:8b")
    assert llm.model_name("ollama") == "qwen3:8b"


def test_fireworks_auto_detected(monkeypatch):
    _clear(monkeypatch)
    monkeypatch.setenv("FIREWORKS_API_KEY", "fw")
    assert llm.provider() == "fireworks"
    assert llm.available() is True
    assert llm.model_name("fireworks") == "accounts/fireworks/models/llama-v3p1-8b-instruct"


def test_ollama_wins_over_fireworks(monkeypatch):
    _clear(monkeypatch)
    monkeypatch.setenv("OLLAMA_API_KEY", "x")
    monkeypatch.setenv("FIREWORKS_API_KEY", "fw")
    assert llm.provider() == "ollama"


def test_tuned_unavailable_without_key_or_record(monkeypatch, tmp_path):
    _clear(monkeypatch)
    monkeypatch.setattr(store, "DATA_DIR", tmp_path)
    assert llm.tuned_available() is False
    monkeypatch.setenv("FIREWORKS_API_KEY", "fw")
    assert llm.tuned_available() is False  # key but no trained-model record


def test_tuned_available_with_key_and_deployed_record(monkeypatch, tmp_path):
    _clear(monkeypatch)
    monkeypatch.setattr(store, "DATA_DIR", tmp_path)
    fireworks.save_record({
        "model": "accounts/acct/models/lottery-guru-2026-08-01",
        "deployed": True,
        "inference_model": "accounts/acct/models/lottery-guru-2026-08-01#accounts/acct/deployments/d1",
    })
    assert llm.tuned_available() is False  # record but no key
    monkeypatch.setenv("FIREWORKS_API_KEY", "fw")
    assert llm.tuned_model() == (
        "accounts/acct/models/lottery-guru-2026-08-01#accounts/acct/deployments/d1")
    assert llm.tuned_available() is True


def test_tuned_unavailable_when_deployment_torn_down(monkeypatch, tmp_path):
    _clear(monkeypatch)
    monkeypatch.setattr(store, "DATA_DIR", tmp_path)
    monkeypatch.setenv("FIREWORKS_API_KEY", "fw")
    fireworks.save_record({"model": "accounts/acct/models/m1", "deployed": False})
    assert llm.tuned_available() is False
