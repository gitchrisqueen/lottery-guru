# 🎰 Lottery Guru

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-08-20

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `1` |
| `contrarian` | `2` `8` `2` |
| `dreambook` | `0` `8` `5` |
| `highest-frequency` | `4` `8` `2` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `4` `0` `1` |
| `moonphase` | `0` `4` `3` |
| `numerology` | `1` `1` `4` |
| `persistent` | `4` `3` `3` |
| `positional` | `1` `7` `5` |
| `random` | `3` `3` `6` |
| `skiphit` | `4` `0` `0` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `1` |
| `contrarian` | `2` `0` `2` |
| `dreambook` | `2` `1` `5` |
| `highest-frequency` | `6` `0` `3` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `6` `9` `4` |
| `moonphase` | `6` `0` `9` |
| `numerology` | `1` `1` `4` |
| `persistent` | `4` `3` `3` |
| `positional` | `2` `1` `6` |
| `random` | `3` `2` `3` |
| `skiphit` | `4` `0` `0` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `0` `6` `9` |
| `contrarian` | `5` `5` `3` `3` |
| `dreambook` | `1` `0` `4` `0` |
| `highest-frequency` | `1` `8` `3` `5` |
| `hot` | `8` `3` `6` `5` |
| `llm-fewshot` | `2` `8` `3` `3` |
| `moonphase` | `9` `8` `4` `1` |
| `numerology` | `1` `1` `4` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `2` `3` `6` `5` |
| `random` | `1` `6` `3` `3` |
| `skiphit` | `9` `8` `3` `3` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `0` `6` `2` |
| `contrarian` | `5` `8` `1` `3` |
| `dreambook` | `3` `6` `9` `3` |
| `highest-frequency` | `1` `8` `6` `5` |
| `hot` | `8` `3` `6` `5` |
| `llm-fewshot` | `1` `8` `3` `1` |
| `moonphase` | `2` `8` `0` `4` |
| `numerology` | `1` `1` `4` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `2` `8` `8` `1` |
| `random` | `7` `9` `6` `1` |
| `skiphit` | `1` `8` `3` `4` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `12` `13` `32` `33` `35` |
| `balanced` | `05` `09` `22` `24` `26` |
| `benford` | `02` `03` `04` `10` `11` |
| `birthday` | `03` `09` `12` `21` `26` |
| `cold` | `10` `12` `22` `26` `35` |
| `contrarian` | `01` `08` `10` `12` `16` |
| `delta` | `04` `07` `12` `16` `31` |
| `highest-frequency` | `03` `10` `12` `26` `35` |
| `hot` | `02` `09` `11` `28` `35` |
| `llm-fewshot` | `07` `17` `22` `25` `33` |
| `moonphase` | `12` `14` `15` `35` `36` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `03` `08` `20` `21` `26` |
| `skiphit` | `03` `04` `18` `23` `26` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `02` `04` `14` `16` `19` |
| `balanced` | `12` `17` `21` `23` `34` |
| `benford` | `01` `04` `16` `26` `32` |
| `birthday` | `08` `10` `17` `18` `28` |
| `cold` | `01` `03` `07` `17` `18` |
| `contrarian` | `13` `18` `26` `30` `34` |
| `delta` | `10` `15` `21` `26` `31` |
| `highest-frequency` | `04` `12` `14` `18` `26` |
| `hot` | `03` `04` `19` `31` `32` |
| `llm-fewshot` | `17` `18` `20` `30` `32` |
| `moonphase` | `02` `12` `14` `18` `24` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `04` `12` `16` `21` `26` |
| `skiphit` | `12` `14` `15` `24` `35` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `3` |
| `contrarian` | `7` `4` |
| `dreambook` | `9` `7` |
| `highest-frequency` | `6` `1` |
| `hot` | `6` `1` |
| `llm-fewshot` | `0` `0` |
| `moonphase` | `6` `3` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `2` `4` |
| `random` | `5` `2` |
| `skiphit` | `5` `9` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `1` |
| `contrarian` | `1` `0` |
| `dreambook` | `0` `4` |
| `highest-frequency` | `1` `1` |
| `hot` | `1` `5` |
| `llm-fewshot` | `4` `4` |
| `moonphase` | `6` `6` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `3` `2` |
| `random` | `4` `9` |
| `skiphit` | `5` `1` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `9` `0` |
| `contrarian` | `7` `4` `3` |
| `dreambook` | `9` `8` `6` |
| `highest-frequency` | `7` `2` `3` |
| `hot` | `7` `2` `0` |
| `llm-fewshot` | `2` `2` `2` |
| `moonphase` | `0` `1` `8` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `6` `6` `3` |
| `random` | `2` `2` `6` |
| `skiphit` | `8` `3` `9` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `6` `0` |
| `contrarian` | `1` `0` `9` |
| `dreambook` | `2` `7` `8` |
| `highest-frequency` | `3` `6` `8` |
| `hot` | `3` `4` `7` |
| `llm-fewshot` | `3` `6` `8` |
| `moonphase` | `3` `2` `8` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `2` `4` `2` |
| `random` | `8` `0` `5` |
| `skiphit` | `1` `6` `5` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `7` `6` `9` |
| `contrarian` | `2` `4` `7` `6` |
| `dreambook` | `8` `7` `5` `1` |
| `highest-frequency` | `7` `1` `6` `1` |
| `hot` | `7` `0` `2` `1` |
| `llm-fewshot` | `3` `8` `3` `2` |
| `moonphase` | `1` `3` `0` `7` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `8` `3` `8` `3` |
| `random` | `7` `1` `7` `9` |
| `skiphit` | `4` `5` `6` `6` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `0` `9` `3` |
| `contrarian` | `5` `5` `2` `4` |
| `dreambook` | `3` `7` `8` `0` |
| `highest-frequency` | `3` `8` `8` `5` |
| `hot` | `3` `6` `8` `7` |
| `llm-fewshot` | `7` `4` `6` `1` |
| `moonphase` | `9` `3` `8` `6` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `1` `8` `2` `7` |
| `random` | `6` `8` `8` `5` |
| `skiphit` | `6` `8` `3` `2` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `8` `9` `1` `7` |
| `contrarian` | `1` `6` `0` `6` `3` |
| `dreambook` | `7` `3` `0` `9` `1` |
| `highest-frequency` | `5` `1` `9` `8` `4` |
| `hot` | `6` `9` `8` `1` `2` |
| `llm-fewshot` | `1` `1` `4` `3` `7` |
| `moonphase` | `9` `0` `5` `8` `4` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `4` `2` `3` `8` `6` |
| `random` | `5` `4` `8` `5` `8` |
| `skiphit` | `3` `0` `9` `8` `5` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `5` `6` `0` `2` |
| `contrarian` | `4` `8` `7` `5` `6` |
| `dreambook` | `1` `8` `3` `6` `2` |
| `highest-frequency` | `1` `1` `1` `5` `2` |
| `hot` | `2` `6` `0` `3` `4` |
| `llm-fewshot` | `8` `5` `9` `7` `6` |
| `moonphase` | `1` `7` `3` `3` `5` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `2` `3` `2` `9` `2` |
| `random` | `1` `6` `1` `1` `2` |
| `skiphit` | `7` `2` `2` `1` `1` |

<sub>Updated 2026-08-20 10:56 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**951** predictions scored across **26** days. Combined, they've hit **374** numbers where pure chance predicts **336.0** (z = **+2.20**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 73 | 40 | 25.7 | 0.55/draw | +2.97 | 2 (Mega Millions) |
| `contrarian` | 40 | 23 | 14.1 | 0.57/draw | +2.51 | 2 (NY Numbers (Pick 3)) |
| `benford` | 8 | 6 | 2.9 | 0.75/draw | +1.96 | 3 (Mega Millions) |
| `persistent` | 40 | 19 | 14.1 | 0.47/draw | +1.39 | 2 (NY Numbers (Pick 3)) |
| `birthday` | 8 | 5 | 2.9 | 0.62/draw | +1.33 | 2 (Powerball) |
| `skiphit` | 40 | 18 | 14.1 | 0.45/draw | +1.10 | 2 (NY Win 4) |
| `numerology` | 40 | 18 | 14.1 | 0.45/draw | +1.10 | 2 (NY Numbers (Pick 3)) |
| `llm-tuned` | 59 | 25 | 20.8 | 0.42/draw | +0.96 | 3 (NY Win 4) |
| `positional` | 89 | 36 | 31.3 | 0.40/draw | +0.89 | 2 (NY Win 4) |
| `random` | 109 | 42 | 38.5 | 0.39/draw | +0.60 | 2 (Mega Millions) |
| `hot` | 109 | 41 | 38.5 | 0.38/draw | +0.42 | 3 (NY Numbers (Pick 3)) |
| `delta` | 20 | 8 | 7.2 | 0.40/draw | +0.32 | 1 (Powerball) |
| `balanced` | 8 | 3 | 2.9 | 0.38/draw | +0.07 | 2 (Mega Millions) |
| `moonphase` | 40 | 14 | 14.1 | 0.35/draw | -0.02 | 2 (NY Win 4) |
| `antibalanced` | 8 | 2 | 2.9 | 0.25/draw | -0.56 | 1 (Powerball) |
| `cold` | 109 | 35 | 38.5 | 0.32/draw | -0.60 | 3 (NY Win 4) |
| `dreambook` | 32 | 9 | 11.2 | 0.28/draw | -0.69 | 1 (NY Win 4) |
| `unpopular` | 20 | 4 | 7.2 | 0.20/draw | -1.28 | 2 (Mega Millions) |
| `llm-fewshot` | 99 | 26 | 35.0 | 0.26/draw | -1.61 | 2 (NY Win 4) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-20 10:56 UTC</sub>
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
