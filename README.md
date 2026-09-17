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
[leaderboard](REPORT.md) is that table, one section per game with scored
results (Powerball, Mega Millions, NY Numbers, NY Win 4 today; the Florida games
have no scored draws yet), never pooled across rule eras. Arms with fewer than 50 scored draws are marked
_(n<50, not yet interpretable)_ rather than ranked as if a lucky week meant
something. The math lives in
[`evaluation/scoring.py`](src/lottery_guru/evaluation/scoring.py) and its
hypergeometric and binomial moments are checked in
[`tests/test_scoring.py`](tests/test_scoring.py).

**No arm is expected to beat chance.** The folk methods (`hot`, `cold`,
`delta`, `numerology`, …) are here to be falsified with real data, and the
`llm-fewshot` and `llm-tuned` arms exist for exactly the same reason: they are
hypotheses, scored against the same null with no special treatment, and we
expect them to converge to z ≈ 0 like everything else. Watching that
convergence happen is the result.

## How the loop runs

Every day it:

1. **Pulls real drawing results** for Powerball, Mega Millions, NY Numbers and NY Win 4 from NY Open Data, and attempts the same for Florida's Fantasy 5, Lotto, Jackpot Triple Play and Pick 2–5 from the Florida Lottery's PDF history files. As of 2026-09-04 no Florida result has landed: every scheduled run since 2026-08-10 fails the Florida fetch on both hosts — a TLS handshake error on most days, a connect timeout on the rest (see the [run log](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/daily.yml)) — so Florida arms are predicted but not yet scored
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
### 🎟️ Predictions for 2026-09-17

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `4` `9` |
| `contrarian` | `9` `3` `0` |
| `dreambook` | `0` `0` `1` |
| `highest-frequency` | `9` `3` `3` |
| `hot` | `5` `8` `3` |
| `llm-fewshot` | `9` `4` `3` |
| `moonphase` | `9` `1` `8` |
| `numerology` | `1` `1` `1` |
| `persistent` | `4` `3` `3` |
| `positional` | `3` `8` `3` |
| `random` | `9` `0` `5` |
| `skiphit` | `2` `3` `8` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `4` `6` |
| `contrarian` | `9` `3` `5` |
| `dreambook` | `9` `4` `0` |
| `highest-frequency` | `5` `3` `3` |
| `hot` | `5` `8` `3` |
| `llm-fewshot` | `8` `7` `0` |
| `moonphase` | `5` `5` `4` |
| `numerology` | `1` `1` `1` |
| `persistent` | `4` `3` `3` |
| `positional` | `7` `2` `3` |
| `random` | `6` `4` `9` |
| `skiphit` | `2` `3` `3` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `9` `6` `2` |
| `contrarian` | `1` `4` `7` `4` |
| `dreambook` | `9` `4` `1` `6` |
| `highest-frequency` | `1` `9` `7` `4` |
| `hot` | `8` `9` `4` `2` |
| `llm-fewshot` | `3` `9` `7` `6` |
| `moonphase` | `4` `5` `7` `2` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `9` `1` `4` `4` |
| `random` | `2` `9` `7` `4` |
| `skiphit` | `5` `7` `7` `3` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `9` `6` `2` |
| `contrarian` | `1` `2` `7` `3` |
| `dreambook` | `7` `4` `2` `9` |
| `highest-frequency` | `1` `9` `7` `2` |
| `hot` | `8` `9` `4` `2` |
| `llm-fewshot` | `7` `5` `7` `0` |
| `moonphase` | `4` `5` `0` `7` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `5` `4` `3` `2` |
| `random` | `0` `0` `8` `7` |
| `skiphit` | `1` `7` `7` `3` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `06` `11` `13` `21` |
| `balanced` | `06` `16` `17` `19` `35` |
| `benford` | `01` `04` `10` `26` `32` |
| `birthday` | `01` `02` `04` `07` `11` |
| `cold` | `11` `14` `22` `28` `34` |
| `contrarian` | `03` `15` `23` `24` `25` |
| `delta` | `09` `13` `27` `34` `36` |
| `highest-frequency` | `01` `10` `13` `24` `35` |
| `hot` | `01` `09` `12` `30` `35` |
| `llm-fewshot` | `09` `10` `21` `24` `35` |
| `moonphase` | `05` `07` `24` `29` `31` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `06` `10` `17` `19` `23` |
| `skiphit` | `02` `03` `13` `18` `24` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `06` `07` `15` `25` |
| `balanced` | `08` `11` `17` `31` `32` |
| `benford` | `04` `16` `17` `23` `30` |
| `birthday` | `01` `06` `07` `24` `27` |
| `cold` | `03` `10` `19` `29` `31` |
| `contrarian` | `03` `05` `06` `23` `24` |
| `delta` | `03` `12` `23` `24` `27` |
| `highest-frequency` | `03` `07` `23` `24` `30` |
| `hot` | `04` `07` `23` `24` `33` |
| `llm-fewshot` | `04` `17` `19` `21` `33` |
| `moonphase` | `03` `05` `30` `31` `35` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `07` `13` `16` `25` `30` |
| `skiphit` | `12` `15` `17` `23` `30` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `6` |
| `contrarian` | `1` `6` |
| `dreambook` | `4` `5` |
| `highest-frequency` | `1` `1` |
| `hot` | `3` `1` |
| `llm-fewshot` | `1` `2` |
| `moonphase` | `2` `0` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `9` `4` |
| `random` | `1` `7` |
| `skiphit` | `7` `5` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `6` |
| `contrarian` | `5` `4` |
| `dreambook` | `5` `3` |
| `highest-frequency` | `4` `3` |
| `hot` | `4` `9` |
| `llm-fewshot` | `3` `9` |
| `moonphase` | `2` `3` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `9` `2` |
| `random` | `4` `5` |
| `skiphit` | `1` `2` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `8` `2` |
| `contrarian` | `9` `0` `9` |
| `dreambook` | `2` `3` `6` |
| `highest-frequency` | `6` `8` `6` |
| `hot` | `9` `5` `6` |
| `llm-fewshot` | `6` `7` `7` |
| `moonphase` | `0` `1` `7` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `6` `0` `6` |
| `random` | `4` `8` `8` |
| `skiphit` | `2` `4` `5` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `9` `4` |
| `contrarian` | `9` `1` `3` |
| `dreambook` | `9` `9` `0` |
| `highest-frequency` | `9` `3` `0` |
| `hot` | `6` `2` `0` |
| `llm-fewshot` | `3` `0` `1` |
| `moonphase` | `8` `3` `0` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `7` `4` `0` |
| `random` | `3` `7` `0` |
| `skiphit` | `9` `3` `4` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `6` `4` `1` |
| `contrarian` | `5` `1` `6` `1` |
| `dreambook` | `2` `5` `9` `3` |
| `highest-frequency` | `5` `1` `6` `1` |
| `hot` | `0` `4` `8` `9` |
| `llm-fewshot` | `7` `7` `5` `7` |
| `moonphase` | `0` `0` `7` `4` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `6` `2` `7` `7` |
| `random` | `5` `1` `6` `1` |
| `skiphit` | `5` `0` `1` `7` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `5` `0` `4` |
| `contrarian` | `8` `5` `7` `2` |
| `dreambook` | `0` `6` `0` `0` |
| `highest-frequency` | `8` `4` `6` `5` |
| `hot` | `9` `5` `2` `3` |
| `llm-fewshot` | `4` `8` `7` `1` |
| `moonphase` | `4` `4` `2` `0` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `3` `4` `6` `9` |
| `random` | `8` `9` `3` `5` |
| `skiphit` | `5` `1` `6` `5` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `4` `7` `0` `9` |
| `contrarian` | `6` `6` `5` `7` `4` |
| `dreambook` | `9` `6` `6` `7` `5` |
| `highest-frequency` | `2` `6` `7` `7` `4` |
| `hot` | `2` `5` `4` `7` `0` |
| `llm-fewshot` | `5` `6` `3` `0` `4` |
| `moonphase` | `8` `1` `3` `5` `7` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `2` `3` `7` `4` `9` |
| `random` | `6` `6` `7` `3` `0` |
| `skiphit` | `3` `3` `0` `1` `9` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `7` `3` `4` `0` |
| `contrarian` | `7` `3` `5` `6` `8` |
| `dreambook` | `3` `9` `0` `9` `3` |
| `highest-frequency` | `3` `1` `6` `1` `0` |
| `hot` | `5` `6` `4` `7` `0` |
| `llm-fewshot` | `1` `6` `6` `1` `9` |
| `moonphase` | `4` `9` `9` `2` `2` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `6` `0` `8` `3` `0` |
| `random` | `3` `7` `6` `7` `6` |
| `skiphit` | `0` `1` `0` `1` `0` |

<sub>Updated 2026-09-17 10:35 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**2503** predictions scored across **54** days. Combined, they've hit **890** numbers where pure chance predicts **887.9** (z = **+0.08**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `positional` | 190 | 79 | 67.1 | 0.42/draw | +1.53 | 3 (NY Win 4) |
| `contrarian` | 161 | 67 | 57.1 | 0.42/draw | +1.39 | 2 (NY Numbers (Pick 3)) |
| `random` | 230 | 93 | 81.5 | 0.40/draw | +1.34 | 2 (Mega Millions) |
| `numerology` | 161 | 64 | 57.1 | 0.40/draw | +0.97 | 3 (NY Numbers (Pick 3)) |
| `persistent` | 161 | 62 | 57.1 | 0.39/draw | +0.69 | 2 (NY Numbers (Pick 3)) |
| `highest-frequency` | 194 | 72 | 68.8 | 0.37/draw | +0.41 | 2 (Mega Millions) |
| `benford` | 28 | 11 | 10.1 | 0.39/draw | +0.31 | 3 (Mega Millions) |
| `birthday` | 28 | 10 | 10.1 | 0.36/draw | -0.03 | 2 (Powerball) |
| `antibalanced` | 28 | 10 | 10.1 | 0.36/draw | -0.03 | 2 (Powerball) |
| `hot` | 230 | 80 | 81.5 | 0.35/draw | -0.18 | 3 (NY Numbers (Pick 3)) |
| `llm-tuned` | 79 | 27 | 27.9 | 0.34/draw | -0.18 | 3 (NY Win 4) |
| `skiphit` | 161 | 54 | 57.1 | 0.34/draw | -0.43 | 3 (NY Win 4) |
| `unpopular` | 40 | 12 | 14.4 | 0.30/draw | -0.68 | 2 (Mega Millions) |
| `balanced` | 28 | 8 | 10.1 | 0.29/draw | -0.70 | 2 (Mega Millions) |
| `llm-fewshot` | 220 | 72 | 78.0 | 0.33/draw | -0.72 | 3 (NY Win 4) |
| `moonphase` | 161 | 50 | 57.1 | 0.31/draw | -0.99 | 2 (NY Win 4) |
| `cold` | 230 | 71 | 81.5 | 0.31/draw | -1.23 | 3 (NY Win 4) |
| `delta` | 40 | 10 | 14.4 | 0.25/draw | -1.24 | 1 (Powerball) |
| `dreambook` | 133 | 38 | 47.0 | 0.29/draw | -1.38 | 2 (NY Numbers (Pick 3)) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-09-17 10:35 UTC</sub>
<!-- SCOREBOARD:END -->

## The honest part

Lottery draws are independent uniform samples. Well-run lotteries consistently pass
uniformity tests (chi-square, gap, runs — see docs/RESEARCH.md), and no peer-reviewed work has ever demonstrated above-chance
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
| `delta` | sample empirical gaps between sorted winners (jackpot games) | chance |
| `positional` | per-position digit frequency (digit games) | chance |
| `unpopular` | avoid birthday/sequence combos to reduce jackpot splitting (jackpot games with room above 31) | same matches, better EV-if-win |
| `birthday` | the mirror of `unpopular`: deliberately popular 1–31 picks | chance, worse split |
| `contrarian` | play numbers that just hit (Clotfelter & Cook's under-bet numbers) | chance |
| `balanced` / `antibalanced` | the "winning tickets look average" sum/parity filter, and its inverse (jackpot games) | chance |
| `skiphit` | Gail Howard's skip-and-hit system, mechanized | chance |
| `benford` | score tickets by closeness to Benford's law — a deliberately wrong control (jackpot games) | chance |
| `persistent` | one fixed ticket per game, never changed (Lustig) | chance |
| `moonphase` | lunar phase folded into the seed — a seeded RNG in costume | chance |
| `numerology` | Pythagorean numerology from a fixed project persona plus the day | chance |
| `dreambook` | Harlem numbers-game dream-book lookup (digit games) | chance |
| `llm-fewshot` | LLM (Ollama Cloud by default) with recent-draw context, no training | chance |
| `llm-tuned` | LoRA-tuned on accumulated history, served from Fireworks (retrained monthly); local MLX adapters are evaluated offline with `finetune eval`, not scored as this arm | chance (measured rigorously) |
| `highest-frequency` | consensus: ranks numbers by how many *other arms* picked them for that same drawing | chance |

Which arms apply to which game is decided by `REGISTRY` in
[`strategies/__init__.py`](src/lottery_guru/strategies/__init__.py); each
strategy module's docstring carries the folk claim it exists to test.

## Quickstart

```bash
pip install -e ".[llm,dev]"

lottery-guru pull --limit 2000   # backfill history
lottery-guru predict             # today's predictions
lottery-guru score               # score anything whose results are in
lottery-guru report              # regenerate REPORT.md
```

`lottery-guru daily` runs all four and then `lottery-guru board`, which
renders the predictions board into [PREDICTIONS.md](PREDICTIONS.md) and the
section above. It's the GitHub Actions cron entry point
(`.github/workflows/daily.yml`, scheduled for 10:15 UTC, after NY Open Data's
nightly batch; GitHub starts scheduled runs late, often by hours — the
[run log](https://github.com/gitchrisqueen/lottery-guru/actions/workflows/daily.yml)
shows the actual start times). Predictions and scores are committed to the
repo: git is the database.

### LLM arm

Provider-pluggable, auto-detected from credentials:

- **Ollama Cloud** (default, cheap/free tier): create a key at
  [ollama.com/settings/keys](https://ollama.com/settings/keys) and set
  `OLLAMA_API_KEY` (as a repo secret for CI). Default model `gpt-oss:20b`;
  override with `LOTTERY_GURU_LLM_MODEL`.
- **Local Ollama**: set `OLLAMA_HOST=http://localhost:11434` — no key needed.
  Pointing `LOTTERY_GURU_LLM_MODEL` at any model your Ollama serves runs it as
  the `llm-fewshot` arm; there is no code path that scores an MLX adapter as
  `llm-tuned`.
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
  It does this only on days Powerball or Mega Millions draws
  (Mon/Tue/Wed/Fri/Sat — `TUNED_ARM_GAMES` in
  [`games.py`](src/lottery_guru/games.py)); Sundays and Thursdays have only
  the daily NY and Florida games, so the GPU stays off and the week costs
  five sessions instead of seven. Every other arm still predicts all seven
  days; only the paid arm is trimmed.

Setup: add the repo secret `FIREWORKS_API_KEY`
([fireworks.ai/settings/users/api-keys](https://app.fireworks.ai/settings/users/api-keys));
the account slug is auto-resolved from the key (set `FIREWORKS_ACCOUNT_ID` to
override). Training needs a Fireworks account tier with GPU quota; the
accelerator classes tried, in order, are listed in
[`finetune/fireworks.py`](src/lottery_guru/finetune/fireworks.py).

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
- **Florida Lottery PDF history files** — Florida has no open-data portal;
  the official machine-readable source is the per-game PDF at
  `files.floridalottery.com/exptkt/<stem>.pdf`, parsed with `pdfplumber`
  ([`data/florida.py`](src/lottery_guru/data/florida.py)). The fetch currently
  fails from GitHub Actions runners with an SSL handshake error on both hosts,
  so no Florida history is in `data/raw/` yet.
- **Texas Lottery CSVs** — used as an integrity cross-check on the most recent
  Powerball draws.

## Disclaimer

This is a statistics/ML measurement project, not gambling advice. Expected
value of every lottery ticket is strongly negative; nothing here changes that.
