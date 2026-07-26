# GitHub Copilot instructions

This is **Lottery Guru**: an automated, honest lottery-prediction experiment.
A daily GitHub Actions loop pulls real drawing results (NY Open Data/Socrata),
generates predictions from a strategy portfolio, scores them against actual
drawings vs the exact null hypothesis, and commits results to the repo
(git is the database — `data/raw`, `data/predictions`, `data/evaluations`).

## Framing

The null hypothesis — no strategy beats chance — is expected to hold; the
project exists to measure that rigorously. Never generate code, comments, or
copy implying lottery draws are predictable.

## Project layout

- `src/lottery_guru/games.py` — game configs + draw schedules
- `src/lottery_guru/data/` — Socrata fetchers, TX cross-check, JSON store
- `src/lottery_guru/strategies/` — strategy `REGISTRY`; LLM arm in `llm.py`
  (Ollama default via native `/api/chat` + JSON-schema `format`; Anthropic optional)
- `src/lottery_guru/evaluation/` — hypergeometric/binomial null scoring, z-tests, REPORT.md
- `src/lottery_guru/predictor.py` — daily orchestration (idempotent scoring)
- `src/lottery_guru/finetune/` — time-ordered JSONL export + MLX LoRA training
- `tests/` — network-free pytest suite

## Conventions

- Python 3.10+, standard library + `requests` only in core (no new runtime deps
  without discussion); `anthropic` is an optional extra.
- Strategies must be **deterministic** per (strategy, game, date, draw_time)
  using `seeded_rng()` — never unseeded randomness.
- Fine-tuning data splits are strictly **time-ordered** (train past, test
  future) — never shuffle.
- Never pool statistics across game rule eras (Mega Millions era change
  April 2025).
- The LLM arm is best-effort: exceptions become warnings and must never fail
  the daily loop; missing credentials mean clean skip.
- Storage is committed JSON under `data/` — keep files small, sorted, and
  diff-friendly (`indent=1`, deterministic ordering).
- All tests must pass (`pytest`) and stay network-free; new strategies need
  validity + determinism tests in `tests/test_strategies.py`.
