# 🎰 Lottery Guru

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-08-10

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Powerball**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `28` `45` `54` `59` `69` + `06` |
| `balanced` | `04` `21` `24` `30` `67` + `10` |
| `benford` | `11` `12` `26` `39` `43` + `09` |
| `birthday` | `03` `04` `08` `19` `30` + `11` |
| `cold` | `11` `15` `23` `33` `51` + `09` |
| `contrarian` | `05` `08` `14` `30` `63` + `04` |
| `delta` | `13` `16` `25` `36` `45` + `08` |
| `highest-frequency` | `04` `30` `36` `50` `67` + `09` |
| `hot` | `18` `36` `48` `52` `64` + `14` |
| `llm-fewshot` | `02` `19` `36` `44` `68` + `14` |
| `llm-tuned` | `08` `26` `55` `67` `69` + `08` |
| `moonphase` | `01` `40` `50` `53` `61` + `21` |
| `numerology` | `10` `12` `20` `24` `36` + `09` |
| `persistent` | `13` `21` `23` `32` `66` + `01` |
| `random` | `04` `36` `56` `58` `68` + `11` |
| `skiphit` | `06` `09` `46` `50` `63` + `04` |
| `unpopular` | `33` `50` `52` `64` `67` + `01` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `0` `6` |
| `contrarian` | `4` `7` `3` |
| `dreambook` | `7` `3` `0` |
| `highest-frequency` | `1` `3` `3` |
| `hot` | `8` `3` `5` |
| `llm-fewshot` | `5` `2` `9` |
| `llm-tuned` | `9` `9` `4` |
| `moonphase` | `1` `8` `3` |
| `numerology` | `1` `1` `3` |
| `persistent` | `4` `3` `3` |
| `positional` | `9` `1` `5` |
| `random` | `0` `8` `3` |
| `skiphit` | `8` `7` `2` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `0` `6` |
| `contrarian` | `8` `5` `3` |
| `dreambook` | `2` `4` `3` |
| `highest-frequency` | `1` `3` `3` |
| `hot` | `8` `3` `5` |
| `llm-fewshot` | `6` `0` `0` |
| `llm-tuned` | `6` `3` `2` |
| `moonphase` | `1` `3` `3` |
| `numerology` | `1` `1` `3` |
| `persistent` | `4` `3` `3` |
| `positional` | `5` `0` `1` |
| `random` | `6` `6` `0` |
| `skiphit` | `2` `5` `2` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `0` `4` `1` |
| `contrarian` | `3` `3` `5` `9` |
| `dreambook` | `0` `6` `2` `9` |
| `highest-frequency` | `3` `9` `3` `8` |
| `hot` | `6` `5` `2` `8` |
| `llm-fewshot` | `8` `6` `9` `0` |
| `llm-tuned` | `7` `9` `5` `8` |
| `moonphase` | `3` `9` `0` `8` |
| `numerology` | `1` `1` `3` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `2` `5` `3` `8` |
| `random` | `0` `5` `3` `6` |
| `skiphit` | `3` `3` `7` `3` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `2` `4` `1` |
| `contrarian` | `5` `8` `8` `3` |
| `dreambook` | `9` `8` `4` `9` |
| `highest-frequency` | `5` `6` `8` `8` |
| `hot` | `6` `5` `8` `3` |
| `llm-fewshot` | `4` `6` `2` `6` |
| `llm-tuned` | `4` `0` `0` `8` |
| `moonphase` | `8` `6` `8` `8` |
| `numerology` | `1` `1` `3` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `5` `6` `2` `8` |
| `random` | `1` `5` `5` `8` |
| `skiphit` | `8` `3` `7` `3` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `02` `10` `18` `30` `36` |
| `balanced` | `02` `20` `21` `22` `29` |
| `benford` | `04` `14` `19` `23` `30` |
| `birthday` | `01` `02` `05` `06` `09` |
| `cold` | `01` `02` `21` `33` `36` |
| `contrarian` | `12` `16` `21` `23` `34` |
| `delta` | `05` `10` `14` `29` `30` |
| `highest-frequency` | `02` `05` `14` `26` `36` |
| `hot` | `06` `13` `17` `26` `36` |
| `llm-fewshot` | `03` `14` `30` `31` `35` |
| `llm-tuned` | `01` `02` `10` `14` `25` |
| `moonphase` | `05` `09` `15` `17` `36` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `19` `22` `25` `26` `35` |
| `skiphit` | `08` `11` `12` `17` `26` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `03` `04` `05` `16` `32` |
| `balanced` | `02` `14` `16` `21` `25` |
| `benford` | `04` `16` `18` `26` `33` |
| `birthday` | `01` `02` `07` `10` `31` |
| `cold` | `17` `21` `27` `33` `35` |
| `contrarian` | `02` `06` `11` `24` `33` |
| `delta` | `01` `03` `14` `24` `28` |
| `highest-frequency` | `01` `02` `14` `16` `21` |
| `hot` | `07` `12` `18` `21` `35` |
| `llm-fewshot` | `19` `20` `29` `30` `35` |
| `llm-tuned` | `01` `02` `22` `27` `30` |
| `moonphase` | `06` `15` `23` `26` `36` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `01` `02` `06` `21` `31` |
| `skiphit` | `11` `14` `17` `28` `30` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `5` |
| `contrarian` | `0` `5` |
| `dreambook` | `2` `6` |
| `highest-frequency` | `1` `5` |
| `hot` | `2` `5` |
| `llm-fewshot` | `1` `1` |
| `llm-tuned` | `5` `7` |
| `moonphase` | `8` `7` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `6` `4` |
| `random` | `3` `3` |
| `skiphit` | `1` `8` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `8` |
| `contrarian` | `7` `3` |
| `dreambook` | `3` `4` |
| `highest-frequency` | `8` `1` |
| `hot` | `2` `9` |
| `llm-fewshot` | `8` `1` |
| `llm-tuned` | `2` `4` |
| `moonphase` | `9` `3` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `3` `1` |
| `random` | `8` `2` |
| `skiphit` | `0` `1` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `6` `9` |
| `contrarian` | `5` `5` `7` |
| `dreambook` | `5` `7` `5` |
| `highest-frequency` | `5` `6` `1` |
| `hot` | `0` `9` `8` |
| `llm-fewshot` | `2` `9` `5` |
| `llm-tuned` | `2` `8` `4` |
| `moonphase` | `1` `7` `3` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `9` `2` `8` |
| `random` | `2` `1` `1` |
| `skiphit` | `5` `6` `0` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `0` `5` |
| `contrarian` | `1` `8` `8` |
| `dreambook` | `5` `3` `0` |
| `highest-frequency` | `9` `0` `8` |
| `hot` | `0` `5` `1` |
| `llm-fewshot` | `6` `8` `8` |
| `llm-tuned` | `9` `7` `4` |
| `moonphase` | `3` `0` `0` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `9` `4` `7` |
| `random` | `4` `9` `7` |
| `skiphit` | `9` `0` `2` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `5` `1` `7` |
| `contrarian` | `7` `8` `8` `2` |
| `dreambook` | `2` `3` `4` `4` |
| `highest-frequency` | `2` `1` `1` `9` |
| `hot` | `5` `1` `3` `0` |
| `llm-fewshot` | `1` `6` `0` `9` |
| `llm-tuned` | `8` `8` `8` `9` |
| `moonphase` | `9` `9` `8` `1` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `2` `7` `0` `3` |
| `random` | `9` `2` `1` `6` |
| `skiphit` | `2` `5` `7` `0` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `7` `0` `4` |
| `contrarian` | `7` `9` `9` `1` |
| `dreambook` | `0` `2` `4` `7` |
| `highest-frequency` | `2` `8` `0` `5` |
| `hot` | `1` `8` `2` `0` |
| `llm-fewshot` | `6` `3` `0` `5` |
| `llm-tuned` | `7` `5` `7` `3` |
| `moonphase` | `3` `6` `4` `2` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `4` `0` `1` `2` |
| `random` | `2` `2` `8` `7` |
| `skiphit` | `2` `8` `3` `6` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `8` `1` `3` `0` |
| `contrarian` | `2` `3` `6` `6` `4` |
| `dreambook` | `9` `3` `7` `7` `3` |
| `highest-frequency` | `5` `3` `6` `0` `4` |
| `hot` | `8` `1` `2` `3` `6` |
| `llm-fewshot` | `2` `4` `2` `1` `0` |
| `llm-tuned` | `7` `2` `7` `7` `6` |
| `moonphase` | `9` `7` `6` `1` `4` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `5` `7` `4` `0` `4` |
| `random` | `7` `3` `4` `0` `4` |
| `skiphit` | `2` `6` `1` `6` `3` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `5` `0` `6` `3` |
| `contrarian` | `1` `4` `7` `1` `9` |
| `dreambook` | `5` `2` `3` `0` `7` |
| `highest-frequency` | `5` `5` `0` `6` `3` |
| `hot` | `5` `3` `8` `6` `0` |
| `llm-fewshot` | `3` `2` `9` `6` `3` |
| `llm-tuned` | `9` `5` `0` `8` `3` |
| `moonphase` | `4` `9` `1` `4` `4` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `5` `6` `3` `6` `7` |
| `random` | `7` `5` `0` `9` `1` |
| `skiphit` | `7` `7` `5` `6` `9` |

<sub>Updated 2026-08-10 11:32 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**406** predictions scored across **16** days. Combined, they've hit **153** numbers where pure chance predicts **143.7** (z = **+0.82**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 33 | 19 | 11.7 | 0.58/draw | +2.27 | 2 (Mega Millions) |
| `positional` | 57 | 23 | 20.1 | 0.40/draw | +0.68 | 2 (NY Win 4) |
| `random` | 69 | 27 | 24.4 | 0.39/draw | +0.55 | 2 (Mega Millions) |
| `llm-tuned` | 26 | 10 | 9.2 | 0.38/draw | +0.29 | 3 (NY Win 4) |
| `hot` | 69 | 25 | 24.4 | 0.36/draw | +0.12 | 2 (NY Numbers (Pick 3)) |
| `cold` | 69 | 25 | 24.4 | 0.36/draw | +0.12 | 3 (NY Win 4) |
| `delta` | 12 | 4 | 4.3 | 0.33/draw | -0.17 | 1 (Powerball) |
| `llm-fewshot` | 59 | 18 | 20.9 | 0.31/draw | -0.67 | 2 (NY Win 4) |
| `unpopular` | 12 | 2 | 4.3 | 0.17/draw | -1.19 | 2 (Mega Millions) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-10 11:32 UTC</sub>
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
