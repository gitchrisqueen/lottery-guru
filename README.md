# 🎰 Lottery Guru

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-08-19

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Powerball**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `22` `50` `51` `56` `63` + `25` |
| `balanced` | `05` `08` `49` `55` `66` + `16` |
| `benford` | `13` `19` `23` `32` `49` + `25` |
| `birthday` | `02` `04` `06` `08` `12` + `11` |
| `cold` | `01` `11` `23` `33` `51` + `19` |
| `contrarian` | `04` `05` `15` `29` `69` + `13` |
| `delta` | `07` `13` `16` `30` `42` + `06` |
| `highest-frequency` | `05` `06` `11` `13` `66` + `25` |
| `hot` | `06` `36` `48` `63` `64` + `14` |
| `llm-fewshot` | `10` `11` `22` `38` `56` + `07` |
| `llm-tuned` | `11` `21` `28` `39` `44` + `26` |
| `moonphase` | `05` `07` `17` `29` `33` + `07` |
| `numerology` | `10` `12` `20` `24` `36` + `09` |
| `persistent` | `13` `21` `23` `32` `66` + `01` |
| `random` | `19` `42` `52` `60` `61` + `22` |
| `skiphit` | `05` `06` `25` `49` `66` + `09` |
| `unpopular` | `36` `41` `51` `57` `68` + `11` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `0` |
| `contrarian` | `4` `5` `2` |
| `dreambook` | `6` `2` `7` |
| `highest-frequency` | `4` `5` `5` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `9` `5` `8` |
| `llm-tuned` | `8` `9` `8` |
| `moonphase` | `3` `5` `5` |
| `numerology` | `1` `1` `3` |
| `persistent` | `4` `3` `3` |
| `positional` | `1` `8` `5` |
| `random` | `2` `7` `8` |
| `skiphit` | `5` `1` `5` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `0` |
| `contrarian` | `4` `1` `2` |
| `dreambook` | `4` `6` `8` |
| `highest-frequency` | `5` `1` `3` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `0` `5` `4` |
| `llm-tuned` | `9` `7` `4` |
| `moonphase` | `2` `9` `0` |
| `numerology` | `1` `1` `3` |
| `persistent` | `4` `3` `3` |
| `positional` | `1` `5` `3` |
| `random` | `5` `6` `5` |
| `skiphit` | `5` `1` `2` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `8` `0` `7` |
| `contrarian` | `8` `5` `5` `0` |
| `dreambook` | `9` `8` `0` `0` |
| `highest-frequency` | `8` `8` `5` `0` |
| `hot` | `8` `6` `3` `5` |
| `llm-fewshot` | `7` `2` `2` `1` |
| `llm-tuned` | `6` `8` `8` `2` |
| `moonphase` | `0` `3` `5` `8` |
| `numerology` | `1` `1` `3` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `7` `2` `7` `0` |
| `random` | `8` `1` `2` `7` |
| `skiphit` | `9` `5` `1` `3` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `8` `0` `7` |
| `contrarian` | `9` `2` `5` `0` |
| `dreambook` | `7` `5` `2` `8` |
| `highest-frequency` | `9` `5` `3` `7` |
| `hot` | `8` `6` `3` `5` |
| `llm-fewshot` | `1` `2` `7` `8` |
| `llm-tuned` | `8` `9` `4` `7` |
| `moonphase` | `0` `6` `3` `6` |
| `numerology` | `1` `1` `3` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `5` `8` `8` `1` |
| `random` | `9` `5` `7` `7` |
| `skiphit` | `9` `5` `5` `3` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `04` `06` `21` `25` |
| `balanced` | `01` `08` `14` `19` `28` |
| `benford` | `04` `12` `19` `24` `33` |
| `birthday` | `02` `06` `10` `11` `12` |
| `cold` | `04` `09` `17` `20` `21` |
| `contrarian` | `07` `09` `11` `27` `34` |
| `delta` | `03` `16` `19` `25` `35` |
| `highest-frequency` | `01` `04` `09` `12` `20` |
| `hot` | `09` `12` `20` `22` `24` |
| `llm-fewshot` | `04` `05` `08` `22` `33` |
| `llm-tuned` | `01` `08` `25` `27` `31` |
| `moonphase` | `01` `09` `20` `26` `36` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `07` `12` `20` `30` `36` |
| `skiphit` | `12` `13` `17` `20` `26` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `03` `06` `08` `13` `25` |
| `balanced` | `03` `08` `10` `19` `31` |
| `benford` | `04` `12` `18` `22` `30` |
| `birthday` | `04` `10` `11` `15` `31` |
| `cold` | `14` `18` `26` `31` `35` |
| `contrarian` | `08` `15` `17` `25` `26` |
| `delta` | `09` `23` `24` `31` `35` |
| `highest-frequency` | `10` `14` `22` `26` `31` |
| `hot` | `01` `15` `20` `22` `30` |
| `llm-fewshot` | `07` `10` `21` `24` `27` |
| `llm-tuned` | `02` `11` `16` `26` `33` |
| `moonphase` | `14` `15` `19` `25` `33` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `12` `20` `21` `22` `31` |
| `skiphit` | `01` `14` `21` `28` `33` |

**Florida Lotto**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `10` `26` `40` `45` `47` `51` |
| `balanced` | `05` `07` `32` `38` `40` `45` |
| `benford` | `05` `11` `19` `21` `35` `42` |
| `birthday` | `04` `05` `12` `17` `27` `30` |
| `cold` | `01` `10` `17` `26` `35` `53` |
| `contrarian` | `01` `07` `10` `16` `32` `41` |
| `delta` | `14` `16` `24` `26` `27` `31` |
| `highest-frequency` | `05` `10` `16` `26` `30` `32` |
| `hot` | `06` `24` `34` `42` `47` `51` |
| `llm-fewshot` | `05` `07` `12` `18` `29` `38` |
| `llm-tuned` | `18` `22` `26` `30` `46` `48` |
| `moonphase` | `16` `32` `43` `49` `52` `53` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `05` `10` `32` `33` `38` `50` |
| `random` | `03` `04` `06` `27` `51` `53` |
| `skiphit` | `11` `14` `16` `22` `48` `52` |
| `unpopular` | `33` `36` `42` `46` `48` `50` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `3` |
| `contrarian` | `0` `2` |
| `dreambook` | `2` `0` |
| `highest-frequency` | `1` `0` |
| `hot` | `1` `0` |
| `llm-fewshot` | `9` `8` |
| `llm-tuned` | `7` `0` |
| `moonphase` | `4` `9` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `2` `0` |
| `random` | `6` `1` |
| `skiphit` | `1` `3` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `6` |
| `contrarian` | `4` `8` |
| `dreambook` | `2` `3` |
| `highest-frequency` | `4` `1` |
| `hot` | `4` `8` |
| `llm-fewshot` | `1` `5` |
| `llm-tuned` | `6` `0` |
| `moonphase` | `5` `8` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `6` `2` |
| `random` | `4` `1` |
| `skiphit` | `6` `0` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `3` `7` |
| `contrarian` | `4` `0` `0` |
| `dreambook` | `8` `4` `2` |
| `highest-frequency` | `9` `0` `4` |
| `hot` | `1` `0` `8` |
| `llm-fewshot` | `9` `4` `7` |
| `llm-tuned` | `6` `4` `6` |
| `moonphase` | `3` `0` `5` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `7` `2` `4` |
| `random` | `9` `8` `4` |
| `skiphit` | `7` `7` `8` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `9` `0` |
| `contrarian` | `3` `6` `5` |
| `dreambook` | `2` `4` `3` |
| `highest-frequency` | `3` `4` `2` |
| `hot` | `8` `1` `2` |
| `llm-fewshot` | `1` `4` `4` |
| `llm-tuned` | `3` `9` `3` |
| `moonphase` | `0` `3` `1` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `7` `4` `7` |
| `random` | `7` `2` `2` |
| `skiphit` | `4` `4` `5` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `1` `3` `7` |
| `contrarian` | `7` `7` `8` `4` |
| `dreambook` | `2` `6` `1` `6` |
| `highest-frequency` | `7` `3` `1` `5` |
| `hot` | `7` `4` `9` `2` |
| `llm-fewshot` | `9` `2` `9` `5` |
| `llm-tuned` | `8` `3` `4` `7` |
| `moonphase` | `4` `3` `7` `1` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `9` `6` `1` `3` |
| `random` | `0` `5` `2` `5` |
| `skiphit` | `8` `3` `8` `2` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `0` `2` `9` |
| `contrarian` | `2` `4` `4` `8` |
| `dreambook` | `2` `4` `4` `7` |
| `highest-frequency` | `2` `1` `1` `5` |
| `hot` | `8` `1` `0` `7` |
| `llm-fewshot` | `5` `1` `1` `4` |
| `llm-tuned` | `5` `0` `3` `4` |
| `moonphase` | `2` `5` `9` `9` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `6` `2` `1` `4` |
| `random` | `2` `2` `8` `0` |
| `skiphit` | `5` `2` `9` `5` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `0` `4` `3` `5` |
| `contrarian` | `1` `5` `6` `8` `3` |
| `dreambook` | `0` `4` `3` `1` `8` |
| `highest-frequency` | `3` `1` `4` `6` `3` |
| `hot` | `6` `9` `4` `0` `3` |
| `llm-fewshot` | `4` `2` `4` `7` `9` |
| `llm-tuned` | `7` `1` `0` `6` `1` |
| `moonphase` | `3` `5` `7` `2` `1` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `3` `4` `4` `6` `0` |
| `random` | `7` `0` `5` `4` `2` |
| `skiphit` | `3` `9` `5` `1` `3` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `0` `5` `6` `4` |
| `contrarian` | `5` `0` `9` `7` `4` |
| `dreambook` | `3` `1` `6` `1` `9` |
| `highest-frequency` | `1` `1` `6` `7` `4` |
| `hot` | `6` `0` `9` `8` `2` |
| `llm-fewshot` | `1` `7` `7` `7` `5` |
| `llm-tuned` | `7` `3` `3` `6` `1` |
| `moonphase` | `7` `4` `4` `4` `5` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `8` `9` `6` `7` `6` |
| `random` | `6` `5` `2` `3` `9` |
| `skiphit` | `1` `8` `3` `1` `0` |

<sub>Updated 2026-08-19 10:58 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**878** predictions scored across **25** days. Combined, they've hit **339** numbers where pure chance predicts **310.7** (z = **+1.70**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 68 | 37 | 24.0 | 0.54/draw | +2.80 | 2 (Mega Millions) |
| `contrarian` | 35 | 21 | 12.4 | 0.60/draw | +2.60 | 2 (NY Numbers (Pick 3)) |
| `skiphit` | 35 | 18 | 12.4 | 0.51/draw | +1.69 | 2 (NY Win 4) |
| `birthday` | 6 | 4 | 2.2 | 0.67/draw | +1.34 | 2 (Powerball) |
| `llm-tuned` | 54 | 23 | 19.1 | 0.43/draw | +0.94 | 3 (NY Win 4) |
| `numerology` | 35 | 15 | 12.4 | 0.43/draw | +0.79 | 2 (NY Numbers (Pick 3)) |
| `balanced` | 6 | 3 | 2.2 | 0.50/draw | +0.61 | 2 (Mega Millions) |
| `benford` | 6 | 3 | 2.2 | 0.50/draw | +0.61 | 1 (Powerball) |
| `positional` | 86 | 33 | 30.3 | 0.38/draw | +0.52 | 2 (NY Win 4) |
| `persistent` | 35 | 14 | 12.4 | 0.40/draw | +0.49 | 2 (NY Numbers (Pick 3)) |
| `random` | 104 | 39 | 36.8 | 0.38/draw | +0.39 | 2 (Mega Millions) |
| `hot` | 104 | 39 | 36.8 | 0.38/draw | +0.39 | 3 (NY Numbers (Pick 3)) |
| `delta` | 18 | 7 | 6.5 | 0.39/draw | +0.22 | 1 (Powerball) |
| `moonphase` | 35 | 13 | 12.4 | 0.37/draw | +0.19 | 2 (NY Win 4) |
| `antibalanced` | 6 | 2 | 2.2 | 0.33/draw | -0.12 | 1 (Powerball) |
| `cold` | 104 | 33 | 36.8 | 0.32/draw | -0.66 | 3 (NY Win 4) |
| `dreambook` | 29 | 8 | 10.2 | 0.28/draw | -0.73 | 1 (NY Win 4) |
| `unpopular` | 18 | 3 | 6.5 | 0.17/draw | -1.46 | 2 (Mega Millions) |
| `llm-fewshot` | 94 | 24 | 33.3 | 0.26/draw | -1.70 | 2 (NY Win 4) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-19 10:58 UTC</sub>
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
