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
### 🎟️ Predictions for 2026-08-24

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Powerball**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `07` `12` `26` `34` + `08` |
| `balanced` | `34` `37` `39` `52` `54` + `17` |
| `benford` | `12` `13` `22` `33` `69` + `02` |
| `birthday` | `01` `02` `03` `05` `30` + `11` |
| `cold` | `11` `23` `33` `51` `52` + `19` |
| `contrarian` | `13` `21` `25` `57` `64` + `17` |
| `delta` | `02` `13` `23` `25` `29` + `14` |
| `highest-frequency` | `01` `12` `13` `21` `33` + `17` |
| `hot` | `06` `21` `56` `63` `64` + `14` |
| `llm-fewshot` | `01` `16` `41` `55` `61` + `06` |
| `llm-tuned` | `07` `27` `43` `55` `60` + `18` |
| `moonphase` | `08` `20` `26` `65` `68` + `10` |
| `numerology` | `06` `10` `12` `20` `24` + `05` |
| `persistent` | `13` `21` `23` `32` `66` + `01` |
| `random` | `14` `17` `33` `64` `68` + `05` |
| `skiphit` | `13` `49` `57` `65` `67` + `23` |
| `unpopular` | `36` `48` `50` `58` `61` + `03` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `0` `2` |
| `contrarian` | `7` `6` `5` |
| `dreambook` | `0` `4` `3` |
| `highest-frequency` | `5` `6` `3` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `9` `9` `5` |
| `llm-tuned` | `6` `2` `3` |
| `moonphase` | `5` `8` `8` |
| `numerology` | `1` `1` `8` |
| `persistent` | `4` `3` `3` |
| `positional` | `6` `0` `7` |
| `random` | `5` `6` `4` |
| `skiphit` | `7` `6` `5` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `0` `2` |
| `contrarian` | `4` `6` `5` |
| `dreambook` | `6` `2` `9` |
| `highest-frequency` | `0` `8` `2` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `5` `8` `9` |
| `llm-tuned` | `9` `6` `6` |
| `moonphase` | `0` `2` `3` |
| `numerology` | `1` `1` `8` |
| `persistent` | `4` `3` `3` |
| `positional` | `3` `9` `7` |
| `random` | `0` `5` `2` |
| `skiphit` | `7` `5` `5` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `1` `4` `0` |
| `contrarian` | `9` `8` `3` `0` |
| `dreambook` | `4` `9` `9` `7` |
| `highest-frequency` | `8` `9` `3` `5` |
| `hot` | `8` `3` `5` `9` |
| `llm-fewshot` | `8` `5` `3` `7` |
| `llm-tuned` | `9` `6` `6` `8` |
| `moonphase` | `5` `4` `7` `3` |
| `numerology` | `1` `1` `8` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `3` `7` `2` `0` |
| `random` | `7` `3` `4` `5` |
| `skiphit` | `8` `5` `3` `2` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `1` `4` `0` |
| `contrarian` | `8` `5` `9` `0` |
| `dreambook` | `5` `2` `3` `0` |
| `highest-frequency` | `8` `9` `4` `0` |
| `hot` | `8` `3` `5` `9` |
| `llm-fewshot` | `4` `4` `4` `8` |
| `llm-tuned` | `9` `0` `4` `1` |
| `moonphase` | `7` `8` `3` `4` |
| `numerology` | `1` `1` `8` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `2` `3` `0` `2` |
| `random` | `2` `9` `4` `3` |
| `skiphit` | `8` `9` `3` `2` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `20` `22` `25` `28` `35` |
| `balanced` | `05` `08` `12` `14` `33` |
| `benford` | `01` `03` `05` `10` `28` |
| `birthday` | `03` `07` `13` `16` `23` |
| `cold` | `02` `06` `09` `18` `22` |
| `contrarian` | `03` `05` `29` `30` `34` |
| `delta` | `09` `12` `17` `27` `30` |
| `highest-frequency` | `03` `05` `12` `20` `22` |
| `hot` | `11` `29` `30` `33` `34` |
| `llm-fewshot` | `10` `26` `31` `33` `36` |
| `llm-tuned` | `13` `16` `22` `34` `35` |
| `moonphase` | `12` `20` `21` `24` `32` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `08` `15` `21` `25` `35` |
| `skiphit` | `03` `20` `21` `25` `36` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `10` `18` `24` `26` `34` |
| `balanced` | `10` `11` `14` `17` `31` |
| `benford` | `04` `13` `15` `23` `36` |
| `birthday` | `01` `02` `03` `08` `15` |
| `cold` | `08` `11` `20` `21` `29` |
| `contrarian` | `03` `15` `23` `25` `33` |
| `delta` | `10` `20` `31` `32` `35` |
| `highest-frequency` | `03` `10` `18` `20` `30` |
| `hot` | `03` `09` `18` `25` `35` |
| `llm-fewshot` | `05` `09` `12` `18` `30` |
| `llm-tuned` | `01` `02` `03` `30` `35` |
| `moonphase` | `08` `12` `20` `29` `34` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `18` `22` `30` `34` `36` |
| `skiphit` | `04` `09` `26` `30` `33` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `6` |
| `contrarian` | `3` `0` |
| `dreambook` | `1` `6` |
| `highest-frequency` | `8` `1` |
| `hot` | `5` `7` |
| `llm-fewshot` | `6` `5` |
| `llm-tuned` | `6` `4` |
| `moonphase` | `8` `9` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `8` `7` |
| `random` | `7` `9` |
| `skiphit` | `2` `1` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `6` |
| `contrarian` | `3` `9` |
| `dreambook` | `5` `7` |
| `highest-frequency` | `8` `6` |
| `hot` | `4` `7` |
| `llm-fewshot` | `8` `6` |
| `llm-tuned` | `9` `6` |
| `moonphase` | `7` `8` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `6` `2` |
| `random` | `4` `4` |
| `skiphit` | `7` `2` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `6` `1` |
| `contrarian` | `0` `5` `3` |
| `dreambook` | `0` `4` `2` |
| `highest-frequency` | `8` `6` `0` |
| `hot` | `7` `5` `0` |
| `llm-fewshot` | `8` `0` `0` |
| `llm-tuned` | `6` `0` `8` |
| `moonphase` | `8` `3` `7` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `4` `2` `2` |
| `random` | `4` `8` `5` |
| `skiphit` | `5` `6` `4` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `2` `8` |
| `contrarian` | `9` `5` `0` |
| `dreambook` | `6` `4` `5` |
| `highest-frequency` | `8` `2` `4` |
| `hot` | `9` `2` `3` |
| `llm-fewshot` | `8` `3` `9` |
| `llm-tuned` | `9` `2` `0` |
| `moonphase` | `4` `1` `4` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `7` `0` `9` |
| `random` | `8` `0` `7` |
| `skiphit` | `8` `4` `1` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `3` `6` `9` |
| `contrarian` | `9` `5` `8` `6` |
| `dreambook` | `6` `1` `7` `6` |
| `highest-frequency` | `9` `5` `1` `6` |
| `hot` | `3` `5` `1` `7` |
| `llm-fewshot` | `9` `2` `1` `6` |
| `llm-tuned` | `1` `2` `2` `1` |
| `moonphase` | `8` `7` `4` `7` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `3` `9` `5` `3` |
| `random` | `9` `5` `2` `3` |
| `skiphit` | `8` `6` `3` `0` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `9` `4` `1` |
| `contrarian` | `6` `0` `1` `2` |
| `dreambook` | `0` `4` `2` `5` |
| `highest-frequency` | `1` `8` `1` `5` |
| `hot` | `9` `8` `3` `7` |
| `llm-fewshot` | `7` `2` `3` `0` |
| `llm-tuned` | `4` `0` `4` `7` |
| `moonphase` | `1` `1` `5` `4` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `0` `8` `0` `7` |
| `random` | `5` `6` `3` `5` |
| `skiphit` | `1` `3` `1` `6` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `1` `7` `5` `8` |
| `contrarian` | `8` `7` `9` `9` `7` |
| `dreambook` | `4` `0` `9` `3` `4` |
| `highest-frequency` | `4` `1` `9` `8` `7` |
| `hot` | `4` `1` `6` `8` `3` |
| `llm-fewshot` | `7` `3` `6` `2` `7` |
| `llm-tuned` | `5` `1` `4` `8` `8` |
| `moonphase` | `9` `1` `9` `2` `1` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `3` `5` `4` `7` `7` |
| `random` | `4` `1` `8` `8` `4` |
| `skiphit` | `6` `4` `9` `1` `7` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `0` `7` `2` `8` |
| `contrarian` | `0` `1` `3` `8` `5` |
| `dreambook` | `3` `4` `8` `7` `2` |
| `highest-frequency` | `5` `1` `8` `4` `4` |
| `hot` | `9` `5` `8` `1` `0` |
| `llm-fewshot` | `5` `2` `6` `0` `2` |
| `llm-tuned` | `5` `4` `6` `3` `4` |
| `moonphase` | `6` `6` `8` `2` `9` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `8` `6` `5` `4` `3` |
| `random` | `4` `2` `9` `4` `8` |
| `skiphit` | `8` `6` `9` `9` `7` |

<sub>Updated 2026-08-24 11:05 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**1173** predictions scored across **30** days. Combined, they've hit **447** numbers where pure chance predicts **413.4** (z = **+1.75**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `contrarian` | 57 | 32 | 20.0 | 0.56/draw | +2.84 | 2 (NY Numbers (Pick 3)) |
| `highest-frequency` | 90 | 45 | 31.7 | 0.50/draw | +2.50 | 2 (Mega Millions) |
| `benford` | 10 | 7 | 3.6 | 0.70/draw | +1.92 | 3 (Mega Millions) |
| `birthday` | 10 | 6 | 3.6 | 0.60/draw | +1.35 | 2 (Powerball) |
| `positional` | 104 | 44 | 36.5 | 0.42/draw | +1.31 | 2 (NY Win 4) |
| `persistent` | 57 | 25 | 20.0 | 0.44/draw | +1.18 | 2 (NY Numbers (Pick 3)) |
| `random` | 126 | 51 | 44.4 | 0.40/draw | +1.04 | 2 (Mega Millions) |
| `skiphit` | 57 | 24 | 20.0 | 0.42/draw | +0.94 | 2 (NY Win 4) |
| `hot` | 126 | 48 | 44.4 | 0.38/draw | +0.57 | 3 (NY Numbers (Pick 3)) |
| `numerology` | 57 | 22 | 20.0 | 0.39/draw | +0.47 | 2 (NY Numbers (Pick 3)) |
| `llm-tuned` | 69 | 25 | 24.4 | 0.36/draw | +0.14 | 3 (NY Win 4) |
| `delta` | 22 | 8 | 7.9 | 0.36/draw | +0.03 | 1 (Powerball) |
| `balanced` | 10 | 3 | 3.6 | 0.30/draw | -0.34 | 2 (Mega Millions) |
| `antibalanced` | 10 | 3 | 3.6 | 0.30/draw | -0.34 | 1 (Powerball) |
| `cold` | 126 | 38 | 44.4 | 0.30/draw | -1.02 | 3 (NY Win 4) |
| `unpopular` | 22 | 5 | 7.9 | 0.23/draw | -1.11 | 2 (Mega Millions) |
| `llm-fewshot` | 116 | 34 | 40.9 | 0.29/draw | -1.14 | 3 (NY Win 4) |
| `dreambook` | 47 | 12 | 16.4 | 0.26/draw | -1.15 | 2 (NY Numbers (Pick 3)) |
| `moonphase` | 57 | 15 | 20.0 | 0.26/draw | -1.18 | 2 (NY Win 4) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-24 11:05 UTC</sub>
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
