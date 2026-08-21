# 🎰 Lottery Guru

[![Live dashboard](https://img.shields.io/badge/📊_live_dashboard-gitchrisqueen.github.io%2Flottery--guru-4056a1)](https://gitchrisqueen.github.io/lottery-guru/)
[![Deploy dashboard](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/pages.yml/badge.svg)](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/pages.yml)
[![Daily prediction loop](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/daily.yml/badge.svg)](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/daily.yml)

**📊 [View the live dashboard →](https://gitchrisqueen.github.io/lottery-guru/)** — sortable leaderboards, today's picks, and the exploit watch, rebuilt after every daily loop.

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-08-21

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Mega Millions**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `26` `52` `57` `61` `70` + `20` |
| `balanced` | `35` `37` `40` `49` `56` + `05` |
| `benford` | `03` `16` `17` `23` `40` + `19` |
| `birthday` | `01` `03` `06` `23` `26` + `05` |
| `cold` | `06` `08` `11` `28` `69` + `18` |
| `contrarian` | `19` `27` `59` `60` `68` + `17` |
| `delta` | `08` `19` `31` `36` `40` + `21` |
| `highest-frequency` | `26` `37` `38` `40` `68` + `21` |
| `hot` | `21` `43` `49` `59` `63` + `12` |
| `llm-fewshot` | `07` `18` `33` `55` `68` + `09` |
| `llm-tuned` | `11` `38` `43` `47` `50` + `23` |
| `moonphase` | `12` `15` `37` `55` `65` + `08` |
| `numerology` | `02` `10` `12` `20` `24` + `01` |
| `persistent` | `01` `09` `37` `38` `39` + `22` |
| `random` | `13` `17` `26` `35` `46` + `07` |
| `skiphit` | `27` `30` `38` `46` `68` + `21` |
| `unpopular` | `32` `33` `37` `50` `52` + `10` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `1` `8` |
| `contrarian` | `2` `0` `5` |
| `dreambook` | `5` `9` `2` |
| `highest-frequency` | `7` `1` `5` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `3` `7` `1` |
| `llm-tuned` | `7` `3` `5` |
| `moonphase` | `8` `5` `5` |
| `numerology` | `1` `1` `5` |
| `persistent` | `4` `3` `3` |
| `positional` | `7` `2` `3` |
| `random` | `3` `9` `4` |
| `skiphit` | `9` `2` `3` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `1` `8` |
| `contrarian` | `9` `0` `3` |
| `dreambook` | `3` `9` `0` |
| `highest-frequency` | `3` `1` `5` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `7` `5` `0` |
| `llm-tuned` | `3` `1` `9` |
| `moonphase` | `4` `6` `6` |
| `numerology` | `1` `1` `5` |
| `persistent` | `4` `3` `3` |
| `positional` | `4` `7` `8` |
| `random` | `3` `7` `1` |
| `skiphit` | `2` `2` `5` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `9` `4` `3` |
| `contrarian` | `1` `6` `1` `5` |
| `dreambook` | `9` `6` `9` `7` |
| `highest-frequency` | `1` `6` `1` `5` |
| `hot` | `8` `3` `6` `5` |
| `llm-fewshot` | `1` `5` `6` `3` |
| `llm-tuned` | `1` `1` `1` `4` |
| `moonphase` | `9` `6` `0` `3` |
| `numerology` | `1` `1` `5` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `9` `4` `4` `1` |
| `random` | `7` `6` `1` `5` |
| `skiphit` | `2` `6` `1` `5` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `9` `3` `4` |
| `contrarian` | `2` `6` `1` `5` |
| `dreambook` | `4` `5` `2` `3` |
| `highest-frequency` | `5` `9` `3` `5` |
| `hot` | `8` `3` `6` `5` |
| `llm-fewshot` | `4` `0` `3` `1` |
| `llm-tuned` | `1` `0` `9` `9` |
| `moonphase` | `5` `5` `3` `3` |
| `numerology` | `1` `1` `5` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `5` `4` `5` `2` |
| `random` | `7` `9` `5` `9` |
| `skiphit` | `2` `6` `1` `5` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `12` `20` `21` `35` `36` |
| `balanced` | `01` `05` `14` `28` `35` |
| `benford` | `04` `10` `13` `28` `34` |
| `birthday` | `02` `05` `08` `10` `14` |
| `cold` | `02` `10` `28` `34` `35` |
| `contrarian` | `01` `02` `21` `29` `33` |
| `delta` | `06` `10` `14` `23` `24` |
| `highest-frequency` | `02` `10` `14` `24` `36` |
| `hot` | `12` `16` `23` `24` `36` |
| `llm-fewshot` | `11` `17` `27` `29` `36` |
| `llm-tuned` | `03` `16` `23` `33` `34` |
| `moonphase` | `07` `10` `22` `24` `25` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `02` `04` `06` `31` `32` |
| `skiphit` | `03` `09` `13` `20` `25` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `02` `06` `10` `20` |
| `balanced` | `07` `12` `19` `25` `34` |
| `benford` | `05` `11` `16` `24` `32` |
| `birthday` | `05` `06` `09` `10` `12` |
| `cold` | `01` `12` `20` `30` `36` |
| `contrarian` | `02` `04` `15` `22` `36` |
| `delta` | `12` `13` `22` `24` `30` |
| `highest-frequency` | `10` `12` `22` `26` `32` |
| `hot` | `02` `07` `27` `29` `34` |
| `llm-fewshot` | `04` `09` `12` `18` `26` |
| `llm-tuned` | `07` `13` `18` `26` `31` |
| `moonphase` | `03` `08` `10` `12` `32` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `14` `22` `27` `28` `32` |
| `skiphit` | `21` `22` `26` `28` `32` |

**FL Jackpot Triple Play**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `04` `07` `14` `17` `21` `24` |
| `balanced` | `01` `07` `10` `30` `40` `41` |
| `benford` | `05` `10` `15` `22` `38` `40` |
| `birthday` | `01` `04` `07` `10` `11` `12` |
| `cold` | `04` `11` `14` `17` `22` `43` |
| `contrarian` | `05` `16` `22` `24` `32` `42` |
| `delta` | `03` `06` `17` `18` `23` `32` |
| `highest-frequency` | `01` `04` `07` `10` `17` `22` |
| `hot` | `07` `08` `18` `28` `31` `43` |
| `llm-fewshot` | `05` `12` `23` `34` `41` `46` |
| `llm-tuned` | `03` `16` `17` `23` `26` `38` |
| `moonphase` | `11` `13` `20` `28` `34` `46` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `01` `04` `10` `18` `21` `29` |
| `random` | `09` `10` `19` `20` `30` `45` |
| `skiphit` | `01` `04` `06` `08` `26` `27` |
| `unpopular` | `22` `33` `38` `39` `42` `45` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `1` |
| `contrarian` | `3` `6` |
| `dreambook` | `9` `4` |
| `highest-frequency` | `0` `4` |
| `hot` | `8` `4` |
| `llm-fewshot` | `0` `5` |
| `llm-tuned` | `7` `6` |
| `moonphase` | `7` `6` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `1` `0` |
| `random` | `0` `3` |
| `skiphit` | `3` `4` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `2` |
| `contrarian` | `6` `5` |
| `dreambook` | `9` `8` |
| `highest-frequency` | `9` `1` |
| `hot` | `6` `8` |
| `llm-fewshot` | `4` `1` |
| `llm-tuned` | `6` `4` |
| `moonphase` | `9` `4` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `7` `2` |
| `random` | `0` `9` |
| `skiphit` | `9` `3` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `3` `4` |
| `contrarian` | `5` `2` `3` |
| `dreambook` | `6` `0` `3` |
| `highest-frequency` | `8` `4` `4` |
| `hot` | `7` `4` `8` |
| `llm-fewshot` | `4` `6` `0` |
| `llm-tuned` | `0` `0` `5` |
| `moonphase` | `6` `4` `4` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `2` `1` `5` |
| `random` | `1` `4` `7` |
| `skiphit` | `8` `3` `6` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `0` `5` |
| `contrarian` | `3` `8` `4` |
| `dreambook` | `0` `2` `4` |
| `highest-frequency` | `8` `1` `4` |
| `hot` | `6` `7` `9` |
| `llm-fewshot` | `1` `6` `7` |
| `llm-tuned` | `8` `8` `4` |
| `moonphase` | `8` `4` `6` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `7` `1` `1` |
| `random` | `2` `5` `4` |
| `skiphit` | `4` `3` `2` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `8` `0` `1` |
| `contrarian` | `2` `5` `7` `1` |
| `dreambook` | `9` `7` `5` `0` |
| `highest-frequency` | `5` `5` `7` `5` |
| `hot` | `4` `9` `7` `8` |
| `llm-fewshot` | `5` `6` `8` `7` |
| `llm-tuned` | `5` `5` `0` `6` |
| `moonphase` | `5` `2` `9` `4` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `6` `5` `3` `3` |
| `random` | `9` `4` `4` `5` |
| `skiphit` | `6` `5` `7` `3` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `4` `6` `3` |
| `contrarian` | `8` `2` `5` `4` |
| `dreambook` | `5` `3` `0` `5` |
| `highest-frequency` | `1` `4` `6` `5` |
| `hot` | `0` `8` `3` `1` |
| `llm-fewshot` | `9` `3` `6` `0` |
| `llm-tuned` | `1` `4` `3` `7` |
| `moonphase` | `1` `9` `5` `8` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `6` `0` `4` `2` |
| `random` | `1` `8` `2` `9` |
| `skiphit` | `7` `6` `0` `8` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `3` `6` `0` `2` |
| `contrarian` | `4` `2` `7` `2` `0` |
| `dreambook` | `8` `8` `3` `6` `1` |
| `highest-frequency` | `4` `1` `6` `5` `4` |
| `hot` | `8` `9` `6` `5` `0` |
| `llm-fewshot` | `3` `5` `9` `1` `3` |
| `llm-tuned` | `4` `7` `5` `6` `3` |
| `moonphase` | `3` `6` `3` `7` `6` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `9` `1` `4` `0` `7` |
| `random` | `3` `0` `2` `1` `0` |
| `skiphit` | `0` `3` `5` `7` `4` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `8` `7` `3` `0` |
| `contrarian` | `6` `6` `1` `1` `8` |
| `dreambook` | `0` `0` `2` `6` `1` |
| `highest-frequency` | `2` `1` `1` `6` `4` |
| `hot` | `2` `8` `5` `4` `6` |
| `llm-fewshot` | `0` `5` `7` `3` `3` |
| `llm-tuned` | `3` `1` `3` `6` `2` |
| `moonphase` | `2` `1` `3` `6` `0` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `1` `7` `1` `5` `9` |
| `random` | `8` `0` `5` `9` `4` |
| `skiphit` | `5` `3` `6` `3` `2` |

<sub>Updated 2026-08-21 11:00 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**999** predictions scored across **27** days. Combined, they've hit **394** numbers where pure chance predicts **352.8** (z = **+2.32**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 77 | 42 | 27.1 | 0.55/draw | +3.01 | 2 (Mega Millions) |
| `contrarian` | 44 | 25 | 15.5 | 0.57/draw | +2.56 | 2 (NY Numbers (Pick 3)) |
| `benford` | 8 | 6 | 2.9 | 0.75/draw | +1.96 | 3 (Mega Millions) |
| `birthday` | 8 | 5 | 2.9 | 0.62/draw | +1.33 | 2 (Powerball) |
| `skiphit` | 44 | 20 | 15.5 | 0.45/draw | +1.21 | 2 (NY Win 4) |
| `persistent` | 44 | 20 | 15.5 | 0.45/draw | +1.21 | 2 (NY Numbers (Pick 3)) |
| `numerology` | 44 | 20 | 15.5 | 0.45/draw | +1.21 | 2 (NY Numbers (Pick 3)) |
| `positional` | 93 | 39 | 32.7 | 0.42/draw | +1.16 | 2 (NY Win 4) |
| `llm-tuned` | 59 | 25 | 20.8 | 0.42/draw | +0.96 | 3 (NY Win 4) |
| `random` | 113 | 44 | 39.9 | 0.39/draw | +0.69 | 2 (Mega Millions) |
| `hot` | 113 | 42 | 39.9 | 0.37/draw | +0.35 | 3 (NY Numbers (Pick 3)) |
| `delta` | 20 | 8 | 7.2 | 0.40/draw | +0.32 | 1 (Powerball) |
| `balanced` | 8 | 3 | 2.9 | 0.38/draw | +0.07 | 2 (Mega Millions) |
| `moonphase` | 44 | 14 | 15.5 | 0.32/draw | -0.40 | 2 (NY Win 4) |
| `dreambook` | 36 | 11 | 12.6 | 0.31/draw | -0.48 | 2 (NY Numbers (Pick 3)) |
| `antibalanced` | 8 | 2 | 2.9 | 0.25/draw | -0.56 | 1 (Powerball) |
| `cold` | 113 | 35 | 39.9 | 0.31/draw | -0.82 | 3 (NY Win 4) |
| `unpopular` | 20 | 4 | 7.2 | 0.20/draw | -1.28 | 2 (Mega Millions) |
| `llm-fewshot` | 103 | 29 | 36.4 | 0.28/draw | -1.29 | 2 (NY Win 4) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-21 11:00 UTC</sub>
<!-- SCOREBOARD:END -->

## The honest part

Lottery draws are independent uniform samples. Well-run lotteries pass every
randomness test, and no peer-reviewed work has ever demonstrated above-chance
draw prediction — the documented "wins" (Selbee, MIT/Cash WinFall, Mandel)
exploited *payout structure*, never draw prediction. So the null hypothesis —
**no strategy beats chance** — is almost certainly true, and this project is the
instrument that demonstrates it with real data. Watching every arm converge to
z ≈ 0 *is* the product. The one exception with defensible math is the
`unpopular` strategy: it can't improve match odds, but avoiding human-popular
numbers raises expected payout *conditional on winning*.

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/RESEARCH.md](docs/RESEARCH.md) for the research behind the design
(data sources, strategy literature, null-hypothesis math, fine-tuning options).

## Strategies

| Arm | Idea | Expected result |
|---|---|---|
| `random` | uniform sample — defines chance | the baseline |
| `hot` | most frequent numbers, trailing window | chance |
| `cold` | most overdue numbers (gambler's-fallacy control) | chance |
| `delta` | sample empirical gaps between sorted winners | chance |
| `positional` | per-position digit frequency (Pick 3/Win 4) | chance |
| `unpopular` | avoid birthday/sequence combos to reduce jackpot splitting | same matches, better EV-if-win |
| `llm-fewshot` | LLM (Ollama Cloud by default) with recent-draw context, no training | chance |
| `llm-tuned` | LoRA-tuned on accumulated history (Fireworks, retrained monthly; or local MLX) | chance (measured rigorously) |
| `highest-frequency` | consensus: ranks numbers by how many *other arms* picked them for that same drawing | chance |

## Quickstart

```bash
pip install -e ".[llm,dev]"

lottery-guru pull --limit 2000   # backfill history
lottery-guru predict             # today's predictions
lottery-guru score               # score anything whose results are in
lottery-guru report              # regenerate REPORT.md
```

`lottery-guru daily` runs all four — it's the GitHub Actions cron entry point
(`.github/workflows/daily.yml`, 10:15 UTC daily, after NY Open Data's nightly
batch). Predictions and scores are committed to the repo: git is the database.

### LLM arm

Provider-pluggable, auto-detected from credentials:

- **Ollama Cloud** (default, cheap/free tier): create a key at
  [ollama.com/settings/keys](https://ollama.com/settings/keys) and set
  `OLLAMA_API_KEY` (as a repo secret for CI). Default model `gpt-oss:20b`;
  override with `LOTTERY_GURU_LLM_MODEL`.
- **Local Ollama**: set `OLLAMA_HOST=http://localhost:11434` — no key needed.
  A fused MLX fine-tune can be imported into Ollama and served the same way.
- **Anthropic**: set `ANTHROPIC_API_KEY` and
  `LOTTERY_GURU_LLM_PROVIDER=anthropic` (needs `pip install -e ".[llm]"`).
- **Fireworks.ai**: set `FIREWORKS_API_KEY` — also unlocks the `llm-tuned` arm
  once a monthly fine-tune has run (see below).

Without any of these, the LLM arm is skipped cleanly — everything else runs
with zero keys.

## Fine-tuning (local, Apple Silicon)

```bash
pip install mlx-lm

lottery-guru finetune export     # build time-ordered train/valid/test JSONL
lottery-guru finetune train      # QLoRA on Qwen3-4B-4bit → adapters/<date>/
lottery-guru finetune eval --adapter adapters/<date>   # base vs tuned, held-out future window
```

Splits are strictly time-ordered (train past → test future). Recommended
cadence: monthly, once ≥60 scored days exist.

## Usage & cost log

`lottery-guru usage` appends to `data/usage/fireworks.jsonl` (committed daily
by the loop), from two sources:

- **`billingUsage`** — Fireworks' metered quantities (accelerator-seconds,
  tokens). Note it reports *quantities, not dollars*: rated dollar totals are
  behind `GetBillingSummary`, which is CLI-only today, so the log deliberately
  records no dollar figure rather than guessing one from assumed rates.
- **Deployment lifetimes** — measured locally at teardown. A dedicated GPU
  bills for as long as it exists, so this is the dominant cost driver and it
  lands the same day instead of waiting for billing to catch up. A failed
  teardown is logged as `deployment_teardown_failed` — a cost risk you can
  grep for — and a deployment that never came up as `deployment_failed`,
  carrying whatever reason Fireworks gave. Both count toward
  `logged_failures`.

`lottery-guru usage --summary-only` totals the committed log without calling
the API.

## Fine-tuning (hosted, automated)

The hosted path uses Fireworks.ai LoRA and runs on two schedules:

- **Monthly retrain** — [`monthly-finetune.yml`](.github/workflows/monthly-finetune.yml),
  1st of each month, once ≥60 scored days exist (before that it skips
  cleanly). Exports the dataset, trains, and commits the tuned model name to
  `data/finetune/fireworks.json`. Manual dispatch takes a `force` input that
  bypasses the gate and a `max_per_game` input for full-history exports.
- **Tuned predictions** — the [daily loop](.github/workflows/daily.yml) brings
  the tuned model up, predicts alongside every other arm, and tears it back
  down, so `llm-tuned` is scored against the same null as everything else.
  It does this only on days a jackpot game draws (Mon/Tue/Wed/Fri/Sat) —
  Sundays and Thursdays are NY-only, so the GPU stays off and the week costs
  five sessions instead of seven. Every other arm still predicts all seven
  days; only the paid arm is trimmed.

Setup: add the repo secret `FIREWORKS_API_KEY`
([fireworks.ai/settings/users/api-keys](https://app.fireworks.ai/settings/users/api-keys));
the account slug is auto-resolved from the key (set `FIREWORKS_ACCOUNT_ID` to
override). Training needs a Tier 2 account (add $50 in credits) for GPU quota.

**Serving costs GPU time.** Fireworks does not serve LoRA fine-tunes
serverlessly — inference needs an on-demand deployment billed while it exists,
so the daily loop keeps one alive only for the few minutes it takes to
predict. Teardown runs even when the loop fails or is cancelled, and also
sweeps any orphaned `lottery-guru` deployment it finds, because a leaked one
bills indefinitely. Check [the dashboard](https://app.fireworks.ai/dashboard/deployments)
if a run ever ends without a clean teardown; `lottery-guru finetune teardown`
removes anything left over. `LOTTERY_GURU_FT_ACCELERATOR` pins a cheaper GPU
class when your account has quota for one.

Bring-up is not guaranteed: a GPU class that is out of capacity often accepts
the request and only fails minutes later. Deployment tries each accelerator
candidate through to `READY`, deletes one that dies, and moves to the next,
all inside a single 30-minute budget so the daily loop stays bounded. If every
candidate fails, the day simply has no `llm-tuned` prediction — the arm is
best-effort and never blocks the rest of the loop.

Run locally with:

```bash
lottery-guru finetune export --max-per-game 100000   # full current-era history
FIREWORKS_API_KEY=... lottery-guru finetune train --provider fireworks
FIREWORKS_API_KEY=... lottery-guru finetune deploy   # then predict, then:
FIREWORKS_API_KEY=... lottery-guru finetune teardown # ALWAYS, to stop billing
```

## Data sources

- **NY Open Data (Socrata)** — official, free, no auth; nightly refresh.
  Powerball `d6yy-54nr`, Mega Millions `5xaw-6ayf`, Numbers/Win4 `hsys-3def`.
- **Texas Lottery CSVs** — used as an integrity cross-check for Powerball.

## Disclaimer

This is a statistics/ML measurement project, not gambling advice. Expected
value of every lottery ticket is strongly negative; nothing here changes that.
