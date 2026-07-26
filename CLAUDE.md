# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this project is

An automated, honest lottery-prediction experiment. A daily GitHub Actions loop
pulls real drawing results, generates predictions from a portfolio of
strategies, scores them against actual drawings, and updates REPORT.md. The
scientific framing is central: **the null hypothesis (no strategy beats
chance) is expected to hold** — the project measures that convergence.
Never add code or copy that implies predictions can actually beat the lottery.

Read [docs/PLAN.md](docs/PLAN.md) (architecture, milestones) and
[docs/RESEARCH.md](docs/RESEARCH.md) (data sources, strategy literature,
null-hypothesis math) before making non-trivial changes.

## Commands

```bash
pip install -e ".[dev]"          # install with test deps
pytest                            # run the test suite
lottery-guru daily                # pull + score + predict + report (cron entry point)
lottery-guru pull --limit 2000    # backfill draw history
lottery-guru predict [--date YYYY-MM-DD] [--no-llm]
lottery-guru score                # score predictions whose results arrived (idempotent)
lottery-guru report               # regenerate REPORT.md
lottery-guru finetune export|train|eval   # MLX fine-tuning (macOS only)
```

## Architecture

- `src/lottery_guru/games.py` — game definitions (Powerball 5/69+1/26,
  Mega Millions 5/70+1/24, NY Numbers, NY Win 4) and draw schedules.
- `src/lottery_guru/data/` — Socrata fetchers (data.ny.gov), TX CSV
  cross-check, JSON storage under `data/` (**git is the database**; raw draws,
  predictions, and evaluations are committed by the daily workflow).
- `src/lottery_guru/strategies/` — each strategy is `(predict_fn, applicable_fn)`
  in `REGISTRY`. The LLM arm (`llm.py`) is provider-pluggable: Ollama
  (default, native `/api/chat` with JSON-schema `format`) or Anthropic.
- `src/lottery_guru/evaluation/` — scoring vs exact hypergeometric/binomial
  null moments, cumulative z-tests, REPORT.md rendering.
- `src/lottery_guru/predictor.py` — daily orchestration; `score_pending()` is
  idempotent and self-heals late-arriving results.
- `src/lottery_guru/finetune/` — time-ordered JSONL export + MLX-LM LoRA wrapper.

## Hard rules

- **Determinism:** statistical strategies must be reproducible per
  (strategy, game, date, draw_time) via `seeded_rng()`. Never use unseeded
  randomness in a strategy.
- **Time-ordered splits only** in fine-tuning: train on the past, test on the
  future. Never shuffle draws across the split boundary.
- **Never pool stats across rule eras** (Mega Millions changed to 5/70+1/24 in
  April 2025 — see `MEGAMILLIONS_ERA_START`).
- **LLM arm is best-effort:** it must never block or fail the daily loop;
  errors are warnings, and absence of credentials means clean skip.
- The scoring math in `evaluation/scoring.py` is verified against the exact
  hypergeometric PMF (Powerball var ≈ 0.31629) — don't "fix" it without
  re-deriving.

## Environment variables

| Var | Purpose |
|---|---|
| `OLLAMA_API_KEY` | Ollama Cloud auth (LLM arm; set as repo secret) |
| `OLLAMA_HOST` | Alternative Ollama endpoint (e.g. `http://localhost:11434`) |
| `LOTTERY_GURU_LLM_PROVIDER` | Force `ollama` or `anthropic` |
| `LOTTERY_GURU_LLM_MODEL` | Override model (default `gpt-oss:20b`) |
| `ANTHROPIC_API_KEY` | Anthropic provider (optional) |
| `SOCRATA_APP_TOKEN` | Optional; lifts data.ny.gov throttling |

## Testing

`pytest` must pass before any push. Tests are network-free (live feeds are
exercised only by the daily workflow). When adding a strategy, extend
`tests/test_strategies.py` — validity, determinism, and applicability are the
required assertions.
