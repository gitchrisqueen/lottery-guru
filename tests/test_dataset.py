import json

from lottery_guru.finetune import dataset
from lottery_guru.data import store
from lottery_guru.data.sources import Draw


def test_export_is_time_ordered(tmp_path, monkeypatch):
    monkeypatch.setattr(store, "DATA_DIR", tmp_path / "data")
    draws = [
        Draw(date=f"2026-01-{day:02d}", draw_time="main",
             numbers=(day % 10, (day + 1) % 10, (day + 2) % 10), special=None)
        for day in range(1, 29)
    ]
    store.save_draws("ny_numbers", draws)

    out = tmp_path / "ft"
    counts = dataset.export(out_dir=str(out), context=3)
    assert counts["train"] > 0 and counts["test"] > 0
    assert counts["train"] >= counts["valid"]

    # every example is well-formed chat JSONL
    for split in ("train", "valid", "test"):
        for line in (out / f"{split}.jsonl").read_text().splitlines():
            ex = json.loads(line)
            roles = [m["role"] for m in ex["messages"]]
            assert roles == ["system", "user", "assistant"]
            answer = json.loads(ex["messages"][2]["content"])
            assert "numbers" in answer
