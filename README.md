# 🎰 Lottery Guru

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-08-17

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Powerball**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `18` `46` `59` `67` `68` + `10` |
| `balanced` | `13` `20` `21` `49` `68` + `03` |
| `benford` | `10` `18` `21` `37` `59` + `18` |
| `birthday` | `02` `03` `04` `07` `12` + `02` |
| `cold` | `11` `15` `23` `33` `51` + `19` |
| `contrarian` | `04` `05` `54` `64` `67` + `10` |
| `delta` | `07` `08` `11` `27` `39` + `02` |
| `highest-frequency` | `13` `21` `23` `59` `64` + `10` |
| `hot` | `06` `21` `48` `63` `64` + `01` |
| `llm-fewshot` | `27` `28` `46` `53` `61` + `08` |
| `llm-tuned` | `01` `13` `14` `40` `52` + `21` |
| `moonphase` | `01` `46` `50` `51` `59` + `08` |
| `numerology` | `08` `10` `12` `20` `24` + `07` |
| `persistent` | `13` `21` `23` `32` `66` + `01` |
| `random` | `02` `15` `23` `45` `69` + `03` |
| `skiphit` | `05` `08` `14` `63` `64` + `09` |
| `unpopular` | `32` `41` `47` `59` `61` + `17` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `1` |
| `contrarian` | `4` `2` `5` |
| `dreambook` | `6` `2` `9` |
| `highest-frequency` | `4` `5` `2` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `3` `4` `2` |
| `llm-tuned` | `5` `5` `8` |
| `moonphase` | `0` `9` `4` |
| `numerology` | `1` `1` `1` |
| `persistent` | `4` `3` `3` |
| `positional` | `2` `0` `8` |
| `random` | `1` `5` `2` |
| `skiphit` | `4` `8` `9` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `1` |
| `contrarian` | `5` `8` `3` |
| `dreambook` | `2` `0` `5` |
| `highest-frequency` | `4` `5` `1` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `7` `4` `6` |
| `llm-tuned` | `2` `5` `3` |
| `moonphase` | `0` `2` `1` |
| `numerology` | `1` `1` `1` |
| `persistent` | `4` `3` `3` |
| `positional` | `7` `6` `5` |
| `random` | `4` `5` `4` |
| `skiphit` | `4` `8` `9` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `9` `2` `6` |
| `contrarian` | `8` `8` `3` `6` |
| `dreambook` | `3` `4` `8` `7` |
| `highest-frequency` | `1` `8` `0` `6` |
| `hot` | `6` `8` `3` `5` |
| `llm-fewshot` | `1` `3` `8` `3` |
| `llm-tuned` | `9` `7` `0` `6` |
| `moonphase` | `4` `6` `1` `4` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `9` `1` `0` `0` |
| `random` | `0` `7` `9` `6` |
| `skiphit` | `1` `8` `0` `7` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `2` `9` `6` |
| `contrarian` | `8` `0` `3` `7` |
| `dreambook` | `0` `4` `8` `0` |
| `highest-frequency` | `1` `1` `0` `5` |
| `hot` | `6` `8` `3` `5` |
| `llm-fewshot` | `9` `9` `0` `4` |
| `llm-tuned` | `1` `6` `4` `5` |
| `moonphase` | `5` `1` `0` `5` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `1` `1` `2` `3` |
| `random` | `1` `6` `6` `6` |
| `skiphit` | `1` `8` `0` `4` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `03` `05` `23` `24` |
| `balanced` | `06` `07` `10` `25` `28` |
| `benford` | `04` `13` `19` `24` `35` |
| `birthday` | `06` `10` `11` `18` `30` |
| `cold` | `02` `28` `29` `30` `34` |
| `contrarian` | `10` `12` `33` `35` `36` |
| `delta` | `01` `04` `08` `21` `22` |
| `highest-frequency` | `01` `06` `10` `24` `25` |
| `hot` | `04` `09` `11` `23` `28` |
| `llm-fewshot` | `02` `19` `24` `29` `34` |
| `llm-tuned` | `01` `13` `20` `25` `27` |
| `moonphase` | `08` `10` `12` `33` `35` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `01` `03` `06` `13` `23` |
| `skiphit` | `02` `16` `25` `26` `34` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `02` `22` `26` `28` `34` |
| `balanced` | `02` `12` `13` `21` `36` |
| `benford` | `04` `17` `19` `22` `31` |
| `birthday` | `03` `06` `11` `15` `27` |
| `cold` | `07` `11` `22` `32` `35` |
| `contrarian` | `03` `10` `17` `30` `32` |
| `delta` | `12` `15` `25` `29` `35` |
| `highest-frequency` | `12` `22` `26` `32` `35` |
| `hot` | `05` `14` `26` `29` `32` |
| `llm-fewshot` | `03` `12` `19` `27` `35` |
| `llm-tuned` | `02` `17` `25` `26` `28` |
| `moonphase` | `19` `26` `32` `33` `35` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `06` `08` `24` `25` `27` |
| `skiphit` | `05` `20` `24` `31` `36` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `5` |
| `contrarian` | `7` `5` |
| `dreambook` | `1` `3` |
| `highest-frequency` | `1` `5` |
| `hot` | `1` `9` |
| `llm-fewshot` | `6` `3` |
| `llm-tuned` | `0` `5` |
| `moonphase` | `5` `7` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `3` `5` |
| `random` | `6` `8` |
| `skiphit` | `5` `7` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `9` |
| `contrarian` | `1` `2` |
| `dreambook` | `1` `6` |
| `highest-frequency` | `1` `1` |
| `hot` | `0` `9` |
| `llm-fewshot` | `0` `7` |
| `llm-tuned` | `2` `8` |
| `moonphase` | `2` `6` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `3` `0` |
| `random` | `8` `7` |
| `skiphit` | `5` `3` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `3` `0` |
| `contrarian` | `7` `7` `7` |
| `dreambook` | `5` `9` `2` |
| `highest-frequency` | `8` `4` `8` |
| `hot` | `8` `0` `7` |
| `llm-fewshot` | `8` `2` `8` |
| `llm-tuned` | `1` `8` `8` |
| `moonphase` | `6` `1` `5` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `5` `4` `9` |
| `random` | `1` `4` `4` |
| `skiphit` | `8` `4` `3` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `9` `3` |
| `contrarian` | `4` `1` `5` |
| `dreambook` | `9` `8` `0` |
| `highest-frequency` | `1` `1` `4` |
| `hot` | `5` `7` `3` |
| `llm-fewshot` | `6` `4` `2` |
| `llm-tuned` | `3` `9` `4` |
| `moonphase` | `6` `0` `7` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `1` `6` `6` |
| `random` | `9` `1` `2` |
| `skiphit` | `8` `2` `4` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `2` `5` `9` |
| `contrarian` | `2` `9` `5` `6` |
| `dreambook` | `6` `2` `7` `4` |
| `highest-frequency` | `3` `9` `5` `1` |
| `hot` | `1` `5` `8` `4` |
| `llm-fewshot` | `8` `3` `4` `9` |
| `llm-tuned` | `3` `5` `9` `6` |
| `moonphase` | `0` `7` `1` `1` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `5` `3` `6` `2` |
| `random` | `3` `9` `5` `1` |
| `skiphit` | `3` `9` `1` `1` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `4` `0` `7` |
| `contrarian` | `7` `7` `5` `9` |
| `dreambook` | `2` `4` `4` `7` |
| `highest-frequency` | `2` `4` `6` `7` |
| `hot` | `5` `8` `9` `2` |
| `llm-fewshot` | `8` `2` `4` `9` |
| `llm-tuned` | `2` `3` `9` `8` |
| `moonphase` | `3` `6` `6` `7` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `7` `1` `6` `0` |
| `random` | `6` `5` `7` `3` |
| `skiphit` | `6` `6` `8` `0` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `1` `3` `9` `6` |
| `contrarian` | `3` `2` `3` `4` `3` |
| `dreambook` | `6` `0` `3` `6` `6` |
| `highest-frequency` | `8` `1` `3` `9` `4` |
| `hot` | `8` `6` `3` `2` `1` |
| `llm-fewshot` | `8` `6` `4` `3` `4` |
| `llm-tuned` | `7` `5` `9` `0` `2` |
| `moonphase` | `3` `8` `1` `6` `2` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `9` `1` `8` `1` `8` |
| `random` | `2` `6` `6` `8` `0` |
| `skiphit` | `8` `7` `8` `9` `9` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `8` `1` `6` `2` |
| `contrarian` | `4` `3` `4` `5` `0` |
| `dreambook` | `2` `4` `4` `7` `4` |
| `highest-frequency` | `4` `8` `1` `5` `4` |
| `hot` | `1` `8` `0` `5` `9` |
| `llm-fewshot` | `2` `8` `0` `6` `8` |
| `llm-tuned` | `7` `8` `3` `6` `6` |
| `moonphase` | `9` `7` `7` `5` `6` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `4` `0` `3` `2` `1` |
| `random` | `6` `2` `1` `2` `7` |
| `skiphit` | `6` `0` `1` `9` `3` |

<sub>Updated 2026-08-17 10:59 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**770** predictions scored across **23** days. Combined, they've hit **297** numbers where pure chance predicts **272.1** (z = **+1.60**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 60 | 33 | 21.2 | 0.55/draw | +2.72 | 2 (Mega Millions) |
| `contrarian` | 27 | 17 | 9.5 | 0.63/draw | +2.57 | 2 (NY Numbers (Pick 3)) |
| `birthday` | 5 | 4 | 1.8 | 0.80/draw | +1.75 | 2 (Powerball) |
| `skiphit` | 27 | 14 | 9.5 | 0.52/draw | +1.54 | 2 (NY Win 4) |
| `moonphase` | 27 | 13 | 9.5 | 0.48/draw | +1.20 | 2 (NY Win 4) |
| `positional` | 79 | 33 | 27.8 | 0.42/draw | +1.04 | 2 (NY Win 4) |
| `benford` | 5 | 3 | 1.8 | 0.60/draw | +0.96 | 1 (Powerball) |
| `persistent` | 27 | 12 | 9.5 | 0.44/draw | +0.86 | 2 (NY Numbers (Pick 3)) |
| `llm-tuned` | 46 | 19 | 16.3 | 0.41/draw | +0.72 | 3 (NY Win 4) |
| `numerology` | 27 | 11 | 9.5 | 0.41/draw | +0.51 | 2 (NY Numbers (Pick 3)) |
| `balanced` | 5 | 2 | 1.8 | 0.40/draw | +0.16 | 2 (Mega Millions) |
| `antibalanced` | 5 | 2 | 1.8 | 0.40/draw | +0.16 | 1 (Powerball) |
| `delta` | 17 | 6 | 6.1 | 0.35/draw | -0.05 | 1 (Powerball) |
| `random` | 96 | 33 | 33.9 | 0.34/draw | -0.17 | 2 (Mega Millions) |
| `hot` | 96 | 33 | 33.9 | 0.34/draw | -0.17 | 2 (NY Numbers (Pick 3)) |
| `dreambook` | 22 | 6 | 7.7 | 0.27/draw | -0.65 | 1 (NY Win 4) |
| `cold` | 96 | 30 | 33.9 | 0.31/draw | -0.71 | 3 (NY Win 4) |
| `unpopular` | 17 | 3 | 6.1 | 0.18/draw | -1.35 | 2 (Mega Millions) |
| `llm-fewshot` | 86 | 23 | 30.4 | 0.27/draw | -1.42 | 2 (NY Win 4) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-17 10:59 UTC</sub>
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
