# 🎰 Lottery Guru

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-08-13

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `6` `3` |
| `contrarian` | `1` `9` `1` |
| `dreambook` | `2` `0` `5` |
| `highest-frequency` | `1` `5` `3` |
| `hot` | `8` `5` `3` |
| `llm-fewshot` | `1` `6` `1` |
| `moonphase` | `1` `4` `4` |
| `numerology` | `1` `1` `5` |
| `persistent` | `4` `3` `3` |
| `positional` | `3` `0` `4` |
| `random` | `0` `7` `7` |
| `skiphit` | `1` `5` `7` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `6` `3` |
| `contrarian` | `1` `1` `1` |
| `dreambook` | `5` `6` `8` |
| `highest-frequency` | `1` `6` `3` |
| `hot` | `8` `5` `3` |
| `llm-fewshot` | `4` `7` `2` |
| `moonphase` | `5` `4` `0` |
| `numerology` | `1` `1` `5` |
| `persistent` | `4` `3` `3` |
| `positional` | `7` `5` `9` |
| `random` | `9` `9` `0` |
| `skiphit` | `1` `9` `7` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `7` `0` `2` |
| `contrarian` | `2` `6` `9` `9` |
| `dreambook` | `3` `4` `8` `7` |
| `highest-frequency` | `1` `1` `5` `8` |
| `hot` | `6` `8` `5` `2` |
| `llm-fewshot` | `2` `1` `5` `0` |
| `moonphase` | `7` `3` `0` `8` |
| `numerology` | `1` `1` `6` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `7` `7` `9` `3` |
| `random` | `1` `5` `7` `9` |
| `skiphit` | `2` `4` `5` `8` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `7` `0` `5` |
| `contrarian` | `3` `9` `9` `9` |
| `dreambook` | `0` `6` `0` `0` |
| `highest-frequency` | `5` `9` `9` `5` |
| `hot` | `6` `8` `5` `2` |
| `llm-fewshot` | `4` `3` `3` `6` |
| `moonphase` | `3` `1` `9` `3` |
| `numerology` | `1` `1` `6` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `5` `2` `1` `4` |
| `random` | `5` `9` `2` `6` |
| `skiphit` | `9` `4` `5` `8` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `18` `29` `30` `34` `36` |
| `balanced` | `06` `07` `13` `32` `34` |
| `benford` | `01` `04` `16` `24` `34` |
| `birthday` | `08` `09` `10` `12` `13` |
| `cold` | `03` `08` `18` `19` `35` |
| `contrarian` | `14` `15` `22` `27` `33` |
| `delta` | `07` `20` `24` `25` `33` |
| `highest-frequency` | `14` `22` `24` `25` `26` |
| `hot` | `14` `16` `26` `28` `35` |
| `llm-fewshot` | `06` `17` `22` `23` `25` |
| `moonphase` | `03` `15` `16` `21` `25` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `06` `20` `24` `26` `36` |
| `skiphit` | `10` `11` `21` `24` `26` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `02` `06` `28` `32` `36` |
| `balanced` | `05` `06` `24` `30` `35` |
| `benford` | `04` `12` `15` `27` `31` |
| `birthday` | `02` `04` `12` `28` `31` |
| `cold` | `08` `09` `26` `27` `31` |
| `contrarian` | `18` `20` `22` `28` `32` |
| `delta` | `03` `16` `18` `25` `35` |
| `highest-frequency` | `04` `16` `20` `31` `35` |
| `hot` | `10` `17` `19` `24` `26` |
| `llm-fewshot` | `04` `19` `23` `31` `35` |
| `moonphase` | `02` `16` `20` `21` `35` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `06` `13` `16` `18` `31` |
| `skiphit` | `05` `15` `17` `22` `25` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `1` |
| `contrarian` | `4` `0` |
| `dreambook` | `0` `6` |
| `highest-frequency` | `1` `1` |
| `hot` | `1` `3` |
| `llm-fewshot` | `2` `4` |
| `moonphase` | `5` `9` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `5` `7` |
| `random` | `7` `6` |
| `skiphit` | `3` `7` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `0` |
| `contrarian` | `1` `7` |
| `dreambook` | `9` `9` |
| `highest-frequency` | `1` `1` |
| `hot` | `5` `9` |
| `llm-fewshot` | `2` `1` |
| `moonphase` | `6` `3` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `4` `6` |
| `random` | `1` `4` |
| `skiphit` | `0` `2` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `6` `5` |
| `contrarian` | `5` `5` `5` |
| `dreambook` | `8` `4` `1` |
| `highest-frequency` | `8` `6` `5` |
| `hot` | `3` `6` `9` |
| `llm-fewshot` | `5` `2` `4` |
| `moonphase` | `0` `8` `5` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `7` `7` `5` |
| `random` | `2` `5` `7` |
| `skiphit` | `4` `9` `6` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `0` `3` |
| `contrarian` | `7` `9` `9` |
| `dreambook` | `2` `7` `8` |
| `highest-frequency` | `6` `7` `4` |
| `hot` | `6` `3` `4` |
| `llm-fewshot` | `6` `7` `3` |
| `moonphase` | `5` `8` `4` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `1` `1` `2` |
| `random` | `0` `8` `4` |
| `skiphit` | `7` `3` `5` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `4` `0` `2` |
| `contrarian` | `7` `8` `6` `8` |
| `dreambook` | `2` `3` `4` `4` |
| `highest-frequency` | `7` `3` `6` `2` |
| `hot` | `9` `5` `0` `2` |
| `llm-fewshot` | `6` `3` `6` `1` |
| `moonphase` | `7` `0` `8` `0` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `8` `9` `2` `2` |
| `random` | `0` `1` `7` `0` |
| `skiphit` | `3` `0` `4` `6` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `2` `1` `5` |
| `contrarian` | `6` `4` `0` `2` |
| `dreambook` | `7` `9` `1` `4` |
| `highest-frequency` | `2` `5` `1` `5` |
| `hot` | `7` `0` `5` `9` |
| `llm-fewshot` | `9` `3` `1` `9` |
| `moonphase` | `2` `5` `0` `0` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `7` `0` `4` `3` |
| `random` | `6` `9` `8` `9` |
| `skiphit` | `2` `5` `9` `5` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `0` `4` `9` `3` |
| `contrarian` | `9` `2` `0` `7` `4` |
| `dreambook` | `9` `2` `7` `5` `1` |
| `highest-frequency` | `9` `2` `1` `6` `4` |
| `hot` | `2` `3` `7` `6` `0` |
| `llm-fewshot` | `9` `0` `1` `7` `3` |
| `moonphase` | `6` `7` `6` `0` `0` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `4` `2` `1` `9` `7` |
| `random` | `9` `6` `9` `6` `3` |
| `skiphit` | `9` `9` `4` `8` `5` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `4` `7` `1` `5` |
| `contrarian` | `0` `4` `0` `2` `1` |
| `dreambook` | `0` `6` `3` `2` `7` |
| `highest-frequency` | `5` `4` `3` `5` `1` |
| `hot` | `8` `4` `7` `5` `9` |
| `llm-fewshot` | `5` `0` `3` `9` `2` |
| `moonphase` | `4` `7` `5` `1` `9` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `1` `2` `6` `9` `7` |
| `random` | `5` `9` `4` `5` `1` |
| `skiphit` | `4` `5` `0` `4` `1` |

<sub>Updated 2026-08-13 11:21 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**574** predictions scored across **19** days. Combined, they've hit **214** numbers where pure chance predicts **203.7** (z = **+0.76**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 45 | 25 | 15.9 | 0.56/draw | +2.40 | 2 (Mega Millions) |
| `moonphase` | 12 | 7 | 4.3 | 0.58/draw | +1.39 | 2 (NY Win 4) |
| `positional` | 66 | 28 | 23.3 | 0.42/draw | +1.03 | 2 (NY Win 4) |
| `balanced` | 3 | 2 | 1.1 | 0.67/draw | +0.94 | 2 (Mega Millions) |
| `antibalanced` | 3 | 2 | 1.1 | 0.67/draw | +0.94 | 1 (Powerball) |
| `skiphit` | 12 | 6 | 4.3 | 0.50/draw | +0.88 | 1 (Powerball) |
| `llm-tuned` | 38 | 15 | 13.4 | 0.39/draw | +0.45 | 3 (NY Win 4) |
| `persistent` | 12 | 5 | 4.3 | 0.42/draw | +0.37 | 1 (NY Win 4) |
| `numerology` | 12 | 5 | 4.3 | 0.42/draw | +0.37 | 2 (NY Numbers (Pick 3)) |
| `birthday` | 3 | 1 | 1.1 | 0.33/draw | -0.08 | 1 (Mega Millions) |
| `benford` | 3 | 1 | 1.1 | 0.33/draw | -0.08 | 1 (Powerball) |
| `random` | 81 | 28 | 28.7 | 0.35/draw | -0.14 | 2 (Mega Millions) |
| `cold` | 81 | 28 | 28.7 | 0.35/draw | -0.14 | 3 (NY Win 4) |
| `delta` | 15 | 5 | 5.4 | 0.33/draw | -0.19 | 1 (Powerball) |
| `hot` | 81 | 27 | 28.7 | 0.33/draw | -0.34 | 2 (NY Numbers (Pick 3)) |
| `contrarian` | 12 | 3 | 4.3 | 0.25/draw | -0.66 | 1 (NY Numbers (Pick 3)) |
| `dreambook` | 9 | 2 | 3.2 | 0.22/draw | -0.71 | 1 (NY Win 4) |
| `llm-fewshot` | 71 | 21 | 25.2 | 0.30/draw | -0.88 | 2 (NY Win 4) |
| `unpopular` | 15 | 3 | 5.4 | 0.20/draw | -1.11 | 2 (Mega Millions) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-13 11:21 UTC</sub>
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
