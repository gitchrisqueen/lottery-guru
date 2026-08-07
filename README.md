# 🎰 Lottery Guru

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-08-07

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Mega Millions**

| Strategy | Predicted |
|---|---|
| `cold` | `06` `08` `11` `28` `69` + `11` |
| `delta` | `09` `20` `28` `31` `43` + `19` |
| `highest-frequency` | `11` `13` `28` `36` `69` + `12` |
| `hot` | `13` `18` `21` `49` `56` + `12` |
| `llm-fewshot` | `11` `24` `36` `52` `58` + `07` |
| `llm-tuned` | `01` `14` `21` `28` `58` + `09` |
| `random` | `13` `36` `45` `61` `63` + `12` |
| `unpopular` | `17` `32` `50` `66` `69` + `14` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `9` |
| `highest-frequency` | `7` `5` `5` |
| `hot` | `8` `3` `5` |
| `llm-fewshot` | `7` `4` `2` |
| `llm-tuned` | `6` `8` `7` |
| `positional` | `1` `5` `2` |
| `random` | `3` `5` `5` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `9` |
| `highest-frequency` | `8` `5` `2` |
| `hot` | `8` `3` `5` |
| `llm-fewshot` | `8` `5` `1` |
| `llm-tuned` | `7` `8` `8` |
| `positional` | `9` `5` `2` |
| `random` | `1` `4` `0` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `7` `0` `2` |
| `highest-frequency` | `6` `4` `0` `3` |
| `hot` | `6` `2` `5` `3` |
| `llm-fewshot` | `6` `8` `6` `6` |
| `llm-tuned` | `4` `7` `5` `2` |
| `positional` | `5` `5` `9` `3` |
| `random` | `3` `4` `8` `9` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `2` `0` `7` |
| `highest-frequency` | `6` `2` `0` `3` |
| `hot` | `6` `2` `5` `3` |
| `llm-fewshot` | `2` `5` `0` `9` |
| `llm-tuned` | `3` `7` `1` `7` |
| `positional` | `8` `6` `4` `3` |
| `random` | `3` `4` `6` `1` |

<sub>Updated 2026-08-07 12:22 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**341** predictions scored across **14** days. Combined, they've hit **128** numbers where pure chance predicts **121.2** (z = **+0.65**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 24 | 16 | 8.5 | 0.67/draw | +2.70 | 2 (Mega Millions) |
| `llm-tuned` | 17 | 8 | 6.0 | 0.47/draw | +0.84 | 3 (NY Win 4) |
| `random` | 60 | 24 | 21.3 | 0.40/draw | +0.62 | 2 (Mega Millions) |
| `cold` | 60 | 23 | 21.3 | 0.38/draw | +0.39 | 3 (NY Win 4) |
| `positional` | 50 | 19 | 17.7 | 0.38/draw | +0.33 | 2 (NY Win 4) |
| `hot` | 60 | 22 | 21.3 | 0.37/draw | +0.16 | 2 (NY Numbers (Pick 3)) |
| `delta` | 10 | 2 | 3.6 | 0.20/draw | -0.90 | 1 (Powerball) |
| `llm-fewshot` | 50 | 14 | 17.8 | 0.28/draw | -0.95 | 2 (NY Win 4) |
| `unpopular` | 10 | 0 | 3.6 | 0.00/draw | -2.03 | 0 |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-07 12:22 UTC</sub>
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
