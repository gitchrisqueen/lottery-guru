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
### 🎟️ Predictions for 2026-08-23

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `3` `0` |
| `contrarian` | `9` `7` `8` |
| `dreambook` | `1` `9` `1` |
| `highest-frequency` | `1` `9` `2` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `2` `9` `5` |
| `moonphase` | `8` `4` `2` |
| `numerology` | `1` `1` `7` |
| `persistent` | `4` `3` `3` |
| `positional` | `2` `9` `2` |
| `random` | `3` `1` `2` |
| `skiphit` | `5` `5` `8` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `3` `0` |
| `contrarian` | `5` `5` `8` |
| `dreambook` | `1` `3` `3` |
| `highest-frequency` | `5` `3` `2` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `1` `1` `1` |
| `moonphase` | `2` `4` `2` |
| `numerology` | `1` `1` `7` |
| `persistent` | `4` `3` `3` |
| `positional` | `3` `8` `4` |
| `random` | `3` `9` `5` |
| `skiphit` | `5` `5` `8` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `6` `1` `4` |
| `contrarian` | `8` `8` `5` `0` |
| `dreambook` | `9` `8` `0` `0` |
| `highest-frequency` | `8` `8` `7` `9` |
| `hot` | `8` `5` `3` `9` |
| `llm-fewshot` | `9` `3` `7` `2` |
| `moonphase` | `4` `3` `3` `9` |
| `numerology` | `1` `1` `7` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `5` `8` `8` `6` |
| `random` | `2` `6` `0` `1` |
| `skiphit` | `8` `8` `5` `7` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `6` `1` `4` |
| `contrarian` | `9` `5` `5` `0` |
| `dreambook` | `5` `0` `2` `4` |
| `highest-frequency` | `2` `6` `5` `4` |
| `hot` | `8` `3` `5` `9` |
| `llm-fewshot` | `9` `0` `3` `2` |
| `moonphase` | `0` `2` `7` `4` |
| `numerology` | `1` `1` `7` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `2` `3` `3` `8` |
| `random` | `1` `6` `2` `1` |
| `skiphit` | `8` `8` `5` `7` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `08` `23` `31` `33` `34` |
| `balanced` | `04` `07` `29` `33` `34` |
| `benford` | `03` `04` `10` `19` `21` |
| `birthday` | `05` `06` `13` `17` `26` |
| `cold` | `07` `13` `23` `29` `32` |
| `contrarian` | `09` `17` `28` `30` `36` |
| `delta` | `04` `09` `10` `13` `24` |
| `highest-frequency` | `07` `10` `21` `29` `34` |
| `hot` | `11` `19` `21` `24` `34` |
| `llm-fewshot` | `10` `12` `21` `28` `34` |
| `moonphase` | `01` `07` `16` `21` `23` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `08` `11` `19` `23` `29` |
| `skiphit` | `01` `07` `08` `14` `21` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `17` `18` `30` `31` `35` |
| `balanced` | `05` `06` `21` `26` `35` |
| `benford` | `05` `11` `15` `27` `30` |
| `birthday` | `06` `08` `11` `29` `31` |
| `cold` | `05` `08` `19` `28` `36` |
| `contrarian` | `12` `15` `18` `28` `30` |
| `delta` | `10` `14` `25` `29` `35` |
| `highest-frequency` | `06` `19` `22` `28` `29` |
| `hot` | `01` `02` `19` `27` `33` |
| `llm-fewshot` | `06` `08` `13` `17` `22` |
| `moonphase` | `06` `19` `20` `28` `33` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `10` `12` `19` `22` `29` |
| `skiphit` | `03` `07` `22` `28` `36` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `0` |
| `contrarian` | `9` `3` |
| `dreambook` | `5` `0` |
| `highest-frequency` | `1` `1` |
| `hot` | `0` `2` |
| `llm-fewshot` | `1` `2` |
| `moonphase` | `9` `8` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `8` `5` |
| `random` | `5` `1` |
| `skiphit` | `1` `6` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `8` |
| `contrarian` | `8` `5` |
| `dreambook` | `7` `2` |
| `highest-frequency` | `0` `6` |
| `hot` | `5` `6` |
| `llm-fewshot` | `0` `0` |
| `moonphase` | `3` `2` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `0` `6` |
| `random` | `2` `4` |
| `skiphit` | `7` `8` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `0` `4` |
| `contrarian` | `8` `8` `1` |
| `dreambook` | `0` `6` `2` |
| `highest-frequency` | `2` `6` `1` |
| `hot` | `3` `0` `1` |
| `llm-fewshot` | `9` `1` `9` |
| `moonphase` | `5` `8` `5` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `2` `6` `5` |
| `random` | `7` `3` `3` |
| `skiphit` | `2` `9` `8` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `9` `4` |
| `contrarian` | `7` `5` `5` |
| `dreambook` | `4` `6` `8` |
| `highest-frequency` | `4` `5` `4` |
| `hot` | `4` `2` `9` |
| `llm-fewshot` | `4` `1` `3` |
| `moonphase` | `1` `5` `9` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `7` `4` `2` |
| `random` | `5` `0` `8` |
| `skiphit` | `5` `0` `0` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `0` `1` `5` |
| `contrarian` | `0` `3` `7` `6` |
| `dreambook` | `4` `5` `2` `3` |
| `highest-frequency` | `1` `5` `6` `5` |
| `hot` | `9` `3` `0` `4` |
| `llm-fewshot` | `1` `5` `3` `9` |
| `moonphase` | `1` `0` `8` `6` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `9` `5` `6` `8` |
| `random` | `2` `9` `5` `7` |
| `skiphit` | `3` `2` `5` `1` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `0` `1` `7` |
| `contrarian` | `1` `4` `2` `0` |
| `dreambook` | `8` `4` `1` `0` |
| `highest-frequency` | `5` `4` `1` `7` |
| `hot` | `3` `7` `2` `1` |
| `llm-fewshot` | `5` `8` `0` `7` |
| `moonphase` | `5` `6` `5` `1` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `9` `9` `4` `6` |
| `random` | `5` `7` `5` `4` |
| `skiphit` | `7` `9` `0` `2` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `2` `9` `1` `0` |
| `contrarian` | `9` `5` `0` `3` `2` |
| `dreambook` | `9` `6` `6` `7` `5` |
| `highest-frequency` | `4` `2` `6` `5` `4` |
| `hot` | `2` `8` `6` `1` `9` |
| `llm-fewshot` | `4` `0` `9` `9` `8` |
| `moonphase` | `4` `2` `1` `1` `4` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `4` `6` `3` `5` `2` |
| `random` | `9` `8` `5` `6` `6` |
| `skiphit` | `1` `2` `8` `5` `2` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `4` `5` `0` `2` |
| `contrarian` | `6` `7` `2` `0` `0` |
| `dreambook` | `7` `2` `3` `1` `9` |
| `highest-frequency` | `1` `2` `1` `0` `4` |
| `hot` | `5` `9` `1` `8` `2` |
| `llm-fewshot` | `2` `9` `1` `3` `4` |
| `moonphase` | `0` `0` `0` `1` `4` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `1` `2` `7` `3` `9` |
| `random` | `7` `6` `6` `4` `3` |
| `skiphit` | `6` `3` `7` `7` `0` |

<sub>Updated 2026-08-23 11:31 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**1137** predictions scored across **29** days. Combined, they've hit **437** numbers where pure chance predicts **401.4** (z = **+1.88**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 87 | 45 | 30.7 | 0.52/draw | +2.74 | 2 (Mega Millions) |
| `contrarian` | 54 | 30 | 19.0 | 0.56/draw | +2.67 | 2 (NY Numbers (Pick 3)) |
| `benford` | 10 | 7 | 3.6 | 0.70/draw | +1.92 | 3 (Mega Millions) |
| `birthday` | 10 | 6 | 3.6 | 0.60/draw | +1.35 | 2 (Powerball) |
| `positional` | 101 | 43 | 35.5 | 0.43/draw | +1.33 | 2 (NY Win 4) |
| `skiphit` | 54 | 24 | 19.0 | 0.44/draw | +1.21 | 2 (NY Win 4) |
| `persistent` | 54 | 24 | 19.0 | 0.44/draw | +1.21 | 2 (NY Numbers (Pick 3)) |
| `random` | 123 | 50 | 43.4 | 0.41/draw | +1.05 | 2 (Mega Millions) |
| `numerology` | 54 | 22 | 19.0 | 0.41/draw | +0.73 | 2 (NY Numbers (Pick 3)) |
| `hot` | 123 | 47 | 43.4 | 0.38/draw | +0.57 | 3 (NY Numbers (Pick 3)) |
| `llm-tuned` | 69 | 25 | 24.4 | 0.36/draw | +0.14 | 3 (NY Win 4) |
| `delta` | 22 | 8 | 7.9 | 0.36/draw | +0.03 | 1 (Powerball) |
| `balanced` | 10 | 3 | 3.6 | 0.30/draw | -0.34 | 2 (Mega Millions) |
| `antibalanced` | 10 | 3 | 3.6 | 0.30/draw | -0.34 | 1 (Powerball) |
| `cold` | 123 | 38 | 43.4 | 0.31/draw | -0.87 | 3 (NY Win 4) |
| `dreambook` | 44 | 12 | 15.4 | 0.27/draw | -0.91 | 2 (NY Numbers (Pick 3)) |
| `moonphase` | 54 | 15 | 19.0 | 0.28/draw | -0.97 | 2 (NY Win 4) |
| `unpopular` | 22 | 5 | 7.9 | 0.23/draw | -1.11 | 2 (Mega Millions) |
| `llm-fewshot` | 113 | 30 | 39.9 | 0.27/draw | -1.66 | 2 (NY Win 4) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-23 11:31 UTC</sub>
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
