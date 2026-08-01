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


def test_export_never_crosses_rule_eras(tmp_path, monkeypatch):
    monkeypatch.setattr(store, "DATA_DIR", tmp_path / "data")
    # Mega Millions era starts 2025-04-08: pre-era draws (special up to 25)
    # must not appear in any example, even as context.
    pre = [Draw(date=f"2025-03-{day:02d}", draw_time="main",
                numbers=(1, 2, 3, 4, day), special=25) for day in range(1, 29)]
    post = [Draw(date=f"2025-05-{day:02d}", draw_time="main",
                 numbers=(5, 6, 7, 8, day), special=day) for day in range(1, 29)]
    store.save_draws("megamillions", pre + post)

    out = tmp_path / "ft"
    counts = dataset.export(out_dir=str(out), context=3)
    assert sum(counts.values()) == len(post) - 3
    for split in ("train", "valid", "test"):
        for line in (out / f"{split}.jsonl").read_text().splitlines():
            assert "2025-03-" not in line
            assert '"special": 25' not in line
