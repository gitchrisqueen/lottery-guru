"""Export chat-format JSONL for fine-tuning.

Task: given the recent-draw context, predict the next drawing. The assistant
turn is the ACTUAL drawn numbers, so a model trained on this data is being
asked to learn structure in i.i.d. uniform draws — the held-out test window
measures whether it found any (it shouldn't, beyond format compliance).

Splits are strictly time-ordered: train on the past, validate/test on the
future. Never shuffle.
"""
from __future__ import annotations

import json
from pathlib import Path

from ..data import store
from ..games import GAMES, Game
from ..strategies import llm as llm_strategy

SYSTEM_PROMPT = (
    "You are a lottery number predictor in a measurement experiment. "
    "Reply only with JSON: {\"numbers\": [...]} plus \"special\" for jackpot games."
)


def _example(game: Game, history, actual) -> dict:
    answer: dict = {"numbers": list(actual.numbers)}
    if actual.special is not None:
        answer["special"] = actual.special
    return {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": llm_strategy.build_prompt(game, history)},
            {"role": "assistant", "content": json.dumps(answer)},
        ]
    }


def export(out_dir: str = "finetune_data", context: int = llm_strategy.CONTEXT_DRAWS,
           max_per_game: int = 500) -> dict[str, int]:
    """Write train/valid/test.jsonl (80/10/10, time-ordered) across all games."""
    examples: list[dict] = []
    for game in GAMES.values():
        draws = store.load_draws(game.key)
        if game.era_start:  # never train across rule eras
            draws = [d for d in draws if d.date >= game.era_start]
        draws = draws[-(max_per_game + context):]
        for i in range(context, len(draws)):
            examples.append(_example(game, draws[i - context:i], draws[i]))
    # interleave games but keep global time order within each game (already sorted)
    n = len(examples)
    splits = {
        "train": examples[: int(n * 0.8)],
        "valid": examples[int(n * 0.8): int(n * 0.9)],
        "test": examples[int(n * 0.9):],
    }
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    counts = {}
    for name, part in splits.items():
        (out / f"{name}.jsonl").write_text(
            "\n".join(json.dumps(e) for e in part) + ("\n" if part else "")
        )
        counts[name] = len(part)
    return counts
