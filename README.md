# 🎰 Lottery Guru

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-08-14

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Mega Millions**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `17` `43` `45` `63` `65` + `01` |
| `balanced` | `02` `25` `33` `44` `69` + `11` |
| `benford` | `16` `23` `35` `41` `55` + `13` |
| `birthday` | `03` `05` `12` `21` `26` + `15` |
| `cold` | `06` `08` `11` `28` `69` + `11` |
| `contrarian` | `01` `14` `51` `57` `65` + `23` |
| `delta` | `12` `33` `53` `63` `67` + `01` |
| `highest-frequency` | `20` `33` `37` `44` `63` + `11` |
| `hot` | `18` `42` `43` `49` `63` + `12` |
| `llm-fewshot` | `09` `20` `37` `44` `52` + `12` |
| `llm-tuned` | `01` `03` `11` `33` `46` + `13` |
| `moonphase` | `15` `19` `33` `49` `52` + `09` |
| `numerology` | `04` `10` `12` `20` `24` + `03` |
| `persistent` | `01` `09` `37` `38` `39` + `22` |
| `random` | `05` `18` `19` `31` `37` + `11` |
| `skiphit` | `20` `30` `32` `44` `68` + `14` |
| `unpopular` | `35` `38` `42` `67` `70` + `19` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `6` `5` |
| `contrarian` | `1` `9` `8` |
| `dreambook` | `1` `9` `1` |
| `highest-frequency` | `1` `9` `8` |
| `hot` | `8` `5` `3` |
| `llm-fewshot` | `8` `4` `7` |
| `llm-tuned` | `4` `9` `6` |
| `moonphase` | `8` `7` `1` |
| `numerology` | `1` `1` `7` |
| `persistent` | `4` `3` `3` |
| `positional` | `6` `4` `0` |
| `random` | `7` `2` `5` |
| `skiphit` | `1` `2` `8` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `6` `5` |
| `contrarian` | `4` `9` `7` |
| `dreambook` | `1` `6` `2` |
| `highest-frequency` | `1` `2` `3` |
| `hot` | `8` `5` `3` |
| `llm-fewshot` | `0` `9` `3` |
| `llm-tuned` | `1` `8` `4` |
| `moonphase` | `3` `0` `4` |
| `numerology` | `1` `1` `7` |
| `persistent` | `4` `3` `3` |
| `positional` | `7` `4` `8` |
| `random` | `6` `2` `7` |
| `skiphit` | `1` `2` `8` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `7` `0` `5` |
| `contrarian` | `3` `4` `6` `6` |
| `dreambook` | `8` `7` `5` `1` |
| `highest-frequency` | `1` `4` `6` `5` |
| `hot` | `6` `8` `5` `9` |
| `llm-fewshot` | `9` `9` `7` `9` |
| `llm-tuned` | `6` `6` `4` `5` |
| `moonphase` | `2` `4` `6` `2` |
| `numerology` | `1` `1` `7` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `1` `8` `6` `7` |
| `random` | `2` `4` `1` `7` |
| `skiphit` | `3` `6` `6` `6` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `7` `0` `5` |
| `contrarian` | `3` `4` `5` `6` |
| `dreambook` | `7` `4` `2` `3` |
| `highest-frequency` | `6` `4` `5` `5` |
| `hot` | `6` `8` `5` `9` |
| `llm-fewshot` | `6` `0` `8` `5` |
| `llm-tuned` | `0` `3` `9` `2` |
| `moonphase` | `0` `4` `8` `8` |
| `numerology` | `1` `1` `7` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `5` `0` `1` `6` |
| `random` | `6` `9` `4` `1` |
| `skiphit` | `9` `9` `6` `6` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `16` `20` `25` `30` `35` |
| `balanced` | `06` `19` `24` `27` `33` |
| `benford` | `05` `14` `16` `26` `33` |
| `birthday` | `06` `12` `15` `16` `27` |
| `cold` | `13` `14` `26` `31` `32` |
| `contrarian` | `06` `14` `20` `27` `29` |
| `delta` | `09` `11` `17` `30` `32` |
| `highest-frequency` | `14` `16` `26` `27` `31` |
| `hot` | `05` `16` `18` `26` `34` |
| `llm-fewshot` | `01` `27` `28` `30` `31` |
| `llm-tuned` | `01` `11` `17` `23` `28` |
| `moonphase` | `03` `06` `09` `26` `31` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `02` `14` `17` `19` `31` |
| `skiphit` | `01` `04` `15` `19` `27` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `18` `19` `25` `31` `36` |
| `balanced` | `02` `04` `23` `28` `33` |
| `benford` | `04` `11` `17` `29` `36` |
| `birthday` | `06` `07` `08` `12` `22` |
| `cold` | `04` `09` `22` `26` `30` |
| `contrarian` | `06` `08` `15` `18` `33` |
| `delta` | `06` `10` `17` `20` `29` |
| `highest-frequency` | `05` `06` `18` `22` `36` |
| `hot` | `05` `12` `14` `18` `24` |
| `llm-fewshot` | `05` `11` `20` `22` `23` |
| `llm-tuned` | `06` `07` `11` `23` `36` |
| `moonphase` | `06` `15` `16` `26` `28` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `01` `05` `06` `14` `27` |
| `skiphit` | `05` `18` `25` `27` `29` |

**FL Jackpot Triple Play**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `06` `12` `18` `22` `24` `44` |
| `balanced` | `07` `16` `30` `35` `37` `40` |
| `benford` | `05` `12` `15` `29` `34` `41` |
| `birthday` | `01` `02` `04` `05` `12` `14` |
| `cold` | `03` `04` `08` `27` `38` `39` |
| `contrarian` | `03` `09` `15` `20` `28` `37` |
| `delta` | `04` `08` `19` `23` `25` `33` |
| `highest-frequency` | `04` `09` `12` `16` `19` `34` |
| `hot` | `07` `16` `18` `19` `21` `34` |
| `llm-fewshot` | `05` `06` `13` `32` `35` `40` |
| `llm-tuned` | `09` `25` `32` `39` `44` `46` |
| `moonphase` | `12` `16` `19` `24` `29` `42` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `01` `04` `10` `18` `21` `29` |
| `random` | `01` `07` `10` `12` `20` `33` |
| `skiphit` | `09` `11` `28` `32` `40` `41` |
| `unpopular` | `16` `23` `34` `38` `43` `45` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `5` |
| `contrarian` | `3` `0` |
| `dreambook` | `5` `7` |
| `highest-frequency` | `4` `7` |
| `hot` | `4` `5` |
| `llm-fewshot` | `6` `7` |
| `llm-tuned` | `5` `9` |
| `moonphase` | `7` `7` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `8` `2` |
| `random` | `4` `4` |
| `skiphit` | `4` `9` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `4` |
| `contrarian` | `5` `2` |
| `dreambook` | `4` `0` |
| `highest-frequency` | `0` `6` |
| `hot` | `4` `5` |
| `llm-fewshot` | `0` `2` |
| `llm-tuned` | `3` `5` |
| `moonphase` | `1` `7` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `9` `0` |
| `random` | `0` `6` |
| `skiphit` | `5` `6` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `9` `0` |
| `contrarian` | `0` `8` `0` |
| `dreambook` | `0` `6` `2` |
| `highest-frequency` | `0` `1` `0` |
| `hot` | `0` `7` `1` |
| `llm-fewshot` | `0` `3` `7` |
| `llm-tuned` | `6` `9` `3` |
| `moonphase` | `9` `1` `9` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `2` `7` `0` |
| `random` | `3` `3` `9` |
| `skiphit` | `2` `4` `1` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `1` `6` |
| `contrarian` | `6` `7` `4` |
| `dreambook` | `1` `6` `2` |
| `highest-frequency` | `1` `7` `2` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `1` `8` `2` |
| `llm-tuned` | `2` `4` `8` |
| `moonphase` | `1` `2` `6` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `3` `7` `5` |
| `random` | `9` `7` `9` |
| `skiphit` | `1` `3` `2` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `4` `1` `8` |
| `contrarian` | `0` `7` `5` `4` |
| `dreambook` | `9` `8` `6` `4` |
| `highest-frequency` | `9` `1` `6` `8` |
| `hot` | `6` `0` `9` `5` |
| `llm-fewshot` | `3` `5` `0` `9` |
| `llm-tuned` | `7` `1` `4` `4` |
| `moonphase` | `6` `6` `9` `8` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `4` `2` `8` `7` |
| `random` | `9` `8` `5` `0` |
| `skiphit` | `9` `5` `3` `8` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `6` `1` `2` |
| `contrarian` | `6` `2` `7` `7` |
| `dreambook` | `9` `6` `0` `2` |
| `highest-frequency` | `2` `2` `7` `2` |
| `hot` | `9` `8` `7` `6` |
| `llm-fewshot` | `7` `2` `5` `3` |
| `llm-tuned` | `8` `3` `0` `7` |
| `moonphase` | `4` `7` `7` `2` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `2` `8` `4` `1` |
| `random` | `0` `2` `6` `2` |
| `skiphit` | `2` `5` `9` `0` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `5` `2` `6` `0` |
| `contrarian` | `3` `4` `7` `1` `9` |
| `dreambook` | `5` `7` `5` `6` `2` |
| `highest-frequency` | `4` `4` `7` `6` `9` |
| `hot` | `4` `2` `7` `3` `0` |
| `llm-fewshot` | `7` `3` `9` `7` `9` |
| `llm-tuned` | `6` `4` `8` `4` `9` |
| `moonphase` | `8` `4` `3` `2` `7` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `4` `7` `7` `6` `8` |
| `random` | `4` `2` `0` `0` `3` |
| `skiphit` | `3` `9` `2` `2` `5` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `2` `0` `4` `1` |
| `contrarian` | `1` `7` `6` `0` `2` |
| `dreambook` | `9` `6` `6` `7` `5` |
| `highest-frequency` | `1` `5` `3` `4` `4` |
| `hot` | `2` `5` `3` `8` `6` |
| `llm-fewshot` | `9` `8` `8` `5` `2` |
| `llm-tuned` | `6` `5` `7` `1` `3` |
| `moonphase` | `1` `7` `0` `4` `4` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `3` `4` `8` `4` `6` |
| `random` | `6` `3` `3` `5` `3` |
| `skiphit` | `0` `5` `3` `4` `2` |

<sub>Updated 2026-08-14 11:20 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**610** predictions scored across **20** days. Combined, they've hit **232** numbers where pure chance predicts **215.7** (z = **+1.17**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 48 | 27 | 16.9 | 0.56/draw | +2.58 | 2 (Mega Millions) |
| `skiphit` | 15 | 8 | 5.3 | 0.53/draw | +1.25 | 1 (Powerball) |
| `persistent` | 15 | 8 | 5.3 | 0.53/draw | +1.25 | 2 (NY Numbers (Pick 3)) |
| `moonphase` | 15 | 8 | 5.3 | 0.53/draw | +1.25 | 2 (NY Win 4) |
| `balanced` | 3 | 2 | 1.1 | 0.67/draw | +0.94 | 2 (Mega Millions) |
| `antibalanced` | 3 | 2 | 1.1 | 0.67/draw | +0.94 | 1 (Powerball) |
| `positional` | 69 | 28 | 24.3 | 0.41/draw | +0.79 | 2 (NY Win 4) |
| `numerology` | 15 | 7 | 5.3 | 0.47/draw | +0.79 | 2 (NY Numbers (Pick 3)) |
| `llm-tuned` | 38 | 15 | 13.4 | 0.39/draw | +0.45 | 3 (NY Win 4) |
| `contrarian` | 15 | 6 | 5.3 | 0.40/draw | +0.33 | 1 (NY Numbers (Pick 3)) |
| `birthday` | 3 | 1 | 1.1 | 0.33/draw | -0.08 | 1 (Mega Millions) |
| `benford` | 3 | 1 | 1.1 | 0.33/draw | -0.08 | 1 (Powerball) |
| `random` | 84 | 29 | 29.7 | 0.35/draw | -0.14 | 2 (Mega Millions) |
| `cold` | 84 | 29 | 29.7 | 0.35/draw | -0.14 | 3 (NY Win 4) |
| `delta` | 15 | 5 | 5.4 | 0.33/draw | -0.19 | 1 (Powerball) |
| `hot` | 84 | 28 | 29.7 | 0.33/draw | -0.33 | 2 (NY Numbers (Pick 3)) |
| `dreambook` | 12 | 3 | 4.2 | 0.25/draw | -0.62 | 1 (NY Win 4) |
| `llm-fewshot` | 74 | 22 | 26.2 | 0.30/draw | -0.86 | 2 (NY Win 4) |
| `unpopular` | 15 | 3 | 5.4 | 0.20/draw | -1.11 | 2 (Mega Millions) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-14 11:20 UTC</sub>
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
