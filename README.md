# 🎰 Lottery Guru

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-08-12

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Powerball**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `24` `44` `56` `57` `69` + `14` |
| `balanced` | `28` `30` `37` `39` `65` + `15` |
| `benford` | `01` `13` `26` `31` `43` + `10` |
| `birthday` | `03` `06` `11` `16` `22` + `12` |
| `cold` | `11` `15` `23` `33` `51` + `09` |
| `contrarian` | `05` `06` `20` `54` `64` + `25` |
| `delta` | `45` `51` `52` `54` `67` + `05` |
| `highest-frequency` | `06` `11` `36` `56` `64` + `14` |
| `hot` | `06` `18` `21` `36` `64` + `14` |
| `llm-fewshot` | `06` `21` `33` `36` `42` + `03` |
| `llm-tuned` | `11` `16` `40` `56` `62` + `16` |
| `moonphase` | `11` `15` `56` `65` `66` + `24` |
| `numerology` | `10` `12` `20` `24` `36` + `11` |
| `persistent` | `13` `21` `23` `32` `66` + `01` |
| `random` | `06` `07` `22` `26` `36` + `24` |
| `skiphit` | `20` `27` `55` `59` `64` + `25` |
| `unpopular` | `34` `36` `43` `54` `61` + `09` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `6` `3` |
| `contrarian` | `5` `1` `7` |
| `dreambook` | `8` `4` `2` |
| `highest-frequency` | `1` `1` `3` |
| `hot` | `8` `5` `3` |
| `llm-fewshot` | `3` `7` `8` |
| `llm-tuned` | `1` `6` `9` |
| `moonphase` | `2` `2` `9` |
| `numerology` | `1` `1` `5` |
| `persistent` | `4` `3` `3` |
| `positional` | `3` `1` `6` |
| `random` | `2` `3` `6` |
| `skiphit` | `5` `9` `7` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `6` `3` |
| `contrarian` | `1` `1` `1` |
| `dreambook` | `3` `6` `9` |
| `highest-frequency` | `1` `5` `3` |
| `hot` | `8` `5` `3` |
| `llm-fewshot` | `3` `2` `3` |
| `llm-tuned` | `7` `8` `9` |
| `moonphase` | `0` `7` `8` |
| `numerology` | `1` `1` `5` |
| `persistent` | `4` `3` `3` |
| `positional` | `6` `5` `9` |
| `random` | `1` `9` `6` |
| `skiphit` | `5` `5` `7` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `1` `6` `5` |
| `contrarian` | `2` `9` `9` `0` |
| `dreambook` | `9` `7` `5` `0` |
| `highest-frequency` | `4` `7` `5` `5` |
| `hot` | `6` `5` `8` `2` |
| `llm-fewshot` | `5` `0` `5` `4` |
| `llm-tuned` | `4` `7` `9` `3` |
| `moonphase` | `9` `7` `2` `6` |
| `numerology` | `1` `1` `5` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `3` `5` `8` `6` |
| `random` | `0` `2` `7` `5` |
| `skiphit` | `2` `9` `2` `0` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `1` `5` `6` |
| `contrarian` | `2` `9` `2` `0` |
| `dreambook` | `2` `2` `9` `7` |
| `highest-frequency` | `2` `1` `5` `0` |
| `hot` | `6` `5` `2` `8` |
| `llm-fewshot` | `1` `1` `2` `4` |
| `llm-tuned` | `7` `5` `5` `6` |
| `moonphase` | `8` `1` `5` `2` |
| `numerology` | `1` `1` `5` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `9` `5` `8` `0` |
| `random` | `5` `0` `5` `8` |
| `skiphit` | `2` `9` `2` `0` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `11` `17` `31` `35` `36` |
| `balanced` | `08` `12` `21` `26` `33` |
| `benford` | `04` `18` `19` `25` `34` |
| `birthday` | `05` `08` `16` `18` `31` |
| `cold` | `03` `05` `11` `22` `28` |
| `contrarian` | `15` `20` `25` `26` `29` |
| `delta` | `08` `09` `23` `32` `36` |
| `highest-frequency` | `11` `22` `26` `29` `36` |
| `hot` | `02` `16` `23` `24` `36` |
| `llm-fewshot` | `09` `11` `13` `17` `22` |
| `llm-tuned` | `11` `12` `16` `18` `20` |
| `moonphase` | `03` `25` `27` `28` `30` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `07` `10` `11` `22` `29` |
| `skiphit` | `04` `06` `22` `23` `29` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `04` `05` `21` `23` |
| `balanced` | `03` `10` `14` `22` `23` |
| `benford` | `05` `11` `13` `29` `31` |
| `birthday` | `05` `08` `11` `30` `31` |
| `cold` | `05` `07` `22` `26` `27` |
| `contrarian` | `04` `11` `17` `27` `32` |
| `delta` | `12` `14` `24` `35` `36` |
| `highest-frequency` | `05` `07` `22` `24` `33` |
| `hot` | `07` `22` `24` `25` `33` |
| `llm-fewshot` | `08` `19` `31` `33` `34` |
| `llm-tuned` | `01` `10` `22` `27` `35` |
| `moonphase` | `01` `06` `16` `25` `33` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `03` `06` `18` `25` `33` |
| `skiphit` | `07` `08` `16` `26` `28` |

**Florida Lotto**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `06` `08` `17` `27` `44` |
| `balanced` | `05` `07` `22` `24` `34` `53` |
| `benford` | `01` `17` `23` `34` `41` `53` |
| `birthday` | `05` `08` `09` `11` `24` `31` |
| `cold` | `10` `12` `21` `37` `41` `48` |
| `contrarian` | `03` `17` `26` `27` `33` `40` |
| `delta` | `03` `09` `19` `21` `27` `32` |
| `highest-frequency` | `03` `05` `12` `24` `33` `34` |
| `hot` | `06` `11` `13` `24` `31` `39` |
| `llm-fewshot` | `03` `04` `07` `11` `31` `52` |
| `llm-tuned` | `14` `28` `30` `32` `41` `47` |
| `moonphase` | `02` `08` `12` `18` `47` `51` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `05` `10` `32` `33` `38` `50` |
| `random` | `01` `03` `04` `09` `16` `34` |
| `skiphit` | `03` `05` `22` `33` `40` `50` |
| `unpopular` | `21` `34` `43` `44` `47` `52` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `9` |
| `contrarian` | `6` `8` |
| `dreambook` | `2` `3` |
| `highest-frequency` | `1` `1` |
| `hot` | `7` `4` |
| `llm-fewshot` | `9` `1` |
| `llm-tuned` | `5` `6` |
| `moonphase` | `4` `6` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `1` `9` |
| `random` | `5` `6` |
| `skiphit` | `7` `7` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `2` |
| `contrarian` | `8` `3` |
| `dreambook` | `8` `7` |
| `highest-frequency` | `8` `1` |
| `hot` | `6` `1` |
| `llm-fewshot` | `6` `6` |
| `llm-tuned` | `7` `4` |
| `moonphase` | `7` `3` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `9` `4` |
| `random` | `6` `1` |
| `skiphit` | `1` `9` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `6` `5` |
| `contrarian` | `3` `8` `9` |
| `dreambook` | `4` `1` `5` |
| `highest-frequency` | `4` `1` `4` |
| `hot` | `2` `1` `6` |
| `llm-fewshot` | `9` `7` `3` |
| `llm-tuned` | `3` `3` `9` |
| `moonphase` | `2` `9` `7` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `8` `7` `4` |
| `random` | `4` `6` `1` |
| `skiphit` | `4` `7` `4` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `5` `7` |
| `contrarian` | `1` `4` `7` |
| `dreambook` | `4` `9` `4` |
| `highest-frequency` | `1` `1` `7` |
| `hot` | `0` `7` `5` |
| `llm-fewshot` | `3` `8` `1` |
| `llm-tuned` | `3` `3` `7` |
| `moonphase` | `4` `1` `4` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `5` `7` `2` |
| `random` | `0` `0` `7` |
| `skiphit` | `1` `8` `0` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `3` `1` `2` |
| `contrarian` | `2` `9` `4` `5` |
| `dreambook` | `0` `6` `3` `2` |
| `highest-frequency` | `1` `9` `1` `5` |
| `hot` | `6` `7` `1` `3` |
| `llm-fewshot` | `4` `7` `4` `6` |
| `llm-tuned` | `3` `2` `9` `5` |
| `moonphase` | `1` `7` `7` `1` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `9` `9` `2` `3` |
| `random` | `0` `5` `2` `5` |
| `skiphit` | `8` `9` `5` `6` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `4` `6` `5` |
| `contrarian` | `6` `7` `8` `9` |
| `dreambook` | `2` `2` `9` `7` |
| `highest-frequency` | `2` `4` `6` `5` |
| `hot` | `6` `1` `0` `2` |
| `llm-fewshot` | `0` `2` `1` `2` |
| `llm-tuned` | `7` `4` `6` `6` |
| `moonphase` | `8` `4` `8` `2` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `9` `6` `2` `3` |
| `random` | `5` `7` `4` `0` |
| `skiphit` | `8` `6` `0` `8` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `8` `5` `3` `6` |
| `contrarian` | `4` `5` `8` `9` `3` |
| `dreambook` | `5` `9` `5` `8` `2` |
| `highest-frequency` | `5` `9` `3` `4` `4` |
| `hot` | `6` `7` `4` `0` `3` |
| `llm-fewshot` | `3` `6` `3` `7` `4` |
| `llm-tuned` | `5` `9` `4` `1` `1` |
| `moonphase` | `6` `7` `9` `9` `4` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `2` `0` `6` `7` `2` |
| `random` | `4` `9` `0` `4` `3` |
| `skiphit` | `3` `8` `3` `4` `7` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `9` `0` `2` `4` |
| `contrarian` | `5` `8` `5` `0` `6` |
| `dreambook` | `2` `4` `9` `9` `1` |
| `highest-frequency` | `7` `4` `9` `4` `4` |
| `hot` | `3` `6` `8` `4` `7` |
| `llm-fewshot` | `6` `6` `8` `3` `2` |
| `llm-tuned` | `7` `3` `7` `2` `3` |
| `moonphase` | `7` `4` `9` `6` `3` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `7` `4` `2` `3` `0` |
| `random` | `9` `3` `0` `8` `0` |
| `skiphit` | `2` `7` `1` `1` `6` |

<sub>Updated 2026-08-12 12:04 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**531** predictions scored across **18** days. Combined, they've hit **201** numbers where pure chance predicts **187.2** (z = **+1.07**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 42 | 24 | 14.8 | 0.57/draw | +2.53 | 2 (Mega Millions) |
| `moonphase` | 9 | 6 | 3.1 | 0.67/draw | +1.72 | 2 (NY Win 4) |
| `balanced` | 2 | 2 | 0.7 | 1.00/draw | +1.61 | 2 (Mega Millions) |
| `skiphit` | 9 | 5 | 3.1 | 0.56/draw | +1.13 | 1 (Powerball) |
| `positional` | 64 | 27 | 22.5 | 0.42/draw | +1.00 | 2 (NY Win 4) |
| `llm-tuned` | 35 | 15 | 12.3 | 0.43/draw | +0.82 | 3 (NY Win 4) |
| `persistent` | 9 | 4 | 3.1 | 0.44/draw | +0.53 | 1 (NY Win 4) |
| `numerology` | 9 | 4 | 3.1 | 0.44/draw | +0.53 | 2 (NY Numbers (Pick 3)) |
| `birthday` | 2 | 1 | 0.7 | 0.50/draw | +0.35 | 1 (Mega Millions) |
| `antibalanced` | 2 | 1 | 0.7 | 0.50/draw | +0.35 | 1 (Powerball) |
| `cold` | 78 | 28 | 27.5 | 0.36/draw | +0.09 | 3 (NY Win 4) |
| `random` | 78 | 27 | 27.5 | 0.35/draw | -0.11 | 2 (Mega Millions) |
| `hot` | 78 | 27 | 27.5 | 0.35/draw | -0.11 | 2 (NY Numbers (Pick 3)) |
| `delta` | 14 | 4 | 5.0 | 0.29/draw | -0.50 | 1 (Powerball) |
| `contrarian` | 9 | 2 | 3.1 | 0.22/draw | -0.67 | 1 (NY Numbers (Pick 3)) |
| `llm-fewshot` | 68 | 20 | 24.0 | 0.29/draw | -0.87 | 2 (NY Win 4) |
| `benford` | 2 | 0 | 0.7 | 0.00/draw | -0.91 | 0 |
| `dreambook` | 7 | 1 | 2.4 | 0.14/draw | -0.95 | 1 (NY Win 4) |
| `unpopular` | 14 | 3 | 5.0 | 0.21/draw | -0.97 | 2 (Mega Millions) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-12 12:04 UTC</sub>
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
