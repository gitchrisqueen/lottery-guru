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
lottery-guru board                # render PREDICTIONS.md + README marker sections
lottery-guru finetune export|train|eval   # MLX fine-tuning (macOS only)
lottery-guru finetune train --provider fireworks --min-scored-days 60  # hosted (CI; monthly workflow)
lottery-guru finetune deploy|teardown     # tuned-model GPU deployment (daily loop; teardown stops billing)
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
  null moments, cumulative z-tests, REPORT.md rendering, and `board.py`
  (PREDICTIONS.md + the README `PREDICTIONS`/`SCOREBOARD` marker sections).
  README sections are spliced between HTML comment markers — never hand-edit
  content inside them; it is regenerated every run.
- `src/lottery_guru/predictor.py` — daily orchestration; `score_pending()` is
  idempotent and self-heals late-arriving results.
- `src/lottery_guru/finetune/` — time-ordered JSONL export + MLX-LM LoRA wrapper
  (local) + Fireworks.ai LoRA client (`fireworks.py`, trained monthly by
  `.github/workflows/monthly-finetune.yml`; the tuned model name is recorded in
  `data/finetune/fireworks.json` and served by the `llm-tuned` arm). Serving
  needs an on-demand GPU deployment that **bills while it exists** — the daily
  loop deploys, predicts, and tears down; teardown runs on `always()` and
  sweeps orphans. Never add a code path that creates a deployment without a
  guaranteed teardown.

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
| `FIREWORKS_API_KEY` | Fireworks.ai auth: monthly fine-tune + `llm-tuned` arm (repo secret) |
| `FIREWORKS_ACCOUNT_ID` | Fireworks.ai account slug (optional; auto-resolved from the key) |
| `LOTTERY_GURU_FT_BASE_MODEL` | Override the Fireworks fine-tune base model |
| `SOCRATA_APP_TOKEN` | Optional; lifts data.ny.gov throttling |

## Testing

`pytest` must pass before any push. Tests are network-free (live feeds are
exercised only by the daily workflow). When adding a strategy, extend
`tests/test_strategies.py` — validity, determinism, and applicability are the
required assertions.
