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
### 🎟️ Predictions for 2026-08-25

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Mega Millions**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `05` `17` `22` `58` + `06` |
| `balanced` | `05` `32` `35` `52` `55` + `12` |
| `benford` | `03` `12` `13` `23` `40` + `13` |
| `birthday` | `04` `05` `06` `11` `12` + `06` |
| `cold` | `06` `08` `11` `28` `69` + `18` |
| `contrarian` | `03` `34` `38` `46` `48` + `24` |
| `delta` | `06` `13` `15` `26` `37` + `02` |
| `highest-frequency` | `05` `06` `12` `34` `37` + `12` |
| `hot` | `21` `34` `42` `43` `49` + `12` |
| `llm-fewshot` | `21` `40` `42` `49` `60` + `12` |
| `moonphase` | `37` `39` `59` `66` `69` + `07` |
| `numerology` | `05` `10` `12` `20` `24` + `04` |
| `persistent` | `01` `09` `37` `38` `39` + `22` |
| `random` | `19` `20` `44` `58` `59` + `23` |
| `skiphit` | `19` `25` `34` `48` `57` + `24` |
| `unpopular` | `23` `32` `37` `44` `45` + `16` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `0` `4` |
| `contrarian` | `7` `8` `1` |
| `dreambook` | `5` `9` `2` |
| `highest-frequency` | `4` `2` `2` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `9` `6` `2` |
| `moonphase` | `1` `2` `7` |
| `numerology` | `1` `1` `9` |
| `persistent` | `4` `3` `3` |
| `positional` | `4` `3` `8` |
| `random` | `0` `7` `7` |
| `skiphit` | `8` `2` `9` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `0` `4` |
| `contrarian` | `8` `8` `9` |
| `dreambook` | `2` `6` `1` |
| `highest-frequency` | `8` `3` `9` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `4` `3` `7` |
| `moonphase` | `7` `3` `5` |
| `numerology` | `1` `1` `9` |
| `persistent` | `4` `3` `3` |
| `positional` | `5` `4` `0` |
| `random` | `5` `3` `9` |
| `skiphit` | `8` `2` `1` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `8` `5` `4` |
| `contrarian` | `6` `4` `9` `2` |
| `dreambook` | `0` `4` `3` `1` |
| `highest-frequency` | `0` `4` `9` `5` |
| `hot` | `8` `3` `9` `5` |
| `llm-fewshot` | `9` `7` `1` `5` |
| `moonphase` | `6` `8` `8` `5` |
| `numerology` | `1` `1` `9` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `7` `1` `0` `3` |
| `random` | `7` `1` `8` `5` |
| `skiphit` | `9` `4` `4` `3` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `8` `5` `2` |
| `contrarian` | `7` `4` `9` `3` |
| `dreambook` | `5` `9` `5` `8` |
| `highest-frequency` | `8` `9` `5` `3` |
| `hot` | `8` `3` `9` `5` |
| `llm-fewshot` | `8` `1` `5` `1` |
| `moonphase` | `9` `9` `8` `3` |
| `numerology` | `1` `1` `9` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `8` `5` `1` `7` |
| `random` | `5` `3` `4` `1` |
| `skiphit` | `9` `4` `4` `3` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `08` `10` `12` `14` `18` |
| `balanced` | `07` `12` `19` `20` `34` |
| `benford` | `04` `14` `15` `22` `30` |
| `birthday` | `07` `10` `14` `18` `19` |
| `cold` | `06` `13` `14` `15` `35` |
| `contrarian` | `02` `10` `16` `25` `31` |
| `delta` | `08` `19` `28` `29` `30` |
| `highest-frequency` | `08` `12` `14` `16` `20` |
| `hot` | `05` `07` `21` `25` `29` |
| `llm-fewshot` | `03` `06` `08` `12` `18` |
| `moonphase` | `04` `06` `08` `16` `20` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `04` `08` `11` `12` `16` |
| `skiphit` | `03` `06` `16` `20` `36` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `06` `10` `12` `16` `34` |
| `balanced` | `02` `17` `25` `27` `34` |
| `benford` | `04` `10` `15` `24` `35` |
| `birthday` | `02` `03` `07` `08` `30` |
| `cold` | `09` `24` `28` `34` `36` |
| `contrarian` | `04` `05` `19` `33` `34` |
| `delta` | `01` `07` `10` `15` `25` |
| `highest-frequency` | `01` `10` `12` `24` `34` |
| `hot` | `09` `12` `25` `26` `30` |
| `llm-fewshot` | `01` `13` `15` `18` `26` |
| `moonphase` | `09` `11` `29` `31` `33` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `07` `18` `19` `28` `33` |
| `skiphit` | `01` `02` `08` `19` `24` |

**FL Jackpot Triple Play**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `21` `26` `33` `34` `36` `44` |
| `balanced` | `12` `14` `17` `25` `30` `39` |
| `benford` | `03` `05` `12` `19` `23` `42` |
| `birthday` | `01` `05` `06` `08` `10` `22` |
| `cold` | `01` `06` `16` `18` `36` `37` |
| `contrarian` | `03` `05` `21` `29` `31` `41` |
| `delta` | `11` `15` `17` `28` `29` `31` |
| `highest-frequency` | `01` `03` `10` `21` `22` `36` |
| `hot` | `06` `21` `22` `33` `35` `40` |
| `llm-fewshot` | `01` `10` `11` `22` `34` `42` |
| `moonphase` | `03` `10` `32` `35` `44` `46` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `01` `04` `10` `18` `21` `29` |
| `random` | `07` `27` `36` `38` `45` `46` |
| `skiphit` | `15` `16` `18` `26` `41` `45` |
| `unpopular` | `17` `35` `36` `37` `39` `42` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `9` |
| `contrarian` | `7` `6` |
| `dreambook` | `9` `4` |
| `highest-frequency` | `4` `1` |
| `hot` | `9` `7` |
| `llm-fewshot` | `1` `3` |
| `moonphase` | `9` `1` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `3` `0` |
| `random` | `4` `5` |
| `skiphit` | `4` `3` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `7` |
| `contrarian` | `4` `6` |
| `dreambook` | `4` `5` |
| `highest-frequency` | `8` `1` |
| `hot` | `7` `0` |
| `llm-fewshot` | `0` `1` |
| `moonphase` | `5` `2` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `8` `4` |
| `random` | `8` `7` |
| `skiphit` | `6` `6` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `7` `8` |
| `contrarian` | `0` `5` `5` |
| `dreambook` | `1` `9` `1` |
| `highest-frequency` | `2` `7` `1` |
| `hot` | `8` `4` `1` |
| `llm-fewshot` | `2` `8` `3` |
| `moonphase` | `3` `7` `0` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `4` `9` `2` |
| `random` | `2` `3` `5` |
| `skiphit` | `5` `0` `0` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `6` `7` |
| `contrarian` | `1` `1` `5` |
| `dreambook` | `2` `5` `9` |
| `highest-frequency` | `2` `4` `9` |
| `hot` | `4` `5` `7` |
| `llm-fewshot` | `3` `3` `1` |
| `moonphase` | `2` `2` `0` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `9` `4` `9` |
| `random` | `3` `4` `0` |
| `skiphit` | `2` `9` `6` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `9` `2` `0` |
| `contrarian` | `0` `2` `9` `1` |
| `dreambook` | `3` `5` `3` `6` |
| `highest-frequency` | `3` `4` `2` `6` |
| `hot` | `7` `8` `2` `6` |
| `llm-fewshot` | `0` `0` `7` `1` |
| `moonphase` | `4` `7` `4` `2` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `7` `9` `2` `8` |
| `random` | `9` `4` `8` `6` |
| `skiphit` | `4` `7` `0` `6` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `9` `4` `6` |
| `contrarian` | `8` `8` `4` `3` |
| `dreambook` | `0` `6` `0` `0` |
| `highest-frequency` | `2` `4` `0` `3` |
| `hot` | `7` `3` `9` `8` |
| `llm-fewshot` | `8` `0` `1` `1` |
| `moonphase` | `2` `4` `0` `6` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `5` `2` `9` `8` |
| `random` | `4` `1` `2` `3` |
| `skiphit` | `2` `9` `0` `3` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `6` `0` `2` `9` |
| `contrarian` | `4` `3` `9` `0` `1` |
| `dreambook` | `5` `7` `5` `6` `2` |
| `highest-frequency` | `1` `1` `1` `5` `9` |
| `hot` | `9` `1` `5` `4` `6` |
| `llm-fewshot` | `1` `2` `1` `8` `9` |
| `moonphase` | `6` `9` `4` `5` `9` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `8` `0` `8` `3` `9` |
| `random` | `8` `3` `8` `0` `0` |
| `skiphit` | `0` `4` `3` `8` `8` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `4` `9` `5` `8` |
| `contrarian` | `9` `7` `5` `7` `2` |
| `dreambook` | `0` `6` `3` `2` `7` |
| `highest-frequency` | `5` `1` `9` `4` `7` |
| `hot` | `1` `5` `4` `0` `9` |
| `llm-fewshot` | `5` `1` `0` `4` `7` |
| `moonphase` | `3` `1` `5` `4` `7` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `0` `9` `9` `0` `1` |
| `random` | `5` `8` `9` `3` `4` |
| `skiphit` | `0` `6` `2` `8` `0` |

<sub>Updated 2026-08-25 11:29 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**1242** predictions scored across **31** days. Combined, they've hit **473** numbers where pure chance predicts **437.7** (z = **+1.78**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `contrarian` | 62 | 33 | 21.8 | 0.53/draw | +2.55 | 2 (NY Numbers (Pick 3)) |
| `highest-frequency` | 95 | 46 | 33.4 | 0.48/draw | +2.30 | 2 (Mega Millions) |
| `benford` | 11 | 8 | 4.0 | 0.73/draw | +2.17 | 3 (Mega Millions) |
| `birthday` | 11 | 7 | 4.0 | 0.64/draw | +1.63 | 2 (Powerball) |
| `random` | 131 | 55 | 46.2 | 0.42/draw | +1.37 | 2 (Mega Millions) |
| `positional` | 108 | 45 | 37.9 | 0.42/draw | +1.22 | 2 (NY Win 4) |
| `skiphit` | 62 | 25 | 21.8 | 0.40/draw | +0.73 | 2 (NY Win 4) |
| `persistent` | 62 | 25 | 21.8 | 0.40/draw | +0.73 | 2 (NY Numbers (Pick 3)) |
| `hot` | 131 | 49 | 46.2 | 0.37/draw | +0.44 | 3 (NY Numbers (Pick 3)) |
| `numerology` | 62 | 23 | 21.8 | 0.37/draw | +0.28 | 2 (NY Numbers (Pick 3)) |
| `llm-tuned` | 74 | 26 | 26.1 | 0.35/draw | -0.03 | 3 (NY Win 4) |
| `delta` | 23 | 8 | 8.3 | 0.35/draw | -0.11 | 1 (Powerball) |
| `moonphase` | 62 | 20 | 21.8 | 0.32/draw | -0.40 | 2 (NY Win 4) |
| `balanced` | 11 | 3 | 4.0 | 0.27/draw | -0.52 | 2 (Mega Millions) |
| `antibalanced` | 11 | 3 | 4.0 | 0.27/draw | -0.52 | 1 (Powerball) |
| `cold` | 131 | 42 | 46.2 | 0.32/draw | -0.65 | 3 (NY Win 4) |
| `dreambook` | 51 | 14 | 17.8 | 0.27/draw | -0.95 | 2 (NY Numbers (Pick 3)) |
| `llm-fewshot` | 121 | 36 | 42.7 | 0.30/draw | -1.08 | 3 (NY Win 4) |
| `unpopular` | 23 | 5 | 8.3 | 0.22/draw | -1.22 | 2 (Mega Millions) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-25 11:29 UTC</sub>
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
