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
### 🎟️ Predictions for 2026-08-27

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `5` `1` |
| `contrarian` | `8` `6` `2` |
| `dreambook` | `4` `9` `9` |
| `highest-frequency` | `8` `5` `9` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `1` `3` `9` |
| `moonphase` | `8` `8` `0` |
| `numerology` | `1` `1` `1` |
| `persistent` | `4` `3` `3` |
| `positional` | `6` `7` `9` |
| `random` | `6` `5` `3` |
| `skiphit` | `9` `0` `7` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `5` `1` |
| `contrarian` | `9` `6` `3` |
| `dreambook` | `6` `2` `9` |
| `highest-frequency` | `1` `5` `1` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `1` `5` `7` |
| `moonphase` | `6` `4` `1` |
| `numerology` | `1` `1` `1` |
| `persistent` | `4` `3` `3` |
| `positional` | `1` `3` `2` |
| `random` | `5` `7` `6` |
| `skiphit` | `9` `0` `7` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `2` `4` `1` |
| `contrarian` | `4` `7` `0` `0` |
| `dreambook` | `2` `3` `4` `4` |
| `highest-frequency` | `2` `4` `4` `5` |
| `hot` | `8` `9` `3` `5` |
| `llm-fewshot` | `2` `4` `4` `2` |
| `moonphase` | `9` `4` `9` `1` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `6` `5` `4` `6` |
| `random` | `5` `6` `7` `8` |
| `skiphit` | `3` `7` `0` `5` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `2` `1` `4` |
| `contrarian` | `3` `7` `6` `1` |
| `dreambook` | `9` `4` `1` `6` |
| `highest-frequency` | `8` `9` `1` `5` |
| `hot` | `8` `9` `3` `5` |
| `llm-fewshot` | `9` `1` `8` `8` |
| `moonphase` | `8` `9` `1` `3` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `3` `4` `8` `8` |
| `random` | `1` `2` `0` `2` |
| `skiphit` | `3` `7` `0` `5` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `03` `09` `14` `17` |
| `balanced` | `01` `08` `12` `29` `36` |
| `benford` | `04` `10` `13` `26` `32` |
| `birthday` | `03` `06` `07` `10` `16` |
| `cold` | `15` `21` `22` `33` `35` |
| `contrarian` | `13` `19` `24` `28` `30` |
| `delta` | `10` `12` `13` `19` `29` |
| `highest-frequency` | `10` `12` `13` `14` `36` |
| `hot` | `08` `13` `14` `24` `36` |
| `llm-fewshot` | `05` `08` `14` `24` `35` |
| `moonphase` | `02` `18` `22` `25` `36` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `01` `09` `12` `16` `33` |
| `skiphit` | `10` `13` `18` `26` `33` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `07` `26` `32` `34` `35` |
| `balanced` | `10` `17` `19` `27` `30` |
| `benford` | `04` `14` `15` `24` `32` |
| `birthday` | `01` `03` `09` `12` `18` |
| `cold` | `04` `07` `10` `14` `23` |
| `contrarian` | `14` `15` `18` `30` `33` |
| `delta` | `08` `13` `21` `30` `33` |
| `highest-frequency` | `04` `07` `09` `14` `22` |
| `hot` | `11` `13` `16` `19` `29` |
| `llm-fewshot` | `06` `07` `09` `14` `24` |
| `moonphase` | `01` `04` `08` `21` `25` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `06` `09` `22` `34` `36` |
| `skiphit` | `04` `07` `14` `22` `26` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `9` |
| `contrarian` | `9` `3` |
| `dreambook` | `9` `8` |
| `highest-frequency` | `0` `8` |
| `hot` | `0` `5` |
| `llm-fewshot` | `8` `9` |
| `moonphase` | `0` `0` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `9` `5` |
| `random` | `0` `8` |
| `skiphit` | `7` `2` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `0` |
| `contrarian` | `9` `6` |
| `dreambook` | `4` `6` |
| `highest-frequency` | `4` `1` |
| `hot` | `5` `3` |
| `llm-fewshot` | `8` `3` |
| `moonphase` | `3` `4` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `6` `9` |
| `random` | `4` `2` |
| `skiphit` | `4` `1` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `3` `9` |
| `contrarian` | `7` `7` `3` |
| `dreambook` | `9` `2` `7` |
| `highest-frequency` | `8` `8` `9` |
| `hot` | `9` `4` `7` |
| `llm-fewshot` | `3` `3` `5` |
| `moonphase` | `2` `8` `1` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `4` `1` `9` |
| `random` | `4` `9` `6` |
| `skiphit` | `8` `8` `5` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `9` `7` |
| `contrarian` | `4` `6` `9` |
| `dreambook` | `9` `8` `6` |
| `highest-frequency` | `9` `3` `9` |
| `hot` | `0` `3` `9` |
| `llm-fewshot` | `3` `3` `3` |
| `moonphase` | `9` `2` `3` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `5` `2` `7` |
| `random` | `9` `7` `6` |
| `skiphit` | `0` `3` `1` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `8` `1` `7` |
| `contrarian` | `6` `9` `7` `1` |
| `dreambook` | `7` `2` `3` `1` |
| `highest-frequency` | `6` `2` `1` `5` |
| `hot` | `2` `9` `8` `0` |
| `llm-fewshot` | `9` `5` `7` `7` |
| `moonphase` | `6` `2` `3` `8` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `3` `0` `4` `8` |
| `random` | `1` `4` `0` `8` |
| `skiphit` | `5` `6` `4` `5` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `1` `7` `0` |
| `contrarian` | `7` `2` `3` `6` |
| `dreambook` | `8` `4` `9` `4` |
| `highest-frequency` | `8` `1` `9` `4` |
| `hot` | `8` `0` `3` `9` |
| `llm-fewshot` | `4` `3` `3` `9` |
| `moonphase` | `6` `1` `4` `2` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `3` `7` `9` `1` |
| `random` | `5` `1` `9` `4` |
| `skiphit` | `7` `9` `4` `4` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `8` `4` `1` `9` |
| `contrarian` | `0` `9` `0` `5` `0` |
| `dreambook` | `3` `6` `8` `9` `8` |
| `highest-frequency` | `0` `6` `6` `5` `8` |
| `hot` | `0` `4` `8` `6` `2` |
| `llm-fewshot` | `8` `4` `7` `5` `4` |
| `moonphase` | `8` `6` `7` `5` `6` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `2` `8` `6` `0` `6` |
| `random` | `9` `7` `3` `4` `8` |
| `skiphit` | `0` `9` `0` `1` `8` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `7` `6` `3` `0` |
| `contrarian` | `6` `4` `7` `0` `7` |
| `dreambook` | `4` `9` `4` `9` `0` |
| `highest-frequency` | `1` `1` `3` `9` `0` |
| `hot` | `7` `5` `3` `9` `4` |
| `llm-fewshot` | `2` `6` `5` `9` `0` |
| `moonphase` | `9` `4` `3` `6` `1` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `8` `1` `3` `9` `5` |
| `random` | `9` `4` `2` `0` `7` |
| `skiphit` | `1` `1` `8` `8` `7` |

<sub>Updated 2026-08-27 20:38 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**1358** predictions scored across **33** days. Combined, they've hit **509** numbers where pure chance predicts **479.3** (z = **+1.44**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `contrarian` | 71 | 37 | 25.0 | 0.52/draw | +2.54 | 2 (NY Numbers (Pick 3)) |
| `highest-frequency` | 104 | 47 | 36.6 | 0.45/draw | +1.81 | 2 (Mega Millions) |
| `benford` | 13 | 8 | 4.7 | 0.62/draw | +1.64 | 3 (Mega Millions) |
| `positional` | 115 | 49 | 40.4 | 0.43/draw | +1.43 | 2 (NY Win 4) |
| `random` | 140 | 58 | 49.4 | 0.41/draw | +1.29 | 2 (Mega Millions) |
| `birthday` | 13 | 7 | 4.7 | 0.54/draw | +1.14 | 2 (Powerball) |
| `persistent` | 71 | 30 | 25.0 | 0.42/draw | +1.06 | 2 (NY Numbers (Pick 3)) |
| `skiphit` | 71 | 28 | 25.0 | 0.39/draw | +0.64 | 2 (NY Win 4) |
| `hot` | 140 | 52 | 49.4 | 0.37/draw | +0.39 | 3 (NY Numbers (Pick 3)) |
| `numerology` | 71 | 26 | 25.0 | 0.37/draw | +0.21 | 2 (NY Numbers (Pick 3)) |
| `llm-tuned` | 74 | 26 | 26.1 | 0.35/draw | -0.03 | 3 (NY Win 4) |
| `balanced` | 13 | 4 | 4.7 | 0.31/draw | -0.34 | 2 (Mega Millions) |
| `delta` | 25 | 8 | 9.0 | 0.32/draw | -0.36 | 1 (Powerball) |
| `moonphase` | 71 | 22 | 25.0 | 0.31/draw | -0.63 | 2 (NY Win 4) |
| `antibalanced` | 13 | 3 | 4.7 | 0.23/draw | -0.83 | 1 (Powerball) |
| `llm-fewshot` | 130 | 40 | 45.9 | 0.31/draw | -0.92 | 3 (NY Win 4) |
| `dreambook` | 58 | 16 | 20.3 | 0.28/draw | -1.01 | 2 (NY Numbers (Pick 3)) |
| `unpopular` | 25 | 6 | 9.0 | 0.24/draw | -1.07 | 2 (Mega Millions) |
| `cold` | 140 | 42 | 49.4 | 0.30/draw | -1.11 | 3 (NY Win 4) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-27 20:38 UTC</sub>
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
