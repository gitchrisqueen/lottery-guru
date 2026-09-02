# 🎰 Lottery Guru

[![Live dashboard](https://img.shields.io/badge/📊_live_dashboard-gitchrisqueen.github.io%2Flottery--guru-4056a1)](https://gitchrisqueen.github.io/lottery-guru/)
[![Deploy dashboard](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/pages.yml/badge.svg)](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/pages.yml)
[![Daily prediction loop](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/daily.yml/badge.svg)](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/daily.yml)

**📊 [View the live dashboard →](https://gitchrisqueen.github.io/lottery-guru/)** — sortable leaderboards, today's picks, and the exploit watch, rebuilt after every daily loop.

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-09-02

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Powerball**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `44` `52` `54` `55` `60` + `02` |
| `balanced` | `02` `32` `43` `53` `54` + `24` |
| `benford` | `04` `14` `17` `26` `36` + `13` |
| `birthday` | `01` `04` `08` `16` `26` + `10` |
| `cold` | `01` `23` `34` `51` `52` + `19` |
| `contrarian` | `12` `18` `49` `65` `67` + `18` |
| `delta` | `06` `08` `21` `42` `65` + `07` |
| `highest-frequency` | `06` `21` `32` `44` `54` + `02` |
| `hot` | `06` `36` `56` `63` `64` + `02` |
| `llm-fewshot` | `14` `39` `44` `54` `56` + `02` |
| `moonphase` | `06` `19` `20` `44` `46` + `12` |
| `numerology` | `03` `10` `12` `20` `24` + `02` |
| `persistent` | `13` `21` `23` `32` `66` + `01` |
| `random` | `02` `31` `44` `47` `63` + `05` |
| `skiphit` | `11` `17` `32` `37` `69` + `13` |
| `unpopular` | `44` `47` `50` `55` `60` + `23` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `2` `5` |
| `contrarian` | `6` `4` `9` |
| `dreambook` | `1` `0` `4` |
| `highest-frequency` | `2` `0` `5` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `2` `0` `1` |
| `moonphase` | `2` `9` `1` |
| `numerology` | `1` `1` `5` |
| `persistent` | `4` `3` `3` |
| `positional` | `3` `8` `4` |
| `random` | `2` `6` `2` |
| `skiphit` | `7` `0` `5` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `2` `5` |
| `contrarian` | `6` `1` `8` |
| `dreambook` | `9` `4` `1` |
| `highest-frequency` | `1` `0` `5` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `3` `9` `3` |
| `moonphase` | `1` `6` `7` |
| `numerology` | `1` `1` `5` |
| `persistent` | `4` `3` `3` |
| `positional` | `4` `3` `5` |
| `random` | `1` `0` `3` |
| `skiphit` | `1` `0` `8` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `3` `9` `7` |
| `contrarian` | `2` `6` `1` `4` |
| `dreambook` | `5` `3` `0` `5` |
| `highest-frequency` | `2` `9` `5` `5` |
| `hot` | `8` `9` `3` `5` |
| `llm-fewshot` | `2` `8` `5` `5` |
| `moonphase` | `1` `9` `3` `9` |
| `numerology` | `1` `1` `5` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `5` `5` `5` `4` |
| `random` | `4` `2` `2` `4` |
| `skiphit` | `2` `6` `1` `4` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `3` `9` `7` |
| `contrarian` | `2` `6` `1` `6` |
| `dreambook` | `5` `9` `2` `1` |
| `highest-frequency` | `2` `9` `2` `5` |
| `hot` | `8` `9` `3` `2` |
| `llm-fewshot` | `9` `5` `2` `9` |
| `moonphase` | `4` `9` `4` `8` |
| `numerology` | `1` `1` `5` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `4` `9` `3` `0` |
| `random` | `7` `0` `5` `7` |
| `skiphit` | `2` `6` `1` `4` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `16` `17` `28` `33` `36` |
| `balanced` | `05` `07` `18` `30` `33` |
| `benford` | `05` `16` `17` `26` `30` |
| `birthday` | `08` `09` `11` `19` `21` |
| `cold` | `02` `09` `10` `15` `18` |
| `contrarian` | `05` `13` `17` `21` `23` |
| `delta` | `04` `19` `25` `27` `34` |
| `highest-frequency` | `05` `09` `17` `19` `33` |
| `hot` | `03` `07` `08` `09` `29` |
| `llm-fewshot` | `17` `25` `28` `32` `33` |
| `moonphase` | `12` `13` `19` `24` `33` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `20` `26` `31` `35` `36` |
| `skiphit` | `04` `09` `13` `19` `25` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `02` `16` `22` `30` `34` |
| `balanced` | `01` `12` `18` `25` `26` |
| `benford` | `01` `05` `18` `26` `35` |
| `birthday` | `03` `07` `09` `14` `17` |
| `cold` | `06` `17` `18` `23` `30` |
| `contrarian` | `03` `11` `12` `25` `36` |
| `delta` | `01` `05` `12` `19` `33` |
| `highest-frequency` | `01` `05` `12` `26` `36` |
| `hot` | `01` `05` `09` `28` `35` |
| `llm-fewshot` | `01` `06` `19` `34` `36` |
| `moonphase` | `01` `11` `27` `31` `32` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `02` `09` `13` `27` `29` |
| `skiphit` | `01` `04` `12` `21` `32` |

**Florida Lotto**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `11` `17` `21` `24` `31` |
| `balanced` | `01` `13` `25` `32` `38` `48` |
| `benford` | `04` `12` `15` `23` `37` `52` |
| `birthday` | `03` `06` `08` `10` `12` `16` |
| `cold` | `18` `23` `36` `37` `39` `50` |
| `contrarian` | `03` `05` `07` `12` `24` `47` |
| `delta` | `14` `29` `42` `44` `45` `46` |
| `highest-frequency` | `10` `12` `23` `24` `25` `39` |
| `hot` | `09` `18` `28` `33` `49` `51` |
| `moonphase` | `13` `17` `29` `35` `45` `50` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `05` `10` `32` `33` `38` `50` |
| `random` | `07` `23` `25` `26` `28` `49` |
| `skiphit` | `01` `14` `25` `27` `34` `39` |
| `unpopular` | `23` `31` `39` `40` `47` `53` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `3` |
| `contrarian` | `1` `2` |
| `dreambook` | `2` `3` |
| `highest-frequency` | `1` `7` |
| `hot` | `5` `2` |
| `llm-fewshot` | `3` `7` |
| `moonphase` | `5` `7` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `1` `6` |
| `random` | `3` `7` |
| `skiphit` | `9` `0` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `6` |
| `contrarian` | `1` `3` |
| `dreambook` | `0` `6` |
| `highest-frequency` | `1` `5` |
| `hot` | `4` `9` |
| `llm-fewshot` | `1` `5` |
| `moonphase` | `4` `2` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `6` `7` |
| `random` | `6` `8` |
| `skiphit` | `3` `5` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `5` `8` |
| `contrarian` | `3` `5` `5` |
| `dreambook` | `3` `1` `6` |
| `highest-frequency` | `3` `6` `4` |
| `hot` | `9` `4` `8` |
| `llm-fewshot` | `7` `6` `4` |
| `moonphase` | `2` `7` `7` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `8` `3` `3` |
| `random` | `0` `9` `3` |
| `skiphit` | `6` `4` `1` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `3` `2` |
| `contrarian` | `2` `2` `6` |
| `dreambook` | `9` `8` `6` |
| `highest-frequency` | `0` `2` `6` |
| `hot` | `0` `5` `4` |
| `llm-fewshot` | `0` `9` `7` |
| `moonphase` | `0` `6` `5` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `5` `2` `9` |
| `random` | `9` `2` `3` |
| `skiphit` | `1` `2` `6` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `6` `1` `2` |
| `contrarian` | `2` `7` `6` `7` |
| `dreambook` | `3` `4` `8` `7` |
| `highest-frequency` | `2` `4` `6` `7` |
| `hot` | `7` `0` `9` `2` |
| `llm-fewshot` | `1` `3` `2` `6` |
| `moonphase` | `2` `5` `4` `3` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `2` `2` `6` `8` |
| `random` | `4` `8` `6` `7` |
| `skiphit` | `8` `9` `6` `7` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `9` `3` `4` |
| `contrarian` | `4` `8` `2` `0` |
| `dreambook` | `9` `6` `6` `7` |
| `highest-frequency` | `7` `8` `2` `4` |
| `hot` | `3` `4` `2` `0` |
| `llm-fewshot` | `5` `8` `4` `4` |
| `moonphase` | `7` `6` `5` `2` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `3` `8` `8` `4` |
| `random` | `2` `8` `2` `9` |
| `skiphit` | `7` `9` `2` `8` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `3` `7` `8` `0` |
| `contrarian` | `3` `0` `1` `8` `6` |
| `dreambook` | `2` `3` `2` `3` `2` |
| `highest-frequency` | `6` `1` `6` `8` `4` |
| `hot` | `6` `7` `4` `5` `3` |
| `llm-fewshot` | `6` `4` `5` `6` `8` |
| `moonphase` | `4` `4` `6` `4` `1` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `9` `2` `2` `2` `4` |
| `random` | `8` `0` `2` `7` `2` |
| `skiphit` | `0` `1` `6` `3` `1` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `4` `6` `7` `2` |
| `contrarian` | `4` `6` `9` `2` `8` |
| `dreambook` | `6` `0` `3` `6` `6` |
| `highest-frequency` | `5` `4` `8` `2` `4` |
| `hot` | `5` `2` `4` `0` `3` |
| `llm-fewshot` | `2` `6` `9` `8` `0` |
| `moonphase` | `9` `3` `8` `6` `1` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `3` `9` `4` `2` `4` |
| `random` | `6` `2` `3` `2` `2` |
| `skiphit` | `3` `4` `8` `8` `1` |

<sub>Updated 2026-09-02 14:38 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**1691** predictions scored across **39** days. Combined, they've hit **626** numbers where pure chance predicts **597.6** (z = **+1.23**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `contrarian` | 97 | 51 | 34.2 | 0.53/draw | +3.03 | 2 (NY Numbers (Pick 3)) |
| `highest-frequency` | 130 | 58 | 45.9 | 0.45/draw | +1.89 | 2 (Mega Millions) |
| `birthday` | 17 | 9 | 6.1 | 0.53/draw | +1.24 | 2 (Powerball) |
| `benford` | 17 | 9 | 6.1 | 0.53/draw | +1.24 | 3 (Mega Millions) |
| `random` | 166 | 67 | 58.6 | 0.40/draw | +1.15 | 2 (Mega Millions) |
| `positional` | 137 | 54 | 48.2 | 0.39/draw | +0.88 | 2 (NY Win 4) |
| `skiphit` | 97 | 39 | 34.2 | 0.40/draw | +0.86 | 2 (NY Win 4) |
| `persistent` | 97 | 37 | 34.2 | 0.38/draw | +0.50 | 2 (NY Numbers (Pick 3)) |
| `hot` | 166 | 62 | 58.6 | 0.37/draw | +0.46 | 3 (NY Numbers (Pick 3)) |
| `numerology` | 97 | 36 | 34.2 | 0.37/draw | +0.32 | 2 (NY Numbers (Pick 3)) |
| `antibalanced` | 17 | 6 | 6.1 | 0.35/draw | -0.05 | 1 (Powerball) |
| `llm-tuned` | 79 | 27 | 27.9 | 0.34/draw | -0.18 | 3 (NY Win 4) |
| `unpopular` | 29 | 9 | 10.4 | 0.31/draw | -0.48 | 2 (Mega Millions) |
| `balanced` | 17 | 5 | 6.1 | 0.29/draw | -0.49 | 2 (Mega Millions) |
| `moonphase` | 97 | 31 | 34.2 | 0.32/draw | -0.58 | 2 (NY Win 4) |
| `delta` | 29 | 8 | 10.4 | 0.28/draw | -0.81 | 1 (Powerball) |
| `cold` | 166 | 51 | 58.6 | 0.31/draw | -1.06 | 3 (NY Win 4) |
| `llm-fewshot` | 156 | 47 | 55.1 | 0.30/draw | -1.16 | 3 (NY Win 4) |
| `dreambook` | 80 | 20 | 28.1 | 0.25/draw | -1.61 | 2 (NY Numbers (Pick 3)) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-09-02 14:38 UTC</sub>
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
