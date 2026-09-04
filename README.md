# 🎰 Lottery Guru

[![Live dashboard](https://img.shields.io/badge/📊_live_dashboard-gitchrisqueen.github.io%2Flottery--guru-4056a1)](https://gitchrisqueen.github.io/lottery-guru/)
[![Deploy dashboard](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/pages.yml/badge.svg)](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/pages.yml)
[![Daily prediction loop](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/daily.yml/badge.svg)](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/daily.yml)

**📊 [View the live dashboard →](https://gitchrisqueen.github.io/lottery-guru/)** — sortable leaderboards, today's picks, and the exploit watch, rebuilt after every daily loop.

An automated, honest lottery-prediction experiment. It is a measurement
harness first: every arm — folk method, LLM, or fine-tuned model — is scored
against exact chance, and the expected finding is that nothing beats it.

## What this measures

**The null-hypothesis scorer.** Lottery draws are independent uniform samples,
so the number of matches a ticket scores has an exact distribution under
chance. For jackpot games, white-ball matches are hypergeometric (Powerball:
5 picks from 69, so chance expects 25/69 ≈ 0.362 matches per ticket); for
digit games, per-position matches are Binomial(k, 1/10). Every day the loop
scores yesterday's predictions against the real drawings, sums observed
matches per (strategy, game) arm, and reports the cumulative
z = (observed − expected) / √(n · variance) with a two-sided p. The
[leaderboard](REPORT.md) is that table, one section per game, never pooled
across rule eras. Arms with fewer than 50 scored draws are marked
_(n<50, not yet interpretable)_ rather than ranked as if a lucky week meant
something. The math lives in
[`evaluation/scoring.py`](src/lottery_guru/evaluation/scoring.py) and is
checked against the exact hypergeometric PMF in the tests.

**No arm is expected to beat chance.** The folk methods (`hot`, `cold`,
`delta`, `numerology`, …) are here to be falsified with real data, and the
`llm-fewshot` and `llm-tuned` arms exist for exactly the same reason: they are
hypotheses, scored against the same null with no special treatment, and we
expect them to converge to z ≈ 0 like everything else. Watching that
convergence happen is the result.

## How the loop runs

Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus the LLM arms
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates the leaderboard** ([REPORT.md](REPORT.md)) comparing every arm to the exact null hypothesis

Periodically, an **LLM fine-tuning loop** (Fireworks LoRA monthly, or MLX
locally on Apple Silicon) trains on the accumulated history so the `llm-tuned`
arm can be scored — and, we expect, falsified — like every other arm. It
measures whether predictions "improve" with training; the honest expectation
is that they do not.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-09-04

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Mega Millions**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `03` `04` `27` `38` `39` + `05` |
| `balanced` | `06` `18` `24` `35` `69` + `24` |
| `benford` | `03` `12` `15` `25` `49` + `08` |
| `birthday` | `03` `04` `05` `18` `28` + `04` |
| `cold` | `06` `11` `28` `58` `69` + `18` |
| `contrarian` | `01` `10` `47` `50` `55` + `17` |
| `delta` | `07` `30` `48` `56` `60` + `06` |
| `highest-frequency` | `04` `18` `39` `42` `60` + `17` |
| `hot` | `42` `49` `56` `59` `63` + `12` |
| `llm-fewshot` | `07` `21` `25` `31` `42` + `12` |
| `moonphase` | `18` `26` `39` `58` `65` + `09` |
| `numerology` | `04` `10` `12` `20` `24` + `03` |
| `persistent` | `01` `09` `37` `38` `39` + `22` |
| `random` | `20` `38` `40` `60` `62` + `17` |
| `skiphit` | `22` `23` `42` `51` `61` + `11` |
| `unpopular` | `39` `41` `56` `60` `65` + `14` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `5` `7` |
| `contrarian` | `1` `1` `3` |
| `dreambook` | `9` `6` `9` |
| `highest-frequency` | `3` `1` `7` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `7` `4` `5` |
| `moonphase` | `3` `5` `5` |
| `numerology` | `1` `1` `7` |
| `persistent` | `4` `3` `3` |
| `positional` | `5` `8` `6` |
| `random` | `3` `9` `1` |
| `skiphit` | `3` `1` `4` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `5` `7` |
| `contrarian` | `3` `1` `4` |
| `dreambook` | `5` `2` `3` |
| `highest-frequency` | `6` `1` `4` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `2` `0` `8` |
| `moonphase` | `6` `7` `7` |
| `numerology` | `1` `1` `7` |
| `persistent` | `4` `3` `3` |
| `positional` | `6` `2` `0` |
| `random` | `6` `8` `4` |
| `skiphit` | `3` `1` `4` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `7` `5` `2` |
| `contrarian` | `6` `3` `1` `4` |
| `dreambook` | `9` `3` `9` `1` |
| `highest-frequency` | `9` `3` `6` `2` |
| `hot` | `9` `8` `3` `2` |
| `llm-fewshot` | `8` `1` `3` `2` |
| `moonphase` | `6` `8` `9` `2` |
| `numerology` | `1` `1` `7` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `4` `8` `0` `2` |
| `random` | `1` `9` `4` `3` |
| `skiphit` | `4` `3` `6` `4` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `7` `5` `2` |
| `contrarian` | `4` `0` `1` `0` |
| `dreambook` | `2` `1` `5` `2` |
| `highest-frequency` | `9` `1` `5` `2` |
| `hot` | `9` `8` `3` `2` |
| `llm-fewshot` | `1` `7` `9` `0` |
| `moonphase` | `6` `5` `2` `5` |
| `numerology` | `1` `1` `7` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `9` `1` `4` `7` |
| `random` | `7` `5` `5` `4` |
| `skiphit` | `6` `3` `6` `4` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `02` `06` `24` `28` `34` |
| `balanced` | `12` `15` `18` `23` `33` |
| `benford` | `04` `15` `17` `27` `31` |
| `birthday` | `04` `08` `11` `17` `25` |
| `cold` | `15` `18` `23` `29` `34` |
| `contrarian` | `04` `08` `10` `30` `32` |
| `delta` | `05` `08` `12` `15` `26` |
| `highest-frequency` | `04` `08` `15` `17` `18` |
| `hot` | `03` `18` `21` `24` `28` |
| `llm-fewshot` | `01` `03` `05` `17` `19` |
| `moonphase` | `02` `07` `08` `34` `35` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `01` `03` `08` `18` `22` |
| `skiphit` | `04` `17` `30` `33` `36` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `03` `04` `12` `17` |
| `balanced` | `12` `13` `19` `26` `31` |
| `benford` | `05` `10` `15` `29` `30` |
| `birthday` | `03` `06` `09` `18` `28` |
| `cold` | `11` `14` `25` `30` `34` |
| `contrarian` | `03` `09` `16` `22` `25` |
| `delta` | `15` `16` `18` `20` `21` |
| `highest-frequency` | `03` `12` `16` `24` `32` |
| `hot` | `07` `24` `30` `32` `35` |
| `llm-fewshot` | `06` `12` `16` `26` `31` |
| `moonphase` | `07` `17` `23` `27` `33` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `11` `12` `16` `27` `32` |
| `skiphit` | `03` `08` `24` `31` `32` |

**FL Jackpot Triple Play**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `28` `31` `36` `40` `45` `46` |
| `balanced` | `02` `06` `21` `29` `36` `39` |
| `benford` | `05` `12` `17` `25` `39` `41` |
| `birthday` | `02` `06` `10` `12` `13` `22` |
| `cold` | `18` `29` `34` `39` `40` `41` |
| `contrarian` | `02` `03` `09` `33` `42` `44` |
| `delta` | `01` `08` `11` `14` `29` `42` |
| `highest-frequency` | `02` `06` `10` `12` `36` `46` |
| `hot` | `05` `12` `24` `31` `45` `46` |
| `llm-fewshot` | `06` `16` `17` `23` `32` `45` |
| `moonphase` | `06` `14` `18` `31` `35` `36` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `01` `04` `10` `18` `21` `29` |
| `random` | `02` `17` `30` `34` `42` `46` |
| `skiphit` | `10` `21` `35` `37` `43` `44` |
| `unpopular` | `20` `24` `34` `43` `44` `46` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `9` |
| `contrarian` | `4` `4` |
| `dreambook` | `6` `1` |
| `highest-frequency` | `1` `1` |
| `hot` | `3` `8` |
| `llm-fewshot` | `0` `8` |
| `moonphase` | `6` `4` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `9` `6` |
| `random` | `1` `0` |
| `skiphit` | `4` `5` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `1` |
| `contrarian` | `1` `0` |
| `dreambook` | `7` `9` |
| `highest-frequency` | `1` `1` |
| `hot` | `1` `9` |
| `llm-fewshot` | `7` `2` |
| `moonphase` | `3` `0` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `9` `3` |
| `random` | `7` `8` |
| `skiphit` | `6` `5` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `1` `2` |
| `contrarian` | `0` `7` `8` |
| `dreambook` | `7` `4` `2` |
| `highest-frequency` | `8` `1` `2` |
| `hot` | `8` `7` `9` |
| `llm-fewshot` | `3` `2` `4` |
| `moonphase` | `6` `5` `5` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `9` `1` `8` |
| `random` | `8` `1` `3` |
| `skiphit` | `4` `6` `2` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `1` `7` |
| `contrarian` | `8` `4` `3` |
| `dreambook` | `7` `4` `2` |
| `highest-frequency` | `8` `1` `4` |
| `hot` | `4` `0` `6` |
| `llm-fewshot` | `2` `9` `0` |
| `moonphase` | `9` `5` `4` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `6` `6` `5` |
| `random` | `2` `9` `4` |
| `skiphit` | `3` `8` `3` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `8` `1` `9` |
| `contrarian` | `8` `8` `3` `9` |
| `dreambook` | `2` `4` `3` `2` |
| `highest-frequency` | `4` `4` `3` `5` |
| `hot` | `0` `9` `6` `3` |
| `llm-fewshot` | `4` `2` `9` `6` |
| `moonphase` | `4` `6` `4` `0` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `0` `6` `2` `6` |
| `random` | `7` `7` `5` `7` |
| `skiphit` | `4` `1` `3` `1` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `9` `6` `3` |
| `contrarian` | `9` `8` `5` `2` |
| `dreambook` | `0` `0` `1` `2` |
| `highest-frequency` | `0` `4` `1` `5` |
| `hot` | `1` `2` `3` `5` |
| `llm-fewshot` | `8` `4` `4` `9` |
| `moonphase` | `5` `6` `4` `9` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `4` `3` `0` `6` |
| `random` | `3` `3` `2` `6` |
| `skiphit` | `3` `2` `2` `7` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `6` `8` `4` `9` |
| `contrarian` | `8` `9` `9` `4` `2` |
| `dreambook` | `9` `8` `0` `0` `2` |
| `highest-frequency` | `7` `8` `6` `4` `2` |
| `hot` | `5` `8` `6` `3` `2` |
| `llm-fewshot` | `7` `2` `4` `9` `8` |
| `moonphase` | `6` `3` `9` `2` `2` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `8` `2` `8` `0` `5` |
| `random` | `7` `8` `0` `5` `6` |
| `skiphit` | `5` `3` `7` `2` `0` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `5` `8` `0` `7` |
| `contrarian` | `8` `9` `7` `9` `8` |
| `dreambook` | `4` `5` `2` `3` `4` |
| `highest-frequency` | `7` `1` `5` `4` `4` |
| `hot` | `7` `4` `0` `8` `6` |
| `llm-fewshot` | `7` `6` `4` `4` `1` |
| `moonphase` | `9` `0` `9` `6` `1` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `8` `1` `5` `2` `9` |
| `random` | `4` `7` `5` `4` `5` |
| `skiphit` | `7` `1` `6` `0` `5` |

<sub>Updated 2026-09-04 14:32 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**1803** predictions scored across **41** days. Combined, they've hit **666** numbers where pure chance predicts **637.0** (z = **+1.21**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `contrarian` | 106 | 55 | 37.4 | 0.52/draw | +3.04 | 2 (NY Numbers (Pick 3)) |
| `random` | 175 | 73 | 61.8 | 0.42/draw | +1.50 | 2 (Mega Millions) |
| `highest-frequency` | 139 | 59 | 49.0 | 0.42/draw | +1.50 | 2 (Mega Millions) |
| `numerology` | 106 | 45 | 37.4 | 0.42/draw | +1.32 | 3 (NY Numbers (Pick 3)) |
| `skiphit` | 106 | 44 | 37.4 | 0.42/draw | +1.14 | 3 (NY Win 4) |
| `birthday` | 18 | 9 | 6.5 | 0.50/draw | +1.06 | 2 (Powerball) |
| `benford` | 18 | 9 | 6.5 | 0.50/draw | +1.06 | 3 (Mega Millions) |
| `positional` | 145 | 57 | 51.0 | 0.39/draw | +0.89 | 2 (NY Win 4) |
| `persistent` | 106 | 40 | 37.4 | 0.38/draw | +0.45 | 2 (NY Numbers (Pick 3)) |
| `hot` | 175 | 64 | 61.8 | 0.37/draw | +0.29 | 3 (NY Numbers (Pick 3)) |
| `llm-tuned` | 79 | 27 | 27.9 | 0.34/draw | -0.18 | 3 (NY Win 4) |
| `antibalanced` | 18 | 6 | 6.5 | 0.33/draw | -0.20 | 1 (Powerball) |
| `unpopular` | 30 | 9 | 10.8 | 0.30/draw | -0.59 | 2 (Mega Millions) |
| `balanced` | 18 | 5 | 6.5 | 0.28/draw | -0.62 | 2 (Mega Millions) |
| `moonphase` | 106 | 33 | 37.4 | 0.31/draw | -0.76 | 2 (NY Win 4) |
| `delta` | 30 | 8 | 10.8 | 0.27/draw | -0.91 | 1 (Powerball) |
| `llm-fewshot` | 165 | 50 | 58.3 | 0.30/draw | -1.15 | 3 (NY Win 4) |
| `cold` | 175 | 51 | 61.8 | 0.29/draw | -1.45 | 3 (NY Win 4) |
| `dreambook` | 88 | 22 | 30.9 | 0.25/draw | -1.69 | 2 (NY Numbers (Pick 3)) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-09-04 14:32 UTC</sub>
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
