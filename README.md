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
### 🎟️ Predictions for 2026-08-22

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Powerball**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `07` `11` `12` `21` `59` + `19` |
| `balanced` | `09` `19` `35` `56` `64` + `12` |
| `benford` | `03` `13` `19` `24` `55` + `01` |
| `birthday` | `01` `05` `08` `09` `26` + `19` |
| `cold` | `11` `23` `33` `51` `52` + `19` |
| `contrarian` | `05` `08` `15` `49` `65` + `22` |
| `delta` | `12` `19` `24` `30` `34` + `03` |
| `highest-frequency` | `12` `19` `23` `24` `56` + `19` |
| `hot` | `21` `36` `56` `63` `64` + `14` |
| `llm-fewshot` | `04` `30` `35` `55` `69` + `12` |
| `llm-tuned` | `16` `23` `27` `48` `51` + `13` |
| `moonphase` | `26` `27` `40` `48` `50` + `08` |
| `numerology` | `10` `12` `20` `24` `36` + `11` |
| `persistent` | `13` `21` `23` `32` `66` + `01` |
| `random` | `07` `14` `24` `47` `49` + `16` |
| `skiphit` | `04` `10` `15` `58` `61` + `02` |
| `unpopular` | `35` `50` `56` `57` `68` + `16` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `8` `3` |
| `contrarian` | `2` `4` `5` |
| `dreambook` | `0` `6` `2` |
| `highest-frequency` | `1` `8` `6` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `9` `1` `6` |
| `llm-tuned` | `1` `8` `0` |
| `moonphase` | `1` `3` `4` |
| `numerology` | `1` `1` `6` |
| `persistent` | `4` `3` `3` |
| `positional` | `1` `8` `6` |
| `random` | `5` `7` `2` |
| `skiphit` | `2` `7` `1` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `8` `3` |
| `contrarian` | `2` `2` `1` |
| `dreambook` | `0` `8` `5` |
| `highest-frequency` | `2` `8` `1` |
| `hot` | `5` `8` `2` |
| `llm-fewshot` | `3` `0` `2` |
| `llm-tuned` | `7` `1` `4` |
| `moonphase` | `4` `6` `7` |
| `numerology` | `1` `1` `6` |
| `persistent` | `4` `3` `3` |
| `positional` | `8` `6` `1` |
| `random` | `2` `3` `0` |
| `skiphit` | `2` `7` `1` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `6` `8` `1` |
| `contrarian` | `7` `9` `5` `0` |
| `dreambook` | `0` `2` `4` `7` |
| `highest-frequency` | `7` `7` `5` `5` |
| `hot` | `8` `3` `5` `9` |
| `llm-fewshot` | `7` `6` `7` `5` |
| `llm-tuned` | `6` `7` `1` `6` |
| `moonphase` | `0` `7` `2` `7` |
| `numerology` | `1` `1` `6` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `6` `7` `9` `2` |
| `random` | `4` `0` `7` `3` |
| `skiphit` | `7` `7` `5` `8` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `6` `1` `8` |
| `contrarian` | `1` `7` `4` `8` |
| `dreambook` | `9` `4` `1` `6` |
| `highest-frequency` | `1` `4` `1` `4` |
| `hot` | `8` `3` `5` `9` |
| `llm-fewshot` | `4` `4` `6` `4` |
| `llm-tuned` | `5` `1` `1` `4` |
| `moonphase` | `7` `4` `7` `3` |
| `numerology` | `1` `1` `6` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `8` `3` `5` `2` |
| `random` | `9` `7` `7` `4` |
| `skiphit` | `1` `7` `4` `3` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `14` `23` `27` `32` `35` |
| `balanced` | `01` `04` `20` `25` `28` |
| `benford` | `04` `05` `11` `23` `34` |
| `birthday` | `03` `06` `07` `10` `23` |
| `cold` | `03` `07` `08` `16` `28` |
| `contrarian` | `09` `15` `17` `20` `32` |
| `delta` | `04` `08` `15` `28` `32` |
| `highest-frequency` | `07` `14` `20` `28` `35` |
| `hot` | `03` `16` `21` `24` `29` |
| `llm-fewshot` | `07` `12` `14` `30` `36` |
| `llm-tuned` | `01` `14` `21` `30` `35` |
| `moonphase` | `10` `14` `26` `34` `35` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `02` `19` `21` `31` `35` |
| `skiphit` | `01` `07` `20` `28` `31` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `09` `21` `28` `33` `36` |
| `balanced` | `06` `08` `13` `31` `32` |
| `benford` | `05` `14` `18` `26` `35` |
| `birthday` | `01` `04` `07` `09` `10` |
| `cold` | `15` `16` `17` `25` `33` |
| `contrarian` | `04` `09` `19` `26` `30` |
| `delta` | `11` `13` `16` `19` `21` |
| `highest-frequency` | `08` `10` `14` `16` `33` |
| `hot` | `03` `08` `10` `16` `28` |
| `llm-fewshot` | `04` `05` `11` `14` `29` |
| `llm-tuned` | `01` `02` `18` `24` `34` |
| `moonphase` | `08` `12` `20` `27` `33` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `14` `15` `20` `28` `34` |
| `skiphit` | `02` `06` `17` `18` `24` |

**Florida Lotto**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `28` `35` `37` `39` `44` `50` |
| `balanced` | `06` `08` `21` `25` `42` `51` |
| `benford` | `03` `11` `17` `25` `48` `53` |
| `birthday` | `05` `06` `13` `16` `25` `28` |
| `cold` | `02` `04` `14` `20` `39` `41` |
| `contrarian` | `03` `15` `16` `20` `44` `47` |
| `delta` | `06` `17` `30` `34` `48` `53` |
| `highest-frequency` | `03` `05` `06` `16` `39` `53` |
| `hot` | `01` `12` `13` `19` `22` `23` |
| `llm-fewshot` | `05` `15` `24` `26` `40` `43` |
| `llm-tuned` | `01` `02` `03` `04` `05` `06` |
| `moonphase` | `01` `23` `38` `41` `43` `53` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `05` `10` `32` `33` `38` `50` |
| `random` | `03` `09` `23` `40` `43` `45` |
| `skiphit` | `09` `11` `16` `28` `49` `53` |
| `unpopular` | `14` `39` `42` `44` `48` `49` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `8` |
| `contrarian` | `7` `7` |
| `dreambook` | `6` `0` |
| `highest-frequency` | `5` `8` |
| `hot` | `5` `8` |
| `llm-fewshot` | `6` `6` |
| `llm-tuned` | `3` `4` |
| `moonphase` | `7` `4` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `5` `5` |
| `random` | `5` `3` |
| `skiphit` | `9` `8` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `4` |
| `contrarian` | `5` `6` |
| `dreambook` | `3` `4` |
| `highest-frequency` | `1` `1` |
| `hot` | `2` `7` |
| `llm-fewshot` | `3` `6` |
| `llm-tuned` | `5` `0` |
| `moonphase` | `6` `1` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `4` `9` |
| `random` | `2` `7` |
| `skiphit` | `1` `5` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `3` `9` |
| `contrarian` | `7` `1` `4` |
| `dreambook` | `4` `9` `9` |
| `highest-frequency` | `4` `1` `4` |
| `hot` | `4` `2` `6` |
| `llm-fewshot` | `4` `3` `5` |
| `llm-tuned` | `1` `1` `1` |
| `moonphase` | `0` `2` `0` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `9` `8` `4` |
| `random` | `5` `1` `6` |
| `skiphit` | `9` `6` `5` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `4` `0` |
| `contrarian` | `1` `3` `4` |
| `dreambook` | `6` `2` `7` |
| `highest-frequency` | `6` `4` `5` |
| `hot` | `6` `1` `4` |
| `llm-fewshot` | `6` `9` `5` |
| `llm-tuned` | `6` `3` `2` |
| `moonphase` | `3` `4` `1` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `1` `3` `6` |
| `random` | `8` `4` `5` |
| `skiphit` | `2` `4` `5` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `4` `6` `2` |
| `contrarian` | `1` `6` `4` `0` |
| `dreambook` | `2` `0` `2` `5` |
| `highest-frequency` | `2` `4` `6` `5` |
| `hot` | `5` `8` `9` `1` |
| `llm-fewshot` | `1` `0` `3` `3` |
| `llm-tuned` | `9` `5` `6` `6` |
| `moonphase` | `2` `4` `0` `0` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `3` `5` `6` `4` |
| `random` | `7` `4` `6` `6` |
| `skiphit` | `3` `4` `0` `2` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `3` `2` `0` |
| `contrarian` | `2` `2` `5` `5` |
| `dreambook` | `2` `0` `5` `3` |
| `highest-frequency` | `1` `3` `1` `5` |
| `hot` | `1` `8` `2` `9` |
| `llm-fewshot` | `5` `0` `0` `1` |
| `llm-tuned` | `5` `3` `4` `8` |
| `moonphase` | `1` `8` `8` `7` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `1` `7` `9` `5` |
| `random` | `8` `3` `6` `5` |
| `skiphit` | `5` `7` `1` `2` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `1` `3` `7` `0` |
| `contrarian` | `3` `1` `1` `6` `5` |
| `dreambook` | `2` `3` `7` `7` `1` |
| `highest-frequency` | `2` `1` `1` `6` `4` |
| `hot` | `0` `4` `3` `7` `1` |
| `llm-fewshot` | `6` `8` `5` `8` `6` |
| `llm-tuned` | `4` `7` `6` `6` `9` |
| `moonphase` | `2` `1` `6` `5` `5` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `1` `6` `1` `9` `7` |
| `random` | `3` `5` `9` `6` `4` |
| `skiphit` | `3` `9` `4` `5` `9` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `2` `0` `8` `4` |
| `contrarian` | `9` `1` `3` `4` `3` |
| `dreambook` | `2` `4` `4` `7` `4` |
| `highest-frequency` | `7` `1` `4` `4` `4` |
| `hot` | `0` `3` `4` `1` `5` |
| `llm-fewshot` | `8` `5` `2` `9` `1` |
| `llm-tuned` | `5` `3` `0` `3` `8` |
| `moonphase` | `7` `5` `5` `4` `7` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `7` `5` `4` `2` `5` |
| `random` | `3` `1` `4` `4` `4` |
| `skiphit` | `1` `7` `2` `2` `7` |

<sub>Updated 2026-08-22 10:52 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**1068** predictions scored across **28** days. Combined, they've hit **419** numbers where pure chance predicts **377.0** (z = **+2.29**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `highest-frequency` | 82 | 44 | 28.9 | 0.54/draw | +2.97 | 2 (Mega Millions) |
| `contrarian` | 49 | 27 | 17.2 | 0.55/draw | +2.48 | 2 (NY Numbers (Pick 3)) |
| `birthday` | 9 | 6 | 3.2 | 0.67/draw | +1.64 | 2 (Powerball) |
| `benford` | 9 | 6 | 3.2 | 0.67/draw | +1.64 | 3 (Mega Millions) |
| `persistent` | 49 | 23 | 17.2 | 0.47/draw | +1.47 | 2 (NY Numbers (Pick 3)) |
| `positional` | 97 | 42 | 34.1 | 0.43/draw | +1.43 | 2 (NY Win 4) |
| `numerology` | 49 | 22 | 17.2 | 0.45/draw | +1.21 | 2 (NY Numbers (Pick 3)) |
| `random` | 118 | 48 | 41.7 | 0.41/draw | +1.04 | 2 (Mega Millions) |
| `skiphit` | 49 | 21 | 17.2 | 0.43/draw | +0.96 | 2 (NY Win 4) |
| `llm-tuned` | 64 | 25 | 22.6 | 0.39/draw | +0.53 | 3 (NY Win 4) |
| `delta` | 21 | 8 | 7.6 | 0.38/draw | +0.17 | 1 (Powerball) |
| `hot` | 118 | 42 | 41.7 | 0.36/draw | +0.06 | 3 (NY Numbers (Pick 3)) |
| `balanced` | 9 | 3 | 3.2 | 0.33/draw | -0.14 | 2 (Mega Millions) |
| `antibalanced` | 9 | 3 | 3.2 | 0.33/draw | -0.14 | 1 (Powerball) |
| `dreambook` | 40 | 12 | 14.0 | 0.30/draw | -0.56 | 2 (NY Numbers (Pick 3)) |
| `moonphase` | 49 | 15 | 17.2 | 0.31/draw | -0.57 | 2 (NY Win 4) |
| `cold` | 118 | 38 | 41.7 | 0.32/draw | -0.60 | 3 (NY Win 4) |
| `unpopular` | 21 | 4 | 7.6 | 0.19/draw | -1.39 | 2 (Mega Millions) |
| `llm-fewshot` | 108 | 30 | 38.1 | 0.28/draw | -1.39 | 2 (NY Win 4) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-08-22 10:52 UTC</sub>
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
