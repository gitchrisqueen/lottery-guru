"""Local fine-tuning via MLX-LM (Apple Silicon). Cost: $0.

Requires: pip install mlx-lm   (macOS / Apple Silicon only)

The recommended base is a small 4-bit instruct model; QLoRA on 3-4B fits in
16 GB and trains in minutes at this dataset size. Adapters are written to
adapters/<date>/ and the evaluate step compares tuned vs base on the held-out
(future) test window — the honest measurement.

Hosted alternative (if CI needs to call the tuned model): Fireworks.ai
serverless LoRA, ~$0.50/M training tokens (<$1/run at this dataset size).
"""
from __future__ import annotations

import datetime as dt
import json
import platform
import subprocess
import sys
from pathlib import Path

DEFAULT_BASE_MODEL = "mlx-community/Qwen3-4B-Instruct-2507-4bit"


def _check_mlx() -> None:
    if platform.system() != "Darwin":
        sys.exit("MLX fine-tuning requires macOS/Apple Silicon. See module docstring for the hosted alternative.")
    try:
        import mlx_lm  # noqa: F401
    except ImportError:
        sys.exit("mlx-lm not installed. Run: pip install mlx-lm")


def train(data_dir: str = "finetune_data", base_model: str = DEFAULT_BASE_MODEL,
          iters: int = 400) -> str:
    _check_mlx()
    adapter_dir = Path("adapters") / dt.date.today().isoformat()
    adapter_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable, "-m", "mlx_lm", "lora",
        "--model", base_model,
        "--train",
        "--data", data_dir,
        "--adapter-path", str(adapter_dir),
        "--iters", str(iters),
        "--batch-size", "2",
        "--learning-rate", "1e-5",
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)
    (adapter_dir / "training_meta.json").write_text(json.dumps({
        "base_model": base_model,
        "data_dir": data_dir,
        "iters": iters,
        "trained_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    }, indent=1))
    return str(adapter_dir)


def evaluate(data_dir: str = "finetune_data", base_model: str = DEFAULT_BASE_MODEL,
             adapter_path: str | None = None) -> None:
    """Report held-out test loss for base vs tuned (mlx_lm's --test mode)."""
    _check_mlx()
    for label, extra in (("base", []), ("tuned", ["--adapter-path", adapter_path] if adapter_path else None)):
        if extra is None:
            continue
        cmd = [
            sys.executable, "-m", "mlx_lm", "lora",
            "--model", base_model,
            "--data", data_dir,
            "--test",
            *extra,
        ]
        print(f"--- {label} model test loss ---")
        subprocess.run(cmd, check=True)
