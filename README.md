# 🎰 Lottery Guru

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-08-16

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `4` |
| `contrarian` | `8` `2` `3` |
| `dreambook` | `0` `8` `5` |
| `highest-frequency` | `0` `2` `3` |
| `hot` | `8` `5` `3` |
| `llm-fewshot` | `9` `7` `0` |
| `moonphase` | `4` `4` `3` |
| `numerology` | `1` `1` `9` |
| `persistent` | `4` `3` `3` |
| `positional` | `2` `3` `4` |
| `random` | `0` `2` `1` |
| `skiphit` | `5` `2` `0` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `9` |
| `contrarian` | `8` `8` `3` |
| `dreambook` | `0` `4` `2` |
| `highest-frequency` | `8` `2` `3` |
| `hot` | `8` `5` `3` |
| `llm-fewshot` | `0` `7` `5` |
| `moonphase` | `8` `2` `3` |
| `numerology` | `1` `1` `9` |
| `persistent` | `4` `3` `3` |
| `positional` | `7` `6` `3` |
| `random` | `8` `2` `6` |
| `skiphit` | `5` `2` `0` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `0` `5` `1` |
| `contrarian` | `3` `1` `3` `4` |
| `dreambook` | `0` `4` `3` `1` |
| `highest-frequency` | `2` `1` `3` `1` |
| `hot` | `6` `8` `5` `3` |
| `llm-fewshot` | `4` `1` `4` `6` |
| `moonphase` | `2` `9` `0` `8` |
| `numerology` | `1` `1` `9` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `4` `3` `3` `7` |
| `random` | `8` `9` `9` `1` |
| `skiphit` | `2` `8` `3` `4` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `0` `5` `1` |
| `contrarian` | `3` `8` `9` `6` |
| `dreambook` | `3` `7` `8` `0` |
| `highest-frequency` | `1` `8` `8` `4` |
| `hot` | `6` `8` `5` `3` |
| `llm-fewshot` | `4` `4` `8` `3` |
| `moonphase` | `1` `5` `3` `2` |
| `numerology` | `1` `1` `9` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `1` `5` `1` `4` |
| `random` | `0` `3` `1` `4` |
| `skiphit` | `2` `8` `3` `4` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `09` `19` `23` `33` |
| `balanced` | `01` `09` `10` `25` `34` |
| `benford` | `01` `05` `18` `21` `30` |
| `birthday` | `02` `05` `08` `09` `17` |
| `cold` | `01` `04` `16` `26` `27` |
| `contrarian` | `04` `17` `23` `31` `34` |
| `delta` | `05` `10` `16` `17` `26` |
| `highest-frequency` | `01` `05` `09` `10` `17` |
| `hot` | `01` `11` `14` `25` `32` |
| `llm-fewshot` | `09` `18` `19` `27` `33` |
| `moonphase` | `02` `06` `12` `28` `31` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `04` `17` `23` `24` `28` |
| `skiphit` | `11` `13` `16` `22` `33` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `17` `26` `27` `30` `33` |
| `balanced` | `02` `05` `30` `32` `35` |
| `benford` | `03` `04` `12` `18` `23` |
| `birthday` | `05` `06` `08` `22` `31` |
| `cold` | `01` `03` `14` `16` `36` |
| `contrarian` | `13` `15` `19` `22` `28` |
| `delta` | `12` `14` `15` `21` `26` |
| `highest-frequency` | `14` `15` `26` `30` `36` |
| `hot` | `20` `27` `28` `33` `36` |
| `llm-fewshot` | `19` `24` `26` `30` `35` |
| `moonphase` | `04` `13` `21` `26` `31` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `07` `13` `14` `15` `29` |
| `skiphit` | `06` `15` `16` `26` `33` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `4` |
| `contrarian` | `4` `5` |
| `dreambook` | `3` `1` |
| `highest-frequency` | `1` `1` |
| `hot` | `5` `9` |
| `llm-fewshot` | `7` `3` |
| `moonphase` | `1` `8` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `3` `4` |
| `random` | `2` `6` |
| `skiphit` | `7` `1` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `4` |
| `contrarian` | `2` `4` |
| `dreambook` | `5` `0` |
| `highest-frequency` | `4` `1` |
| `hot` | `8` `4` |
| `llm-fewshot` | `2` `1` |
| `moonphase` | `4` `2` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `6` `3` |
| `random` | `4` `1` |
| `skiphit` | `4` `2` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `5` `7` |
| `contrarian` | `2` `5` `2` |
| `dreambook` | `6` `2` `7` |
| `highest-frequency` | `5` `2` `7` |
| `hot` | `5` `0` `7` |
| `llm-fewshot` | `5` `8` `3` |
| `moonphase` | `1` `3` `8` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `8` `2` `2` |
| `random` | `3` `1` `3` |
| `skiphit` | `5` `0` `2` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `5` `4` |
| `contrarian` | `1` `6` `8` |
| `dreambook` | `9` `8` `6` |
| `highest-frequency` | `1` `1` `4` |
| `hot` | `2` `1` `0` |
| `llm-fewshot` | `5` `0` `4` |
| `moonphase` | `1` `3` `3` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `6` `1` `0` |
| `random` | `5` `6` `1` |
| `skiphit` | `0` `2` `0` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `9` `7` `5` |
| `contrarian` | `5` `5` `7` `5` |
| `dreambook` | `0` `4` `8` `0` |
| `highest-frequency` | `7` `9` `5` `5` |
| `hot` | `7` `0` `4` `9` |
| `llm-fewshot` | `2` `5` `3` `2` |
| `moonphase` | `8` `9` `5` `3` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `8` `9` `0` `9` |
| `random` | `7` `3` `5` `2` |
| `skiphit` | `7` `2` `8` `7` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `6` `9` `3` |
| `contrarian` | `4` `4` `6` `3` |
| `dreambook` | `1` `0` `4` `0` |
| `highest-frequency` | `4` `0` `6` `0` |
| `hot` | `6` `8` `5` `2` |
| `llm-fewshot` | `4` `1` `8` `6` |
| `moonphase` | `8` `3` `6` `0` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `7` `0` `9` `5` |
| `random` | `3` `6` `3` `0` |
| `skiphit` | `3` `9` `9` `1` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `4` `2` `1` `6` |
| `contrarian` | `3` `5` `7` `5` `0` |
| `dreambook` | `4` `7` `3` `0` `3` |
| `highest-frequency` | `5` `1` `6` `1` `3` |
| `hot` | `7` `1` `6` `5` `4` |
| `llm-fewshot` | `5` `6` `6` `1` `5` |
| `moonphase` | `9` `5` `9` `8` `1` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `7` `8` `6` `3` `3` |
| `random` | `0` `1` `3` `2` `3` |
| `skiphit` | `8` `3` `7` `1` `3` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `9` `7` `1` `2` |
| `contrarian` | `7` `2` `2` `8` `8` |
| `dreambook` | `8` `8` `3` `6` `1` |
| `highest-frequency` | `0` `8` `1` `8` `4` |
| `hot` | `2` `8` `5` `6` `0` |
| `llm-fewshot` | `5` `8` `2` `0` `9` |
| `moonphase` | `1` `8` `5` `9` `7` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `7` `1` `7` `2` `0` |
| `random` | `8` `2` `1` `8` `5` |
| `skiphit` | `0` `5` `1` `7` `3` |

<sub>Updated 2026-08-16 10:47 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**722** predictions scored across **22** days. Combined, they've hit **270** numbers where pure chance predicts **255.3** (z = **+0.98**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 56 | 29 | 19.8 | 0.52/draw | +2.20 | 2 (Mega Millions) |
| `birthday` | 5 | 4 | 1.8 | 0.80/draw | +1.75 | 2 (Powerball) |
| `contrarian` | 23 | 12 | 8.1 | 0.52/draw | +1.45 | 2 (NY Numbers (Pick 3)) |
| `moonphase` | 23 | 11 | 8.1 | 0.48/draw | +1.08 | 2 (NY Win 4) |
| `benford` | 5 | 3 | 1.8 | 0.60/draw | +0.96 | 1 (Powerball) |
| `positional` | 75 | 31 | 26.4 | 0.41/draw | +0.94 | 2 (NY Win 4) |
| `llm-tuned` | 46 | 19 | 16.3 | 0.41/draw | +0.72 | 3 (NY Win 4) |
| `skiphit` | 23 | 10 | 8.1 | 0.43/draw | +0.71 | 1 (Powerball) |
| `persistent` | 23 | 10 | 8.1 | 0.43/draw | +0.71 | 2 (NY Numbers (Pick 3)) |
| `numerology` | 23 | 9 | 8.1 | 0.39/draw | +0.33 | 2 (NY Numbers (Pick 3)) |
| `balanced` | 5 | 2 | 1.8 | 0.40/draw | +0.16 | 2 (Mega Millions) |
| `antibalanced` | 5 | 2 | 1.8 | 0.40/draw | +0.16 | 1 (Powerball) |
| `delta` | 17 | 6 | 6.1 | 0.35/draw | -0.05 | 1 (Powerball) |
| `hot` | 92 | 32 | 32.5 | 0.35/draw | -0.10 | 2 (NY Numbers (Pick 3)) |
| `random` | 92 | 31 | 32.5 | 0.34/draw | -0.28 | 2 (Mega Millions) |
| `dreambook` | 18 | 5 | 6.3 | 0.28/draw | -0.55 | 1 (NY Win 4) |
| `cold` | 92 | 29 | 32.5 | 0.32/draw | -0.65 | 3 (NY Win 4) |
| `unpopular` | 17 | 3 | 6.1 | 0.18/draw | -1.35 | 2 (Mega Millions) |
| `llm-fewshot` | 82 | 22 | 29.0 | 0.27/draw | -1.37 | 2 (NY Win 4) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-16 10:47 UTC</sub>
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
