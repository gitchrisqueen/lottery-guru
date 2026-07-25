"""JSON storage under data/ — git is the database."""
from __future__ import annotations

import json
from pathlib import Path

from .sources import Draw

DATA_DIR = Path("data")


def raw_path(game_key: str) -> Path:
    return DATA_DIR / "raw" / f"{game_key}.json"


def load_draws(game_key: str) -> list[Draw]:
    path = raw_path(game_key)
    if not path.exists():
        return []
    return [Draw.from_dict(d) for d in json.loads(path.read_text())]


def save_draws(game_key: str, draws: list[Draw]) -> None:
    path = raw_path(game_key)
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(set(draws), key=lambda d: (d.date, d.draw_time))
    path.write_text(json.dumps([d.to_dict() for d in ordered], indent=1) + "\n")


def merge_draws(game_key: str, new: list[Draw]) -> int:
    """Merge fetched draws into the store; returns count of newly added draws."""
    existing = load_draws(game_key)
    seen = {(d.date, d.draw_time) for d in existing}
    added = [d for d in new if (d.date, d.draw_time) not in seen]
    if added:
        save_draws(game_key, existing + added)
    return len(added)


def _dated_dir(name: str) -> Path:
    d = DATA_DIR / name
    d.mkdir(parents=True, exist_ok=True)
    return d


def load_json_list(name: str, date: str) -> list[dict]:
    path = _dated_dir(name) / f"{date}.json"
    if not path.exists():
        return []
    return json.loads(path.read_text())


def save_json_list(name: str, date: str, items: list[dict]) -> None:
    path = _dated_dir(name) / f"{date}.json"
    path.write_text(json.dumps(items, indent=1) + "\n")


def all_dates(name: str) -> list[str]:
    d = DATA_DIR / name
    if not d.exists():
        return []
    return sorted(p.stem for p in d.glob("*.json"))
