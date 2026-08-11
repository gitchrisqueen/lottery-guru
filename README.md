# 🎰 Lottery Guru

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-08-11

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Mega Millions**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `03` `04` `09` `12` `65` + `10` |
| `balanced` | `01` `20` `56` `59` `61` + `22` |
| `benford` | `16` `19` `26` `39` `45` + `04` |
| `birthday` | `01` `02` `03` `05` `26` + `09` |
| `cold` | `06` `08` `11` `28` `69` + `11` |
| `contrarian` | `17` `18` `55` `57` `65` + `21` |
| `delta` | `12` `15` `24` `29` `38` + `07` |
| `highest-frequency` | `01` `03` `21` `26` `59` + `22` |
| `hot` | `21` `42` `49` `56` `63` + `12` |
| `llm-fewshot` | `13` `19` `21` `46` `63` + `12` |
| `llm-tuned` | `01` `33` `50` `59` `63` + `14` |
| `moonphase` | `21` `44` `45` `61` `62` + `03` |
| `numerology` | `09` `10` `12` `20` `24` + `08` |
| `persistent` | `01` `09` `37` `38` `39` + `22` |
| `random` | `03` `22` `26` `34` `69` + `20` |
| `skiphit` | `04` `20` `21` `26` `54` + `14` |
| `unpopular` | `39` `50` `59` `64` `67` + `23` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `6` `7` |
| `contrarian` | `8` `5` `1` |
| `dreambook` | `0` `2` `4` |
| `highest-frequency` | `8` `5` `4` |
| `hot` | `8` `5` `3` |
| `llm-fewshot` | `9` `0` `4` |
| `llm-tuned` | `1` `5` `8` |
| `moonphase` | `2` `9` `7` |
| `numerology` | `1` `1` `4` |
| `persistent` | `4` `3` `3` |
| `positional` | `5` `9` `5` |
| `random` | `7` `7` `8` |
| `skiphit` | `8` `5` `1` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `6` `3` |
| `contrarian` | `2` `5` `1` |
| `dreambook` | `4` `9` `9` |
| `highest-frequency` | `1` `5` `1` |
| `hot` | `8` `5` `3` |
| `llm-fewshot` | `9` `5` `1` |
| `llm-tuned` | `2` `8` `6` |
| `moonphase` | `1` `5` `5` |
| `numerology` | `1` `1` `4` |
| `persistent` | `4` `3` `3` |
| `positional` | `8` `3` `1` |
| `random` | `2` `4` `9` |
| `skiphit` | `1` `5` `1` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `1` `5` `6` |
| `contrarian` | `3` `3` `8` `0` |
| `dreambook` | `7` `2` `3` `1` |
| `highest-frequency` | `4` `1` `5` `0` |
| `hot` | `6` `2` `5` `8` |
| `llm-fewshot` | `4` `8` `4` `4` |
| `llm-tuned` | `1` `4` `1` `6` |
| `moonphase` | `0` `1` `5` `0` |
| `numerology` | `1` `1` `4` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `4` `1` `5` `4` |
| `random` | `4` `8` `3` `1` |
| `skiphit` | `3` `3` `2` `0` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `1` `6` `5` |
| `contrarian` | `2` `3` `7` `0` |
| `dreambook` | `9` `6` `0` `2` |
| `highest-frequency` | `2` `5` `4` `5` |
| `hot` | `6` `5` `2` `8` |
| `llm-fewshot` | `8` `0` `4` `9` |
| `llm-tuned` | `6` `4` `4` `3` |
| `moonphase` | `9` `4` `9` `7` |
| `numerology` | `1` `1` `4` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `2` `5` `4` `5` |
| `random` | `0` `5` `3` `5` |
| `skiphit` | `2` `3` `2` `0` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `05` `26` `31` `34` `36` |
| `balanced` | `01` `02` `21` `24` `26` |
| `benford` | `04` `15` `16` `20` `35` |
| `birthday` | `04` `05` `26` `28` `30` |
| `cold` | `10` `12` `18` `24` `30` |
| `contrarian` | `02` `07` `14` `28` `32` |
| `delta` | `04` `12` `19` `21` `25` |
| `highest-frequency` | `04` `05` `24` `25` `26` |
| `hot` | `15` `18` `21` `27` `33` |
| `llm-fewshot` | `03` `08` `13` `17` `25` |
| `llm-tuned` | `01` `02` `22` `25` `36` |
| `moonphase` | `07` `18` `24` `25` `33` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `04` `06` `07` `08` `15` |
| `skiphit` | `05` `10` `14` `23` `26` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `17` `23` `33` `35` |
| `balanced` | `09` `13` `14` `30` `36` |
| `benford` | `01` `04` `14` `29` `35` |
| `birthday` | `01` `07` `10` `12` `19` |
| `cold` | `07` `08` `17` `31` `33` |
| `contrarian` | `01` `21` `29` `31` `36` |
| `delta` | `05` `07` `11` `24` `32` |
| `highest-frequency` | `01` `07` `12` `17` `29` |
| `hot` | `07` `16` `18` `29` `34` |
| `llm-fewshot` | `03` `10` `25` `26` `27` |
| `llm-tuned` | `12` `17` `18` `29` `32` |
| `moonphase` | `06` `13` `20` `29` `35` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `07` `12` `15` `17` `32` |
| `skiphit` | `02` `18` `29` `30` `31` |

**FL Jackpot Triple Play**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `27` `28` `29` `35` `44` `45` |
| `balanced` | `02` `11` `18` `23` `27` `42` |
| `benford` | `03` `05` `16` `18` `29` `44` |
| `birthday` | `04` `05` `06` `07` `19` `30` |
| `cold` | `06` `08` `09` `13` `20` `42` |
| `contrarian` | `17` `21` `24` `27` `33` `38` |
| `delta` | `08` `11` `18` `21` `23` `35` |
| `highest-frequency` | `08` `18` `21` `27` `29` `44` |
| `hot` | `08` `16` `21` `28` `29` `40` |
| `llm-fewshot` | `03` `12` `23` `27` `34` `42` |
| `llm-tuned` | `09` `20` `26` `29` `32` `40` |
| `moonphase` | `15` `19` `26` `35` `36` `44` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `01` `04` `10` `18` `21` `29` |
| `random` | `09` `17` `24` `27` `38` `40` |
| `skiphit` | `07` `08` `14` `22` `25` `39` |
| `unpopular` | `13` `31` `33` `36` `39` `44` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `5` |
| `contrarian` | `7` `3` |
| `dreambook` | `7` `4` |
| `highest-frequency` | `7` `1` |
| `hot` | `8` `9` |
| `llm-fewshot` | `7` `8` |
| `llm-tuned` | `5` `5` |
| `moonphase` | `3` `4` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `4` `0` |
| `random` | `1` `7` |
| `skiphit` | `8` `2` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `2` |
| `contrarian` | `7` `7` |
| `dreambook` | `9` `2` |
| `highest-frequency` | `1` `7` |
| `hot` | `9` `7` |
| `llm-fewshot` | `0` `8` |
| `llm-tuned` | `4` `6` |
| `moonphase` | `6` `4` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `7` `9` |
| `random` | `1` `8` |
| `skiphit` | `2` `5` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `2` `4` |
| `contrarian` | `9` `3` `5` |
| `dreambook` | `7` `3` `0` |
| `highest-frequency` | `8` `2` `5` |
| `hot` | `3` `2` `9` |
| `llm-fewshot` | `4` `8` `5` |
| `llm-tuned` | `2` `4` `7` |
| `moonphase` | `4` `6` `5` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `7` `9` `3` |
| `random` | `0` `2` `9` |
| `skiphit` | `8` `0` `2` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `0` `4` |
| `contrarian` | `1` `7` `8` |
| `dreambook` | `5` `2` `3` |
| `highest-frequency` | `1` `4` `0` |
| `hot` | `9` `4` `0` |
| `llm-fewshot` | `9` `1` `7` |
| `llm-tuned` | `1` `3` `6` |
| `moonphase` | `6` `8` `9` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `5` `7` `9` |
| `random` | `2` `0` `5` |
| `skiphit` | `1` `4` `0` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `1` `9` `0` |
| `contrarian` | `8` `7` `3` `8` |
| `dreambook` | `2` `6` `6` `0` |
| `highest-frequency` | `3` `1` `4` `5` |
| `hot` | `3` `9` `4` `5` |
| `llm-fewshot` | `3` `4` `0` `0` |
| `llm-tuned` | `6` `5` `5` `1` |
| `moonphase` | `9` `7` `0` `8` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `3` `1` `7` `9` |
| `random` | `5` `7` `4` `8` |
| `skiphit` | `1` `8` `2` `9` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `3` `9` `4` |
| `contrarian` | `6` `1` `1` `5` |
| `dreambook` | `6` `4` `5` `5` |
| `highest-frequency` | `6` `4` `5` `5` |
| `hot` | `4` `6` `5` `1` |
| `llm-fewshot` | `6` `6` `5` `1` |
| `llm-tuned` | `8` `9` `5` `9` |
| `moonphase` | `8` `9` `2` `4` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `3` `8` `5` `8` |
| `random` | `5` `7` `6` `3` |
| `skiphit` | `4` `4` `3` `4` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `6` `9` `5` `2` |
| `contrarian` | `0` `7` `5` `5` `9` |
| `dreambook` | `0` `0` `1` `2` `0` |
| `highest-frequency` | `3` `1` `1` `5` `3` |
| `hot` | `6` `8` `4` `3` `7` |
| `llm-fewshot` | `5` `2` `1` `1` `3` |
| `llm-tuned` | `7` `6` `1` `2` `9` |
| `moonphase` | `3` `7` `0` `3` `2` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `2` `4` `1` `4` `7` |
| `random` | `3` `2` `6` `7` `3` |
| `skiphit` | `3` `3` `5` `2` `3` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `1` `6` `9` `5` |
| `contrarian` | `9` `7` `4` `8` `2` |
| `dreambook` | `1` `7` `1` `9` `2` |
| `highest-frequency` | `5` `2` `2` `8` `4` |
| `hot` | `5` `9` `2` `7` `0` |
| `llm-fewshot` | `3` `2` `0` `2` `4` |
| `llm-tuned` | `0` `2` `5` `2` `4` |
| `moonphase` | `2` `9` `2` `8` `1` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `2` `0` `2` `4` `6` |
| `random` | `5` `8` `5` `8` `3` |
| `skiphit` | `9` `2` `3` `6` `3` |

<sub>Updated 2026-08-11 11:57 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**475** predictions scored across **17** days. Combined, they've hit **173** numbers where pure chance predicts **168.1** (z = **+0.40**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 38 | 21 | 13.4 | 0.55/draw | +2.18 | 2 (Mega Millions) |
| `antibalanced` | 1 | 1 | 0.4 | 1.00/draw | +1.13 | 1 (Powerball) |
| `positional` | 61 | 26 | 21.5 | 0.43/draw | +1.02 | 2 (NY Win 4) |
| `llm-tuned` | 31 | 13 | 10.9 | 0.42/draw | +0.66 | 3 (NY Win 4) |
| `persistent` | 5 | 2 | 1.8 | 0.40/draw | +0.19 | 1 (NY Win 4) |
| `moonphase` | 5 | 2 | 1.8 | 0.40/draw | +0.19 | 1 (NY Numbers (Pick 3)) |
| `random` | 74 | 27 | 26.2 | 0.36/draw | +0.17 | 2 (Mega Millions) |
| `cold` | 74 | 27 | 26.2 | 0.36/draw | +0.17 | 3 (NY Win 4) |
| `hot` | 74 | 26 | 26.2 | 0.35/draw | -0.04 | 2 (NY Numbers (Pick 3)) |
| `delta` | 13 | 4 | 4.7 | 0.31/draw | -0.34 | 1 (Powerball) |
| `skiphit` | 5 | 1 | 1.8 | 0.20/draw | -0.61 | 1 (Powerball) |
| `numerology` | 5 | 1 | 1.8 | 0.20/draw | -0.61 | 1 (NY Numbers (Pick 3)) |
| `birthday` | 1 | 0 | 0.4 | 0.00/draw | -0.64 | 0 |
| `balanced` | 1 | 0 | 0.4 | 0.00/draw | -0.64 | 0 |
| `benford` | 1 | 0 | 0.4 | 0.00/draw | -0.64 | 0 |
| `llm-fewshot` | 64 | 19 | 22.7 | 0.30/draw | -0.81 | 2 (NY Win 4) |
| `unpopular` | 13 | 3 | 4.7 | 0.23/draw | -0.83 | 2 (Mega Millions) |
| `dreambook` | 4 | 0 | 1.4 | 0.00/draw | -1.25 | 0 |
| `contrarian` | 5 | 0 | 1.8 | 0.00/draw | -1.40 | 0 |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-11 11:57 UTC</sub>
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
