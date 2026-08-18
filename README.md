# 🎰 Lottery Guru

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-08-18

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Mega Millions**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `10` `20` `54` `60` `66` + `02` |
| `balanced` | `17` `21` `31` `56` `64` + `13` |
| `benford` | `19` `21` `30` `41` `59` + `14` |
| `birthday` | `02` `05` `11` `12` `13` + `05` |
| `cold` | `06` `08` `11` `28` `69` + `18` |
| `contrarian` | `17` `27` `30` `46` `60` + `17` |
| `delta` | `05` `06` `09` `28` `50` + `11` |
| `highest-frequency` | `10` `21` `27` `38` `39` + `14` |
| `hot` | `18` `21` `42` `43` `49` + `12` |
| `llm-fewshot` | `19` `39` `49` `50` `66` + `19` |
| `llm-tuned` | `04` `18` `27` `40` `67` + `15` |
| `moonphase` | `02` `10` `21` `31` `58` + `14` |
| `numerology` | `10` `12` `20` `24` `34` + `09` |
| `persistent` | `01` `09` `37` `38` `39` + `22` |
| `random` | `03` `24` `35` `38` `56` + `10` |
| `skiphit` | `01` `03` `27` `37` `60` + `04` |
| `unpopular` | `33` `38` `39` `51` `58` + `14` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `1` |
| `contrarian` | `4` `8` `5` |
| `dreambook` | `9` `6` `6` |
| `highest-frequency` | `4` `8` `1` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `9` `7` `8` |
| `llm-tuned` | `4` `8` `9` |
| `moonphase` | `5` `4` `4` |
| `numerology` | `1` `1` `1` |
| `persistent` | `4` `3` `3` |
| `positional` | `2` `8` `8` |
| `random` | `7` `3` `6` |
| `skiphit` | `4` `5` `3` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `7` `1` |
| `contrarian` | `4` `5` `5` |
| `dreambook` | `5` `2` `3` |
| `highest-frequency` | `5` `5` `3` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `9` `3` `8` |
| `llm-tuned` | `1` `5` `3` |
| `moonphase` | `2` `1` `3` |
| `numerology` | `1` `1` `1` |
| `persistent` | `4` `3` `3` |
| `positional` | `8` `5` `3` |
| `random` | `5` `5` `6` |
| `skiphit` | `9` `8` `2` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `6` `4` `2` |
| `contrarian` | `5` `8` `3` `0` |
| `dreambook` | `2` `4` `9` `9` |
| `highest-frequency` | `2` `9` `9` `5` |
| `hot` | `8` `6` `3` `2` |
| `llm-fewshot` | `2` `0` `7` `1` |
| `llm-tuned` | `9` `9` `9` `3` |
| `moonphase` | `0` `4` `8` `2` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `3` `5` `9` `4` |
| `random` | `0` `2` `4` `5` |
| `skiphit` | `8` `3` `7` `0` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `6` `4` `1` |
| `contrarian` | `5` `8` `3` `1` |
| `dreambook` | `3` `7` `8` `0` |
| `highest-frequency` | `8` `7` `6` `5` |
| `hot` | `8` `6` `3` `5` |
| `llm-fewshot` | `6` `4` `4` `5` |
| `llm-tuned` | `3` `5` `6` `6` |
| `moonphase` | `8` `1` `2` `7` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `9` `7` `6` `0` |
| `random` | `1` `7` `3` `2` |
| `skiphit` | `8` `3` `7` `0` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `05` `21` `27` `33` |
| `balanced` | `08` `14` `18` `23` `29` |
| `benford` | `05` `10` `14` `25` `35` |
| `birthday` | `02` `03` `11` `19` `22` |
| `cold` | `05` `07` `08` `12` `33` |
| `contrarian` | `05` `07` `20` `31` `36` |
| `delta` | `03` `13` `17` `29` `35` |
| `highest-frequency` | `05` `14` `20` `33` `35` |
| `hot` | `12` `18` `30` `34` `35` |
| `llm-fewshot` | `08` `21` `22` `31` `35` |
| `llm-tuned` | `14` `18` `20` `25` `33` |
| `moonphase` | `02` `15` `16` `23` `25` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `03` `06` `10` `19` `28` |
| `skiphit` | `01` `09` `14` `23` `35` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `22` `23` `26` `27` `29` |
| `balanced` | `06` `19` `24` `29` `34` |
| `benford` | `02` `06` `14` `17` `31` |
| `birthday` | `05` `14` `20` `22` `25` |
| `cold` | `03` `11` `22` `25` `35` |
| `contrarian` | `16` `17` `19` `26` `32` |
| `delta` | `01` `14` `16` `28` `32` |
| `highest-frequency` | `05` `14` `22` `26` `31` |
| `hot` | `07` `11` `14` `26` `30` |
| `llm-fewshot` | `02` `05` `07` `14` `27` |
| `llm-tuned` | `04` `27` `31` `34` `36` |
| `moonphase` | `05` `15` `26` `28` `31` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `03` `04` `14` `23` `33` |
| `skiphit` | `04` `05` `11` `16` `23` |

**FL Jackpot Triple Play**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `25` `32` `34` `36` `40` `44` |
| `balanced` | `09` `17` `27` `32` `36` `46` |
| `benford` | `01` `06` `12` `29` `37` `42` |
| `birthday` | `01` `04` `08` `09` `11` `30` |
| `cold` | `02` `04` `08` `19` `20` `42` |
| `contrarian` | `06` `07` `08` `13` `26` `35` |
| `delta` | `07` `09` `14` `28` `30` `39` |
| `highest-frequency` | `06` `07` `08` `10` `36` `39` |
| `hot` | `03` `06` `07` `20` `36` `39` |
| `llm-fewshot` | `06` `26` `30` `35` `36` `39` |
| `llm-tuned` | `03` `10` `15` `21` `39` `46` |
| `moonphase` | `03` `22` `28` `33` `35` `39` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `01` `04` `10` `18` `21` `29` |
| `random` | `01` `10` `11` `23` `27` `31` |
| `skiphit` | `06` `07` `08` `15` `18` `34` |
| `unpopular` | `20` `26` `27` `42` `43` `46` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `1` |
| `contrarian` | `0` `1` |
| `dreambook` | `5` `9` |
| `highest-frequency` | `2` `1` |
| `hot` | `1` `8` |
| `llm-fewshot` | `3` `9` |
| `llm-tuned` | `2` `2` |
| `moonphase` | `7` `1` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `2` `1` |
| `random` | `2` `4` |
| `skiphit` | `9` `1` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `0` |
| `contrarian` | `1` `6` |
| `dreambook` | `6` `0` |
| `highest-frequency` | `3` `5` |
| `hot` | `3` `9` |
| `llm-fewshot` | `3` `8` |
| `llm-tuned` | `2` `4` |
| `moonphase` | `3` `5` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `3` `5` |
| `random` | `3` `5` |
| `skiphit` | `5` `9` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `0` `5` |
| `contrarian` | `5` `5` `6` |
| `dreambook` | `0` `0` `1` |
| `highest-frequency` | `5` `6` `1` |
| `hot` | `4` `2` `8` |
| `llm-fewshot` | `3` `6` `7` |
| `llm-tuned` | `0` `9` `0` |
| `moonphase` | `5` `1` `1` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `5` `0` `7` |
| `random` | `9` `6` `8` |
| `skiphit` | `9` `1` `0` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `2` `6` |
| `contrarian` | `4` `7` `0` |
| `dreambook` | `2` `4` `3` |
| `highest-frequency` | `8` `2` `9` |
| `hot` | `6` `4` `9` |
| `llm-fewshot` | `2` `7` `5` |
| `llm-tuned` | `5` `2` `4` |
| `moonphase` | `8` `5` `5` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `8` `8` `9` |
| `random` | `0` `3` `9` |
| `skiphit` | `8` `6` `1` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `8` `0` `7` |
| `contrarian` | `1` `9` `2` `7` |
| `dreambook` | `5` `3` `0` `5` |
| `highest-frequency` | `5` `4` `0` `5` |
| `hot` | `1` `3` `8` `2` |
| `llm-fewshot` | `6` `4` `8` `8` |
| `llm-tuned` | `8` `7` `4` `8` |
| `moonphase` | `9` `7` `1` `7` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `8` `0` `0` `2` |
| `random` | `5` `6` `0` `0` |
| `skiphit` | `9` `5` `7` `4` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `7` `8` `4` |
| `contrarian` | `6` `0` `7` `1` |
| `dreambook` | `5` `7` `5` `6` |
| `highest-frequency` | `0` `4` `5` `5` |
| `hot` | `6` `4` `1` `5` |
| `llm-fewshot` | `0` `3` `8` `4` |
| `llm-tuned` | `7` `8` `5` `1` |
| `moonphase` | `9` `1` `6` `0` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `0` `3` `5` `2` |
| `random` | `8` `9` `2` `7` |
| `skiphit` | `0` `4` `0` `4` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `9` `4` `7` `5` |
| `contrarian` | `6` `4` `7` `9` `5` |
| `dreambook` | `5` `0` `2` `4` `3` |
| `highest-frequency` | `5` `9` `7` `9` `5` |
| `hot` | `8` `9` `3` `1` `2` |
| `llm-fewshot` | `5` `7` `0` `7` `6` |
| `llm-tuned` | `9` `9` `7` `0` `1` |
| `moonphase` | `4` `0` `2` `2` `3` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `4` `8` `0` `9` `9` |
| `random` | `4` `2` `7` `6` `2` |
| `skiphit` | `5` `4` `9` `9` `8` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `4` `6` `2` `3` |
| `contrarian` | `4` `1` `8` `2` `4` |
| `dreambook` | `7` `2` `4` `0` `2` |
| `highest-frequency` | `8` `1` `1` `5` `4` |
| `hot` | `2` `1` `4` `0` `5` |
| `llm-fewshot` | `6` `9` `7` `1` `7` |
| `llm-tuned` | `9` `4` `6` `5` `3` |
| `moonphase` | `8` `9` `7` `1` `4` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `3` `5` `0` `7` `8` |
| `random` | `3` `5` `1` `2` `6` |
| `skiphit` | `0` `4` `1` `5` `3` |

<sub>Updated 2026-08-18 11:40 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**826** predictions scored across **24** days. Combined, they've hit **317** numbers where pure chance predicts **292.5** (z = **+1.51**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 64 | 35 | 22.6 | 0.55/draw | +2.75 | 2 (Mega Millions) |
| `contrarian` | 31 | 19 | 11.0 | 0.61/draw | +2.57 | 2 (NY Numbers (Pick 3)) |
| `birthday` | 6 | 4 | 2.2 | 0.67/draw | +1.34 | 2 (Powerball) |
| `skiphit` | 31 | 15 | 11.0 | 0.48/draw | +1.29 | 2 (NY Win 4) |
| `positional` | 82 | 33 | 28.9 | 0.40/draw | +0.80 | 2 (NY Win 4) |
| `persistent` | 31 | 13 | 11.0 | 0.42/draw | +0.65 | 2 (NY Numbers (Pick 3)) |
| `moonphase` | 31 | 13 | 11.0 | 0.42/draw | +0.65 | 2 (NY Win 4) |
| `balanced` | 6 | 3 | 2.2 | 0.50/draw | +0.61 | 2 (Mega Millions) |
| `benford` | 6 | 3 | 2.2 | 0.50/draw | +0.61 | 1 (Powerball) |
| `llm-tuned` | 50 | 20 | 17.7 | 0.40/draw | +0.57 | 3 (NY Win 4) |
| `numerology` | 31 | 12 | 11.0 | 0.39/draw | +0.33 | 2 (NY Numbers (Pick 3)) |
| `delta` | 18 | 7 | 6.5 | 0.39/draw | +0.22 | 1 (Powerball) |
| `random` | 100 | 36 | 35.4 | 0.36/draw | +0.11 | 2 (Mega Millions) |
| `hot` | 100 | 36 | 35.4 | 0.36/draw | +0.11 | 2 (NY Numbers (Pick 3)) |
| `antibalanced` | 6 | 2 | 2.2 | 0.33/draw | -0.12 | 1 (Powerball) |
| `cold` | 100 | 32 | 35.4 | 0.32/draw | -0.60 | 3 (NY Win 4) |
| `dreambook` | 25 | 7 | 8.8 | 0.28/draw | -0.64 | 1 (NY Win 4) |
| `unpopular` | 18 | 3 | 6.5 | 0.17/draw | -1.46 | 2 (Mega Millions) |
| `llm-fewshot` | 90 | 24 | 31.9 | 0.27/draw | -1.47 | 2 (NY Win 4) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-18 11:40 UTC</sub>
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
