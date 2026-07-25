"""LLM prediction arms.

`llm-fewshot`: an LLM given recent-draw context with structured JSON output —
the no-training LLM control arm. Provider-pluggable:

- **ollama** (default): Ollama Cloud (https://ollama.com/api/chat, Bearer
  OLLAMA_API_KEY) or a local Ollama server (OLLAMA_HOST=http://localhost:11434,
  no key). Cheap/free; the daily loop makes only a handful of tiny calls.
- **anthropic**: Claude API (ANTHROPIC_API_KEY + the `anthropic` package).

Selection: LOTTERY_GURU_LLM_PROVIDER=ollama|anthropic, or auto-detected from
which credentials are present (Ollama wins if both are set).

`llm-tuned` (local only): the MLX LoRA-tuned model — see lottery_guru.finetune.
A fused adapter can be imported into Ollama so this same code path serves it.
"""
from __future__ import annotations

import json
import os
import random

import requests

from ..data.sources import Draw
from ..games import Game
from . import Prediction

CONTEXT_DRAWS = 20
DEFAULT_MODELS = {"ollama": "gpt-oss:20b", "anthropic": "claude-opus-5"}
SYSTEM_PROMPT = (
    "You are a lottery number predictor in a measurement experiment. "
    "Reply only with the JSON prediction."
)


def provider() -> str | None:
    explicit = os.environ.get("LOTTERY_GURU_LLM_PROVIDER")
    if explicit:
        return explicit
    if os.environ.get("OLLAMA_API_KEY") or os.environ.get("OLLAMA_HOST"):
        return "ollama"
    if os.environ.get("ANTHROPIC_API_KEY"):
        return "anthropic"
    return None


def model_name(prov: str) -> str:
    return os.environ.get("LOTTERY_GURU_LLM_MODEL", DEFAULT_MODELS[prov])


def available() -> bool:
    prov = provider()
    if prov == "ollama":
        return True  # cloud key or local host configured
    if prov == "anthropic":
        try:
            import anthropic  # noqa: F401
            return True
        except ImportError:
            return False
    return False


def build_prompt(game: Game, history: list[Draw]) -> str:
    recent = history[-CONTEXT_DRAWS:]
    lines = [
        f"{d.date} {d.draw_time}: {' '.join(map(str, d.numbers))}"
        + (f" + {d.special}" if d.special is not None else "")
        for d in recent
    ]
    if game.kind == "jackpot":
        spec = (
            f"Pick {game.pick_count} distinct numbers from {game.pick_min}-{game.pick_max}"
            f" and one special ball from 1-{game.special_max}."
        )
    else:
        spec = f"Pick {game.pick_count} digits, each 0-9 (order matters, repeats allowed)."
    return (
        f"Game: {game.display}. {spec}\n"
        f"Recent draws (oldest first):\n" + "\n".join(lines) + "\n"
        "Predict the next drawing."
    )


def _output_schema(game: Game) -> dict:
    props: dict = {
        "numbers": {"type": "array", "items": {"type": "integer"}},
    }
    required = ["numbers"]
    if game.special_max is not None:
        props["special"] = {"type": "integer"}
        required.append("special")
    return {
        "type": "object",
        "properties": props,
        "required": required,
        "additionalProperties": False,
    }


def sanitize(game: Game, numbers: list[int], special, rng: random.Random) -> Prediction:
    """Coerce model output into a valid ticket; fill gaps with seeded randomness."""
    if game.kind == "jackpot":
        valid = [n for n in dict.fromkeys(numbers) if isinstance(n, int) and game.pick_min <= n <= game.pick_max]
        pool = [n for n in range(game.pick_min, game.pick_max + 1) if n not in valid]
        while len(valid) < game.pick_count:
            valid.append(pool.pop(rng.randrange(len(pool))))
        nums = tuple(sorted(valid[: game.pick_count]))
        sp = special if isinstance(special, int) and 1 <= special <= game.special_max else rng.randint(1, game.special_max)
        return Prediction(numbers=nums, special=sp)
    digits = [n for n in numbers if isinstance(n, int) and 0 <= n <= 9]
    while len(digits) < game.pick_count:
        digits.append(rng.randint(0, 9))
    return Prediction(numbers=tuple(digits[: game.pick_count]), special=None)


def _predict_ollama(game: Game, history: list[Draw], rng: random.Random) -> Prediction:
    host = os.environ.get("OLLAMA_HOST", "https://ollama.com").rstrip("/")
    headers = {}
    key = os.environ.get("OLLAMA_API_KEY")
    if key:
        headers["Authorization"] = f"Bearer {key}"
    resp = requests.post(
        f"{host}/api/chat",
        headers=headers,
        json={
            "model": model_name("ollama"),
            "stream": False,
            "format": _output_schema(game),  # native structured-output support
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": build_prompt(game, history)},
            ],
        },
        timeout=120,
    )
    resp.raise_for_status()
    text = resp.json().get("message", {}).get("content", "{}")
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        data = {}
    return sanitize(game, data.get("numbers", []), data.get("special"), rng)


def _predict_anthropic(game: Game, history: list[Draw], rng: random.Random) -> Prediction:
    import anthropic

    client = anthropic.Anthropic()
    response = client.messages.create(
        model=model_name("anthropic"),
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        output_config={"format": {"type": "json_schema", "schema": _output_schema(game)}},
        messages=[{"role": "user", "content": build_prompt(game, history)}],
    )
    if response.stop_reason == "refusal":
        return sanitize(game, [], None, rng)
    text = next((b.text for b in response.content if b.type == "text"), "{}")
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        data = {}
    return sanitize(game, data.get("numbers", []), data.get("special"), rng)


def predict_fewshot(game: Game, history: list[Draw], rng: random.Random) -> Prediction:
    prov = provider()
    if prov == "ollama":
        return _predict_ollama(game, history, rng)
    if prov == "anthropic":
        return _predict_anthropic(game, history, rng)
    raise RuntimeError("no LLM provider configured")
