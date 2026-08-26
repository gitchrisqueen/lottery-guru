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
### 🎟️ Predictions for 2026-08-26

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Powerball**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `35` `44` `54` `56` `61` + `13` |
| `balanced` | `09` `31` `57` `58` `64` + `12` |
| `benford` | `03` `14` `15` `28` `40` + `04` |
| `birthday` | `01` `05` `09` `15` `22` + `21` |
| `cold` | `01` `11` `23` `51` `52` + `19` |
| `contrarian` | `03` `10` `16` `33` `58` + `23` |
| `delta` | `04` `05` `37` `41` `47` + `20` |
| `highest-frequency` | `03` `09` `57` `64` `66` + `07` |
| `hot` | `03` `36` `56` `63` `64` + `14` |
| `llm-fewshot` | `46` `52` `53` `56` `63` + `07` |
| `moonphase` | `09` `24` `29` `45` `66` + `07` |
| `numerology` | `08` `10` `12` `20` `24` + `07` |
| `persistent` | `13` `21` `23` `32` `66` + `01` |
| `random` | `01` `35` `57` `64` `67` + `03` |
| `skiphit` | `27` `33` `38` `54` `68` + `23` |
| `unpopular` | `32` `40` `55` `57` `66` + `18` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `4` `5` |
| `contrarian` | `8` `2` `2` |
| `dreambook` | `0` `4` `3` |
| `highest-frequency` | `0` `2` `3` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `0` `6` `3` |
| `moonphase` | `0` `8` `3` |
| `numerology` | `1` `1` `1` |
| `persistent` | `4` `3` `3` |
| `positional` | `9` `9` `1` |
| `random` | `0` `2` `3` |
| `skiphit` | `8` `6` `2` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `4` `5` |
| `contrarian` | `6` `8` `2` |
| `dreambook` | `1` `8` `3` |
| `highest-frequency` | `8` `8` `2` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `9` `4` `7` |
| `moonphase` | `7` `1` `1` |
| `numerology` | `1` `1` `1` |
| `persistent` | `4` `3` `3` |
| `positional` | `8` `2` `0` |
| `random` | `9` `3` `9` |
| `skiphit` | `8` `8` `2` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `5` `2` `6` |
| `contrarian` | `7` `1` `1` `3` |
| `dreambook` | `3` `9` `0` `9` |
| `highest-frequency` | `8` `9` `0` `5` |
| `hot` | `8` `9` `3` `5` |
| `llm-fewshot` | `9` `8` `9` `8` |
| `moonphase` | `8` `9` `7` `2` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `4` `7` `0` `1` |
| `random` | `0` `1` `0` `2` |
| `skiphit` | `4` `4` `9` `1` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `5` `6` `2` |
| `contrarian` | `7` `1` `9` `1` |
| `dreambook` | `8` `7` `5` `1` |
| `highest-frequency` | `8` `1` `9` `1` |
| `hot` | `8` `9` `3` `5` |
| `llm-fewshot` | `9` `8` `7` `6` |
| `moonphase` | `6` `3` `1` `7` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `2` `1` `3` `9` |
| `random` | `0` `1` `9` `3` |
| `skiphit` | `4` `4` `9` `1` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `07` `09` `15` `29` `33` |
| `balanced` | `03` `08` `12` `18` `29` |
| `benford` | `04` `10` `12` `28` `36` |
| `birthday` | `03` `07` `10` `13` `26` |
| `cold` | `19` `22` `26` `30` `36` |
| `contrarian` | `12` `22` `23` `24` `25` |
| `delta` | `08` `18` `22` `23` `36` |
| `highest-frequency` | `10` `12` `22` `29` `30` |
| `hot` | `11` `17` `26` `29` `35` |
| `llm-fewshot` | `14` `18` `21` `30` `34` |
| `moonphase` | `02` `09` `25` `32` `34` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `08` `09` `10` `29` `30` |
| `skiphit` | `14` `21` `22` `30` `34` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `06` `07` `09` `12` `13` |
| `balanced` | `04` `14` `15` `21` `34` |
| `benford` | `05` `10` `13` `24` `30` |
| `birthday` | `02` `10` `18` `26` `27` |
| `cold` | `03` `09` `30` `33` `35` |
| `contrarian` | `04` `05` `22` `27` `36` |
| `delta` | `07` `08` `10` `18` `32` |
| `highest-frequency` | `05` `10` `12` `13` `18` |
| `hot` | `04` `08` `13` `18` `25` |
| `llm-fewshot` | `07` `12` `18` `23` `34` |
| `moonphase` | `13` `16` `18` `28` `35` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `06` `10` `21` `30` `31` |
| `skiphit` | `10` `14` `16` `23` `35` |

**Florida Lotto**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `36` `39` `40` `43` `46` `53` |
| `balanced` | `03` `04` `15` `20` `32` `49` |
| `benford` | `18` `19` `21` `34` `47` `53` |
| `birthday` | `04` `05` `12` `16` `19` `27` |
| `cold` | `07` `08` `14` `16` `33` `45` |
| `contrarian` | `08` `12` `19` `26` `28` `37` |
| `delta` | `02` `03` `13` `15` `27` `29` |
| `highest-frequency` | `08` `10` `20` `32` `33` `53` |
| `hot` | `11` `22` `28` `32` `41` `43` |
| `llm-fewshot` | `04` `08` `17` `26` `39` `53` |
| `moonphase` | `18` `31` `32` `34` `45` `53` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `05` `10` `32` `33` `38` `50` |
| `random` | `03` `10` `20` `27` `35` `51` |
| `skiphit` | `08` `11` `20` `21` `24` `33` |
| `unpopular` | `25` `33` `37` `38` `46` `48` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `3` |
| `contrarian` | `7` `2` |
| `dreambook` | `2` `4` |
| `highest-frequency` | `9` `4` |
| `hot` | `1` `0` |
| `llm-fewshot` | `9` `6` |
| `moonphase` | `9` `6` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `3` `8` |
| `random` | `9` `2` |
| `skiphit` | `7` `4` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `2` |
| `contrarian` | `5` `6` |
| `dreambook` | `9` `4` |
| `highest-frequency` | `5` `5` |
| `hot` | `7` `9` |
| `llm-fewshot` | `1` `5` |
| `moonphase` | `5` `3` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `5` `4` |
| `random` | `8` `5` |
| `skiphit` | `4` `2` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `5` `2` |
| `contrarian` | `5` `7` `1` |
| `dreambook` | `1` `0` `4` |
| `highest-frequency` | `1` `3` `5` |
| `hot` | `9` `3` `5` |
| `llm-fewshot` | `4` `3` `5` |
| `moonphase` | `8` `4` `5` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `9` `9` `8` |
| `random` | `8` `3` `4` |
| `skiphit` | `2` `5` `2` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `8` `6` |
| `contrarian` | `9` `9` `2` |
| `dreambook` | `2` `2` `9` |
| `highest-frequency` | `2` `2` `4` |
| `hot` | `0` `2` `8` |
| `llm-fewshot` | `2` `3` `5` |
| `moonphase` | `5` `1` `8` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `6` `5` `4` |
| `random` | `2` `6` `6` |
| `skiphit` | `7` `0` `4` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `8` `1` `2` |
| `contrarian` | `3` `7` `1` `1` |
| `dreambook` | `8` `4` `9` `4` |
| `highest-frequency` | `2` `5` `1` `1` |
| `hot` | `4` `2` `9` `3` |
| `llm-fewshot` | `8` `5` `8` `7` |
| `moonphase` | `6` `8` `6` `2` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `2` `5` `0` `1` |
| `random` | `7` `0` `1` `1` |
| `skiphit` | `2` `5` `9` `2` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `7` `2` `3` |
| `contrarian` | `5` `4` `4` `4` |
| `dreambook` | `7` `2` `3` `1` |
| `highest-frequency` | `5` `4` `0` `5` |
| `hot` | `8` `0` `7` `1` |
| `llm-fewshot` | `5` `2` `9` `8` |
| `moonphase` | `8` `4` `0` `5` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `5` `1` `6` `8` |
| `random` | `7` `0` `8` `1` |
| `skiphit` | `3` `4` `0` `4` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `1` `7` `0` `3` |
| `contrarian` | `9` `3` `2` `7` `2` |
| `dreambook` | `7` `2` `3` `1` `9` |
| `highest-frequency` | `1` `1` `4` `0` `1` |
| `hot` | `1` `5` `4` `2` `7` |
| `llm-fewshot` | `6` `4` `5` `0` `5` |
| `moonphase` | `8` `4` `9` `6` `1` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `9` `4` `0` `3` `7` |
| `random` | `0` `4` `0` `8` `1` |
| `skiphit` | `1` `1` `4` `0` `6` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `9` `3` `7` `8` |
| `contrarian` | `3` `1` `9` `9` `4` |
| `dreambook` | `0` `6` `2` `9` `3` |
| `highest-frequency` | `5` `1` `2` `9` `4` |
| `hot` | `2` `9` `3` `1` `4` |
| `llm-fewshot` | `5` `0` `6` `0` `9` |
| `moonphase` | `5` `8` `7` `8` `2` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `3` `6` `2` `8` `0` |
| `random` | `5` `9` `4` `3` `7` |
| `skiphit` | `9` `3` `1` `7` `3` |

<sub>Updated 2026-08-26 11:31 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**1306** predictions scored across **32** days. Combined, they've hit **491** numbers where pure chance predicts **460.3** (z = **+1.52**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `contrarian` | 67 | 36 | 23.5 | 0.54/draw | +2.72 | 2 (NY Numbers (Pick 3)) |
| `highest-frequency` | 100 | 47 | 35.2 | 0.47/draw | +2.11 | 2 (Mega Millions) |
| `benford` | 12 | 8 | 4.3 | 0.67/draw | +1.89 | 3 (Mega Millions) |
| `positional` | 112 | 48 | 39.3 | 0.43/draw | +1.46 | 2 (NY Win 4) |
| `random` | 136 | 57 | 47.9 | 0.42/draw | +1.38 | 2 (Mega Millions) |
| `birthday` | 12 | 7 | 4.3 | 0.58/draw | +1.38 | 2 (Powerball) |
| `skiphit` | 67 | 28 | 23.5 | 0.42/draw | +0.98 | 2 (NY Win 4) |
| `persistent` | 67 | 26 | 23.5 | 0.39/draw | +0.54 | 2 (NY Numbers (Pick 3)) |
| `hot` | 136 | 50 | 47.9 | 0.37/draw | +0.31 | 3 (NY Numbers (Pick 3)) |
| `numerology` | 67 | 24 | 23.5 | 0.36/draw | +0.10 | 2 (NY Numbers (Pick 3)) |
| `llm-tuned` | 74 | 26 | 26.1 | 0.35/draw | -0.03 | 3 (NY Win 4) |
| `delta` | 24 | 8 | 8.6 | 0.33/draw | -0.23 | 1 (Powerball) |
| `balanced` | 12 | 3 | 4.3 | 0.25/draw | -0.68 | 2 (Mega Millions) |
| `antibalanced` | 12 | 3 | 4.3 | 0.25/draw | -0.68 | 1 (Powerball) |
| `moonphase` | 67 | 20 | 23.5 | 0.30/draw | -0.77 | 2 (NY Win 4) |
| `cold` | 136 | 42 | 47.9 | 0.31/draw | -0.91 | 3 (NY Win 4) |
| `dreambook` | 55 | 15 | 19.2 | 0.27/draw | -1.01 | 2 (NY Numbers (Pick 3)) |
| `llm-fewshot` | 126 | 38 | 44.4 | 0.30/draw | -1.02 | 3 (NY Win 4) |
| `unpopular` | 24 | 5 | 8.6 | 0.21/draw | -1.33 | 2 (Mega Millions) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-26 11:31 UTC</sub>
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
