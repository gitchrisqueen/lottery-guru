"""LLM prediction arms.

`llm-fewshot`: Claude API with recent-draw context and structured output — the
no-training LLM control arm. Runs only when ANTHROPIC_API_KEY is set and the
anthropic package is installed; otherwise the predictor skips it cleanly.

`llm-tuned` (local only): same prompt served by a local MLX model with the
latest LoRA adapter — see lottery_guru.finetune.
"""
from __future__ import annotations

import json
import os
import random

from ..data.sources import Draw
from ..games import Game
from . import Prediction

MODEL = os.environ.get("LOTTERY_GURU_LLM_MODEL", "claude-opus-5")
CONTEXT_DRAWS = 20


def available() -> bool:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return False
    try:
        import anthropic  # noqa: F401
        return True
    except ImportError:
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
        valid = [n for n in dict.fromkeys(numbers) if game.pick_min <= n <= game.pick_max]
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


def predict_fewshot(game: Game, history: list[Draw], rng: random.Random) -> Prediction:
    import anthropic

    client = anthropic.Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=(
            "You are a lottery number predictor in a measurement experiment. "
            "Reply only with the JSON prediction."
        ),
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
