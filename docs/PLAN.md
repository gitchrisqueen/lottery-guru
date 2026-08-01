# Lottery Guru — Project Plan

## What this project is

An automated, honest experiment: pull real lottery drawings daily, generate predictions from a
portfolio of strategies (statistical folk methods + an LLM arm), score every prediction against
the actual drawing, and periodically fine-tune a local LLM on the accumulated
(context → prediction → outcome) history to measure whether anything improves over time.

**The scientific framing (and the fun of it):** lottery draws are independent uniform samples.
The null hypothesis — no strategy beats chance — is almost certainly true, and this project is
the instrument that demonstrates it with real money-free data. Every strategy is a hypothesis to
falsify; the leaderboard's convergence to the theoretical baseline *is* the product. The one
strategy with defensible math (`unpopular`) doesn't improve match odds at all — it improves
expected payout conditional on winning by avoiding numbers humans over-pick.

## Games tracked

| Game | Format | Draws | Why |
|---|---|---|---|
| `powerball` | 5 of 69 + 1 of 26 | Mon/Wed/Sat | flagship, deep history (2010→) |
| `megamillions` | 5 of 70 + 1 of 24 | Tue/Fri | second jackpot game (era-split Apr 2025) |
| `ny_numbers` | 3 ordered digits 0–9 | daily ×2 (midday/evening) | **daily** predictions need a daily game |
| `ny_win4` | 4 ordered digits 0–9 | daily ×2 | second daily stream |

There is a drawing every single day of the week across these four, so the daily loop always has
something to predict and something to score.

## Architecture

```
data.ny.gov (Socrata JSON, nightly ~08:00 UTC)  ──┐
texaslottery.com CSVs (cross-check, intraday)  ───┤
                                                  ▼
                                       src/lottery_guru/data/
                                       fetch → normalize → data/raw/{game}.json
                                                  │
                    ┌─────────────────────────────┼──────────────────────────┐
                    ▼                             ▼                          ▼
             strategies/*                  evaluation/scoring          finetune/dataset
     each: predict(game, history)     score predictions vs actual    (ctx, pred, outcome)
     → numbers (+ optional prob       matches, z vs null, log-loss,        → JSONL
        vector over the ball space)   prize tier, cumulative stats          │
                    │                             │                         ▼
                    ▼                             ▼                  mlx_lm.lora (local)
        data/predictions/YYYY-MM-DD.json   data/evaluations/*.json   → adapters/ → llm
                    └─────────────► REPORT.md leaderboard ◄─────────  strategy uses it
```

Storage is **git-as-database**: JSON files committed to the repo. At this scale (a few KB/day)
that gives free history, diffs, and reproducibility with zero infrastructure.

## Components

### 1. Data layer (`data/`)
- `sources.py` — Socrata fetchers per game (with `$order=draw_date DESC` incremental pulls),
  TX CSV fetcher for Powerball/Mega cross-checks. Retries + timeout; optional
  `SOCRATA_APP_TOKEN` env var.
- `store.py` — normalized draw records `{date, draw_time, numbers[], special}` in
  `data/raw/{game}.json`, deduped, sorted. Backfill = same code path, just deeper `$limit`.
- Integrity: Powerball/Mega rows diffed against TX CSV when both present; mismatch → warning
  in the daily log, never silent.

### 2. Strategy layer (`strategies/`)
Common interface: `predict(game, history, rng) -> Prediction{numbers, special, probs?}`.
Arms: `random` (null), `hot`, `cold`, `delta`, `positional` (digit games), `unpopular`
(jackpot games), `llm-fewshot` (Claude API, no training — the LLM control arm),
`llm-tuned` (local MLX model + latest LoRA adapter, once one exists).
Deterministic per (strategy, game, date) via seeded RNG so reruns are reproducible.

### 3. Evaluation layer (`evaluation/`)
- Per-prediction: white/digit matches, special-ball hit, prize tier.
- Per-strategy cumulative: observed vs expected matches under the exact null
  (hypergeometric for jackpot games, binomial for digit games), z-score, two-sided p-value.
- Log-loss vs uniform for strategies emitting probability vectors.
- `report.py` renders `REPORT.md`: leaderboard table + "days run / expected vs observed"
  and a plain-language verdict line per strategy.

### 4. Daily automation (GitHub Actions, `daily.yml`)
Cron **10:15 UTC daily** (after NY's nightly batch):
1. `lottery-guru pull` — fetch new results
2. `lottery-guru score` — score all unscored past predictions that now have results
3. `lottery-guru predict` — generate today's predictions for whichever games draw today
   (LLM few-shot arm runs only if `ANTHROPIC_API_KEY` secret is set; skipped cleanly otherwise)
4. `lottery-guru report` — regenerate REPORT.md
5. Commit & push the changed JSON/report back to the repo

The same commands run locally, so the Mac and CI are interchangeable.

### 5. Fine-tuning loop (`finetune/`, local Mac — MLX)
- `dataset.py` — export chat-format JSONL from history: system prompt fixes the JSON output
  contract; user message carries recent-draw context; assistant message is the *actual* drawn
  numbers. **Time-ordered** train/valid/test split — never train on the future.
- `train_mlx.py` — wraps `mlx_lm.lora` (QLoRA on `mlx-community/Qwen3-4B-Instruct-2507-4bit`
  by default), writes adapters to `adapters/{date}/`, records train/valid loss.
- `evaluate` — runs base vs tuned on the held-out future window: mean matches vs null,
  valid-JSON rate, per-number marginal chi-square, prediction entropy (mode-collapse detector).
- Cadence: monthly (or on demand) once ≥60 scored days exist. Hosted path implemented
  (`finetune/fireworks.py` + `.github/workflows/monthly-finetune.yml`): Fireworks.ai
  serverless LoRA (<$1/run) trains monthly in CI, commits the tuned model name to
  `data/finetune/fireworks.json`, and the daily loop's `llm-tuned` arm calls it.

## Milestones

- **M0 (today):** research + plan committed; repo live.
- **M1 (today):** data layer + backfill working against live NY/TX feeds.
- **M2 (today):** all statistical strategies + scorer + report; tests green; Actions cron enabled.
- **M3 (day 1+):** daily loop producing predictions/scores autonomously; LLM few-shot arm on.
- **M4 (~day 60):** first MLX fine-tune; four-arm comparison (random / frequency / base LLM /
  tuned LLM) in REPORT.md.
- **M5 (ongoing):** quarterly randomness audit of the draws themselves; write-up of results.

## Risks & mitigations

- **Schema/endpoint drift** (NY dataset IDs stable since ~2013, but): TX cross-check + loud
  failure in CI rather than silent staleness.
- **Era changes** (ball-range rule changes): game config carries era boundaries; stats never
  pool across eras (Mega Millions 2025 change already handled).
- **LLM mode collapse / leakage:** entropy monitoring, time-ordered splits, valid-JSON rate.
- **Actions cron jitter** (can run late): `score` is idempotent and scores *any* pending
  prediction whose result has arrived, so a late/missed run self-heals next day.
- **Expectation management:** README states up front that no strategy is expected to beat
  chance and that this is a measurement instrument, not gambling advice.
