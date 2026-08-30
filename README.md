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
### 🎟️ Predictions for 2026-08-30

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `0` `7` |
| `contrarian` | `6` `4` `3` |
| `dreambook` | `0` `4` `3` |
| `highest-frequency` | `1` `4` `3` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `3` `6` `4` |
| `moonphase` | `1` `4` `5` |
| `numerology` | `1` `1` `5` |
| `persistent` | `4` `3` `3` |
| `positional` | `4` `4` `0` |
| `random` | `6` `7` `3` |
| `skiphit` | `8` `5` `9` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `0` `7` |
| `contrarian` | `8` `4` `9` |
| `dreambook` | `4` `7` `3` |
| `highest-frequency` | `8` `9` `3` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `8` `0` `1` |
| `moonphase` | `2` `9` `2` |
| `numerology` | `1` `1` `5` |
| `persistent` | `4` `3` `3` |
| `positional` | `4` `9` `8` |
| `random` | `1` `8` `8` |
| `skiphit` | `8` `5` `9` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `4` `8` `1` |
| `contrarian` | `8` `2` `5` `9` |
| `dreambook` | `5` `9` `5` `8` |
| `highest-frequency` | `5` `5` `5` `5` |
| `hot` | `9` `8` `3` `5` |
| `llm-fewshot` | `8` `8` `3` `6` |
| `moonphase` | `5` `7` `4` `4` |
| `numerology` | `1` `1` `5` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `2` `0` `4` `0` |
| `random` | `5` `5` `5` `3` |
| `skiphit` | `6` `5` `5` `7` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `4` `8` `1` |
| `contrarian` | `8` `5` `9` `9` |
| `dreambook` | `7` `5` `2` `8` |
| `highest-frequency` | `8` `5` `3` `5` |
| `hot` | `9` `8` `3` `5` |
| `llm-fewshot` | `9` `5` `5` `0` |
| `moonphase` | `8` `4` `7` `7` |
| `numerology` | `1` `1` `5` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `3` `6` `7` `5` |
| `random` | `5` `1` `6` `2` |
| `skiphit` | `6` `5` `3` `7` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `02` `04` `15` `16` `21` |
| `balanced` | `01` `05` `20` `25` `26` |
| `benford` | `01` `03` `04` `18` `26` |
| `birthday` | `06` `08` `09` `16` `21` |
| `cold` | `01` `16` `22` `28` `29` |
| `contrarian` | `01` `03` `10` `12` `33` |
| `delta` | `07` `19` `23` `30` `31` |
| `highest-frequency` | `01` `20` `22` `29` `36` |
| `hot` | `03` `09` `20` `29` `36` |
| `llm-fewshot` | `11` `15` `18` `22` `27` |
| `moonphase` | `06` `07` `11` `20` `23` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `13` `23` `29` `32` `36` |
| `skiphit` | `08` `09` `18` `28` `31` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `07` `08` `11` `12` `18` |
| `balanced` | `01` `16` `19` `22` `25` |
| `benford` | `03` `04` `10` `16` `29` |
| `birthday` | `03` `07` `10` `20` `24` |
| `cold` | `04` `08` `12` `17` `30` |
| `contrarian` | `13` `19` `24` `27` `35` |
| `delta` | `04` `09` `21` `23` `29` |
| `highest-frequency` | `04` `08` `10` `12` `24` |
| `hot` | `16` `21` `23` `27` `32` |
| `llm-fewshot` | `04` `23` `24` `33` `36` |
| `moonphase` | `01` `02` `08` `11` `13` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `01` `02` `07` `17` `22` |
| `skiphit` | `08` `12` `14` `31` `34` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `5` |
| `contrarian` | `3` `9` |
| `dreambook` | `0` `4` |
| `highest-frequency` | `7` `0` |
| `hot` | `6` `0` |
| `llm-fewshot` | `5` `7` |
| `moonphase` | `2` `0` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `9` `0` |
| `random` | `7` `1` |
| `skiphit` | `2` `4` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `0` |
| `contrarian` | `9` `8` |
| `dreambook` | `2` `4` |
| `highest-frequency` | `7` `4` |
| `hot` | `5` `7` |
| `llm-fewshot` | `0` `5` |
| `moonphase` | `7` `5` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `6` `9` |
| `random` | `0` `2` |
| `skiphit` | `7` `4` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `4` `2` |
| `contrarian` | `1` `1` `8` |
| `dreambook` | `2` `4` `4` |
| `highest-frequency` | `1` `4` `4` |
| `hot` | `1` `6` `0` |
| `llm-fewshot` | `3` `7` `9` |
| `moonphase` | `1` `9` `9` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `2` `4` `7` |
| `random` | `8` `5` `1` |
| `skiphit` | `5` `3` `6` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `8` `2` |
| `contrarian` | `2` `9` `1` |
| `dreambook` | `5` `7` `8` |
| `highest-frequency` | `5` `7` `8` |
| `hot` | `1` `2` `8` |
| `llm-fewshot` | `7` `5` `4` |
| `moonphase` | `5` `3` `9` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `7` `4` `3` |
| `random` | `4` `7` `5` |
| `skiphit` | `0` `2` `3` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `5` `0` `8` |
| `contrarian` | `3` `6` `6` `0` |
| `dreambook` | `9` `4` `0` `1` |
| `highest-frequency` | `3` `6` `6` `5` |
| `hot` | `0` `9` `2` `4` |
| `llm-fewshot` | `3` `1` `1` `2` |
| `moonphase` | `3` `6` `0` `2` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `0` `9` `6` `5` |
| `random` | `0` `0` `6` `8` |
| `skiphit` | `7` `6` `4` `0` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `0` `8` `9` |
| `contrarian` | `9` `6` `4` `6` |
| `dreambook` | `9` `7` `5` `0` |
| `highest-frequency` | `2` `4` `1` `0` |
| `hot` | `9` `1` `2` `0` |
| `llm-fewshot` | `7` `4` `1` `2` |
| `moonphase` | `2` `8` `7` `4` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `5` `7` `5` `3` |
| `random` | `7` `5` `1` `0` |
| `skiphit` | `8` `2` `7` `1` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `0` `4` `1` `6` |
| `contrarian` | `9` `3` `8` `1` `3` |
| `dreambook` | `3` `1` `6` `1` `9` |
| `highest-frequency` | `1` `1` `1` `1` `6` |
| `hot` | `7` `5` `3` `2` `1` |
| `llm-fewshot` | `8` `4` `4` `8` `6` |
| `moonphase` | `6` `7` `2` `6` `8` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `1` `6` `1` `3` `6` |
| `random` | `4` `5` `5` `7` `0` |
| `skiphit` | `5` `2` `1` `6` `9` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `7` `9` `2` `6` |
| `contrarian` | `7` `9` `6` `0` `3` |
| `dreambook` | `6` `4` `5` `5` `1` |
| `highest-frequency` | `1` `1` `5` `4` `1` |
| `hot` | `4` `8` `7` `6` `5` |
| `llm-fewshot` | `1` `2` `5` `2` `2` |
| `moonphase` | `1` `1` `5` `4` `6` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `4` `1` `2` `7` `1` |
| `random` | `6` `5` `0` `4` `2` |
| `skiphit` | `8` `6` `1` `9` `1` |

<sub>Updated 2026-08-30 15:02 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**1527** predictions scored across **36** days. Combined, they've hit **569** numbers where pure chance predicts **539.3** (z = **+1.35**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `contrarian` | 84 | 43 | 29.6 | 0.51/draw | +2.60 | 2 (NY Numbers (Pick 3)) |
| `highest-frequency` | 117 | 53 | 41.3 | 0.45/draw | +1.93 | 2 (Mega Millions) |
| `benford` | 15 | 9 | 5.4 | 0.60/draw | +1.66 | 3 (Mega Millions) |
| `random` | 153 | 65 | 54.0 | 0.42/draw | +1.58 | 2 (Mega Millions) |
| `positional` | 126 | 50 | 44.3 | 0.40/draw | +0.90 | 2 (NY Win 4) |
| `skiphit` | 84 | 34 | 29.6 | 0.40/draw | +0.85 | 2 (NY Win 4) |
| `birthday` | 15 | 7 | 5.4 | 0.47/draw | +0.73 | 2 (Powerball) |
| `hot` | 153 | 59 | 54.0 | 0.39/draw | +0.72 | 3 (NY Numbers (Pick 3)) |
| `persistent` | 84 | 32 | 29.6 | 0.38/draw | +0.47 | 2 (NY Numbers (Pick 3)) |
| `numerology` | 84 | 31 | 29.6 | 0.37/draw | +0.27 | 2 (NY Numbers (Pick 3)) |
| `llm-tuned` | 79 | 27 | 27.9 | 0.34/draw | -0.18 | 3 (NY Win 4) |
| `antibalanced` | 15 | 5 | 5.4 | 0.33/draw | -0.19 | 1 (Powerball) |
| `unpopular` | 27 | 9 | 9.7 | 0.33/draw | -0.25 | 2 (Mega Millions) |
| `moonphase` | 84 | 27 | 29.6 | 0.32/draw | -0.51 | 2 (NY Win 4) |
| `delta` | 27 | 8 | 9.7 | 0.30/draw | -0.59 | 1 (Powerball) |
| `balanced` | 15 | 4 | 5.4 | 0.27/draw | -0.65 | 2 (Mega Millions) |
| `llm-fewshot` | 143 | 43 | 50.5 | 0.30/draw | -1.12 | 3 (NY Win 4) |
| `cold` | 153 | 45 | 54.0 | 0.29/draw | -1.30 | 3 (NY Win 4) |
| `dreambook` | 69 | 18 | 24.2 | 0.26/draw | -1.33 | 2 (NY Numbers (Pick 3)) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-30 15:02 UTC</sub>
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
