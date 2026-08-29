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
### 🎟️ Predictions for 2026-08-29

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Powerball**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `46` `60` `63` `67` `69` + `20` |
| `balanced` | `01` `05` `29` `40` `52` + `20` |
| `benford` | `10` `18` `21` `30` `44` + `24` |
| `birthday` | `04` `07` `08` `09` `21` + `01` |
| `cold` | `01` `11` `23` `51` `52` + `19` |
| `contrarian` | `31` `32` `38` `45` `58` + `02` |
| `delta` | `02` `05` `09` `22` `32` + `13` |
| `highest-frequency` | `03` `21` `32` `46` `58` + `20` |
| `hot` | `03` `06` `58` `63` `64` + `02` |
| `llm-fewshot` | `17` `33` `36` `46` `56` + `20` |
| `moonphase` | `14` `17` `20` `31` `59` + `07` |
| `numerology` | `10` `12` `20` `24` `36` + `09` |
| `persistent` | `13` `21` `23` `32` `66` + `01` |
| `random` | `03` `17` `18` `22` `35` + `06` |
| `skiphit` | `03` `12` `32` `45` `58` + `23` |
| `unpopular` | `37` `46` `55` `62` `65` + `22` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `1` `2` |
| `contrarian` | `8` `4` `3` |
| `dreambook` | `9` `3` `9` |
| `highest-frequency` | `8` `4` `4` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `4` `9` `0` |
| `moonphase` | `2` `4` `4` |
| `numerology` | `1` `1` `4` |
| `persistent` | `4` `3` `3` |
| `positional` | `7` `9` `7` |
| `random` | `5` `5` `4` |
| `skiphit` | `8` `4` `8` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `1` `2` |
| `contrarian` | `8` `4` `8` |
| `dreambook` | `7` `2` `4` |
| `highest-frequency` | `8` `3` `2` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `2` `9` `1` |
| `moonphase` | `1` `5` `9` |
| `numerology` | `1` `1` `4` |
| `persistent` | `4` `3` `3` |
| `positional` | `7` `3` `1` |
| `random` | `8` `7` `2` |
| `skiphit` | `8` `4` `8` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `7` `0` `4` |
| `contrarian` | `1` `6` `2` `0` |
| `dreambook` | `2` `7` `8` `1` |
| `highest-frequency` | `8` `7` `2` `4` |
| `hot` | `8` `9` `5` `3` |
| `llm-fewshot` | `8` `8` `9` `6` |
| `moonphase` | `4` `7` `8` `4` |
| `numerology` | `1` `1` `4` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `7` `5` `9` `4` |
| `random` | `0` `5` `2` `6` |
| `skiphit` | `8` `6` `2` `1` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `7` `0` `4` |
| `contrarian` | `1` `5` `5` `3` |
| `dreambook` | `1` `9` `1` `7` |
| `highest-frequency` | `1` `9` `6` `3` |
| `hot` | `8` `9` `5` `3` |
| `llm-fewshot` | `2` `7` `3` `6` |
| `moonphase` | `4` `1` `0` `4` |
| `numerology` | `1` `1` `4` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `1` `7` `6` `9` |
| `random` | `0` `4` `7` `2` |
| `skiphit` | `8` `6` `2` `1` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `03` `15` `23` `29` `35` |
| `balanced` | `05` `06` `26` `31` `36` |
| `benford` | `04` `06` `19` `22` `33` |
| `birthday` | `01` `03` `06` `11` `31` |
| `cold` | `05` `19` `25` `26` `27` |
| `contrarian` | `03` `16` `23` `27` `32` |
| `delta` | `03` `13` `19` `22` `30` |
| `highest-frequency` | `03` `06` `19` `23` `26` |
| `hot` | `06` `08` `14` `23` `24` |
| `llm-fewshot` | `07` `09` `13` `32` `35` |
| `moonphase` | `19` `27` `31` `32` `36` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `07` `12` `23` `29` `30` |
| `skiphit` | `06` `12` `14` `15` `28` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `10` `23` `30` `33` `34` |
| `balanced` | `04` `09` `13` `29` `32` |
| `benford` | `02` `04` `13` `15` `30` |
| `birthday` | `01` `03` `04` `10` `12` |
| `cold` | `01` `10` `17` `21` `34` |
| `contrarian` | `03` `15` `29` `31` `33` |
| `delta` | `05` `09` `16` `18` `29` |
| `highest-frequency` | `04` `10` `12` `20` `29` |
| `hot` | `10` `15` `20` `28` `31` |
| `llm-fewshot` | `07` `14` `23` `29` `35` |
| `moonphase` | `02` `12` `20` `25` `36` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `03` `04` `05` `07` `08` |
| `skiphit` | `06` `07` `08` `11` `12` |

**Florida Lotto**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `06` `24` `40` `42` `50` `52` |
| `balanced` | `10` `20` `29` `32` `39` `51` |
| `benford` | `14` `17` `21` `35` `48` `51` |
| `birthday` | `01` `02` `08` `11` `25` `30` |
| `cold` | `04` `20` `22` `36` `37` `43` |
| `contrarian` | `14` `26` `28` `35` `45` `50` |
| `delta` | `04` `06` `15` `17` `18` `25` |
| `highest-frequency` | `06` `10` `17` `30` `36` `51` |
| `hot` | `06` `17` `36` `40` `45` `46` |
| `llm-fewshot` | `07` `10` `11` `18` `31` `41` |
| `moonphase` | `04` `08` `15` `22` `26` `53` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `05` `10` `32` `33` `38` `50` |
| `random` | `17` `19` `29` `30` `36` `42` |
| `skiphit` | `03` `31` `33` `34` `35` `49` |
| `unpopular` | `25` `32` `34` `44` `45` `51` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `4` |
| `contrarian` | `9` `0` |
| `dreambook` | `2` `0` |
| `highest-frequency` | `8` `4` |
| `hot` | `0` `4` |
| `llm-fewshot` | `1` `5` |
| `moonphase` | `7` `2` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `8` `8` |
| `random` | `4` `9` |
| `skiphit` | `3` `8` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `9` |
| `contrarian` | `4` `9` |
| `dreambook` | `5` `6` |
| `highest-frequency` | `6` `1` |
| `hot` | `4` `5` |
| `llm-fewshot` | `6` `7` |
| `moonphase` | `8` `0` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `2` `1` |
| `random` | `2` `0` |
| `skiphit` | `5` `3` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `2` `3` |
| `contrarian` | `0` `8` `9` |
| `dreambook` | `8` `8` `3` |
| `highest-frequency` | `8` `1` `3` |
| `hot` | `0` `5` `2` |
| `llm-fewshot` | `6` `3` `3` |
| `moonphase` | `1` `4` `7` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `5` `1` `8` |
| `random` | `7` `5` `6` |
| `skiphit` | `1` `9` `6` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `2` `3` |
| `contrarian` | `7` `6` `1` |
| `dreambook` | `7` `5` `2` |
| `highest-frequency` | `7` `6` `1` |
| `hot` | `7` `0` `3` |
| `llm-fewshot` | `8` `0` `5` |
| `moonphase` | `9` `7` `5` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `2` `7` `1` |
| `random` | `8` `1` `5` |
| `skiphit` | `0` `6` `0` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `2` `4` |
| `contrarian` | `5` `4` `9` `6` |
| `dreambook` | `7` `2` `3` `1` |
| `highest-frequency` | `6` `2` `1` `5` |
| `hot` | `3` `7` `4` `5` |
| `llm-fewshot` | `4` `3` `8` `1` |
| `moonphase` | `6` `6` `1` `6` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `0` `2` `6` `3` |
| `random` | `9` `2` `4` `2` |
| `skiphit` | `8` `9` `1` `8` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `8` `7` `9` |
| `contrarian` | `6` `8` `5` `2` |
| `dreambook` | `3` `4` `8` `7` |
| `highest-frequency` | `9` `8` `5` `7` |
| `hot` | `6` `3` `5` `7` |
| `llm-fewshot` | `0` `8` `3` `9` |
| `moonphase` | `9` `6` `2` `7` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `9` `0` `9` `2` |
| `random` | `0` `9` `8` `0` |
| `skiphit` | `9` `5` `4` `4` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `9` `6` `1` `2` |
| `contrarian` | `3` `4` `4` `2` `4` |
| `dreambook` | `5` `9` `2` `1` `8` |
| `highest-frequency` | `5` `9` `2` `1` `7` |
| `hot` | `3` `8` `2` `4` `7` |
| `llm-fewshot` | `2` `4` `2` `1` `8` |
| `moonphase` | `7` `7` `8` `7` `3` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `4` `7` `9` `0` `7` |
| `random` | `1` `3` `2` `9` `7` |
| `skiphit` | `9` `9` `9` `5` `7` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `3` `2` `7` `6` |
| `contrarian` | `8` `6` `5` `6` `1` |
| `dreambook` | `2` `3` `4` `4` `0` |
| `highest-frequency` | `7` `3` `1` `2` `6` |
| `hot` | `4` `5` `2` `6` `1` |
| `llm-fewshot` | `7` `9` `9` `9` `8` |
| `moonphase` | `3` `2` `8` `3` `0` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `0` `5` `1` `8` `7` |
| `random` | `7` `9` `1` `2` `6` |
| `skiphit` | `2` `7` `5` `2` `6` |

<sub>Updated 2026-08-29 15:13 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**1463** predictions scored across **35** days. Combined, they've hit **548** numbers where pure chance predicts **516.7** (z = **+1.46**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `contrarian` | 79 | 40 | 27.8 | 0.51/draw | +2.44 | 2 (NY Numbers (Pick 3)) |
| `highest-frequency` | 112 | 51 | 39.5 | 0.46/draw | +1.93 | 2 (Mega Millions) |
| `random` | 148 | 64 | 52.3 | 0.43/draw | +1.72 | 2 (Mega Millions) |
| `benford` | 14 | 8 | 5.0 | 0.57/draw | +1.41 | 3 (Mega Millions) |
| `positional` | 122 | 50 | 42.9 | 0.41/draw | +1.14 | 2 (NY Win 4) |
| `birthday` | 14 | 7 | 5.0 | 0.50/draw | +0.93 | 2 (Powerball) |
| `skiphit` | 79 | 32 | 27.8 | 0.41/draw | +0.83 | 2 (NY Win 4) |
| `persistent` | 79 | 32 | 27.8 | 0.41/draw | +0.83 | 2 (NY Numbers (Pick 3)) |
| `numerology` | 79 | 31 | 27.8 | 0.39/draw | +0.63 | 2 (NY Numbers (Pick 3)) |
| `hot` | 148 | 56 | 52.3 | 0.38/draw | +0.55 | 3 (NY Numbers (Pick 3)) |
| `llm-tuned` | 79 | 27 | 27.9 | 0.34/draw | -0.18 | 3 (NY Win 4) |
| `delta` | 26 | 8 | 9.4 | 0.31/draw | -0.48 | 1 (Powerball) |
| `balanced` | 14 | 4 | 5.0 | 0.29/draw | -0.50 | 2 (Mega Millions) |
| `antibalanced` | 14 | 4 | 5.0 | 0.29/draw | -0.50 | 1 (Powerball) |
| `moonphase` | 79 | 24 | 27.8 | 0.30/draw | -0.77 | 2 (NY Win 4) |
| `unpopular` | 26 | 7 | 9.4 | 0.27/draw | -0.83 | 2 (Mega Millions) |
| `llm-fewshot` | 138 | 42 | 48.7 | 0.30/draw | -1.02 | 3 (NY Win 4) |
| `cold` | 148 | 44 | 52.3 | 0.30/draw | -1.21 | 3 (NY Win 4) |
| `dreambook` | 65 | 17 | 22.8 | 0.26/draw | -1.28 | 2 (NY Numbers (Pick 3)) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-29 15:13 UTC</sub>
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
