from lottery_guru.strategies import llm


def _clear(monkeypatch):
    for var in ("LOTTERY_GURU_LLM_PROVIDER", "OLLAMA_API_KEY", "OLLAMA_HOST",
                "ANTHROPIC_API_KEY", "LOTTERY_GURU_LLM_MODEL"):
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
