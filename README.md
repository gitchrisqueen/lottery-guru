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
### 🎟️ Predictions for 2026-09-25

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Mega Millions**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `07` `11` `25` `41` `63` + `24` |
| `balanced` | `06` `27` `38` `40` `47` + `04` |
| `benford` | `12` `18` `23` `32` `46` + `03` |
| `birthday` | `05` `06` `07` `08` `12` + `03` |
| `cold` | `11` `15` `28` `64` `69` + `18` |
| `contrarian` | `04` `13` `37` `56` `58` + `08` |
| `delta` | `03` `27` `36` `41` `42` + `01` |
| `highest-frequency` | `07` `12` `27` `41` `56` + `03` |
| `hot` | `30` `48` `56` `59` `63` + `12` |
| `llm-fewshot` | `21` `44` `46` `62` `66` + `21` |
| `moonphase` | `08` `09` `18` `27` `66` + `03` |
| `numerology` | `07` `10` `12` `20` `24` + `06` |
| `persistent` | `01` `09` `37` `38` `39` + `22` |
| `random` | `01` `02` `24` `49` `62` + `09` |
| `skiphit` | `13` `55` `56` `58` `68` + `22` |
| `unpopular` | `37` `38` `39` `41` `61` + `23` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `9` `7` |
| `contrarian` | `2` `3` `0` |
| `dreambook` | `4` `9` `4` |
| `highest-frequency` | `2` `3` `1` |
| `hot` | `5` `0` `6` |
| `llm-fewshot` | `3` `5` `7` |
| `moonphase` | `9` `5` `4` |
| `numerology` | `1` `1` `1` |
| `persistent` | `4` `3` `3` |
| `positional` | `2` `2` `6` |
| `random` | `3` `7` `1` |
| `skiphit` | `2` `3` `1` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `9` `7` |
| `contrarian` | `6` `5` `1` |
| `dreambook` | `1` `9` `1` |
| `highest-frequency` | `2` `5` `1` |
| `hot` | `5` `0` `6` |
| `llm-fewshot` | `7` `6` `6` |
| `moonphase` | `2` `8` `5` |
| `numerology` | `1` `1` `1` |
| `persistent` | `4` `3` `3` |
| `positional` | `2` `7` `7` |
| `random` | `3` `2` `3` |
| `skiphit` | `2` `5` `1` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `8` `3` `5` |
| `contrarian` | `7` `9` `5` `4` |
| `dreambook` | `2` `1` `5` `2` |
| `highest-frequency` | `5` `8` `3` `4` |
| `hot` | `4` `8` `9` `1` |
| `llm-fewshot` | `5` `9` `2` `4` |
| `moonphase` | `8` `5` `0` `7` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `6` `8` `3` `9` |
| `random` | `5` `3` `1` `8` |
| `skiphit` | `7` `2` `6` `4` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `1` `3` `5` |
| `contrarian` | `2` `2` `0` `4` |
| `dreambook` | `2` `3` `2` `3` |
| `highest-frequency` | `5` `6` `6` `5` |
| `hot` | `8` `4` `9` `1` |
| `llm-fewshot` | `4` `6` `4` `3` |
| `moonphase` | `5` `6` `5` `5` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `8` `7` `1` `2` |
| `random` | `5` `3` `5` `3` |
| `skiphit` | `7` `2` `6` `4` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `11` `22` `26` `33` `36` |
| `balanced` | `03` `05` `18` `27` `28` |
| `benford` | `03` `05` `14` `16` `23` |
| `birthday` | `02` `05` `14` `23` `25` |
| `cold` | `03` `06` `15` `17` `24` |
| `contrarian` | `04` `21` `24` `25` `36` |
| `delta` | `08` `14` `25` `29` `35` |
| `highest-frequency` | `03` `05` `14` `29` `36` |
| `hot` | `04` `11` `12` `19` `32` |
| `llm-fewshot` | `05` `21` `23` `29` `34` |
| `moonphase` | `01` `16` `29` `33` `36` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `01` `06` `07` `14` `26` |
| `skiphit` | `03` `04` `16` `25` `29` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `21` `22` `30` `32` `36` |
| `balanced` | `12` `20` `23` `27` `33` |
| `benford` | `04` `11` `12` `22` `33` |
| `birthday` | `05` `08` `12` `17` `29` |
| `cold` | `06` `08` `09` `13` `27` |
| `contrarian` | `09` `11` `20` `26` `32` |
| `delta` | `02` `12` `19` `28` `30` |
| `highest-frequency` | `08` `12` `26` `30` `32` |
| `hot` | `02` `07` `08` `16` `30` |
| `llm-fewshot` | `04` `13` `17` `24` `26` |
| `moonphase` | `06` `08` `15` `21` `26` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `03` `13` `27` `31` `32` |
| `skiphit` | `06` `24` `30` `32` `35` |

**FL Jackpot Triple Play**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `31` `33` `34` `36` `39` `46` |
| `balanced` | `08` `09` `14` `21` `25` `36` |
| `benford` | `04` `07` `16` `18` `26` `37` |
| `birthday` | `06` `07` `08` `10` `25` `31` |
| `cold` | `14` `16` `17` `19` `20` `25` |
| `contrarian` | `02` `03` `05` `21` `23` `28` |
| `delta` | `03` `18` `24` `25` `34` `44` |
| `highest-frequency` | `04` `07` `10` `18` `25` `29` |
| `hot` | `08` `14` `24` `29` `33` `40` |
| `llm-fewshot` | `08` `09` `25` `34` `38` `42` |
| `moonphase` | `04` `07` `09` `10` `29` `45` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `01` `04` `10` `18` `21` `29` |
| `random` | `04` `07` `12` `29` `30` `42` |
| `skiphit` | `04` `05` `10` `12` `27` `44` |
| `unpopular` | `18` `23` `37` `38` `40` `45` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `6` |
| `contrarian` | `3` `1` |
| `dreambook` | `1` `8` |
| `highest-frequency` | `1` `1` |
| `hot` | `5` `8` |
| `llm-fewshot` | `2` `5` |
| `moonphase` | `3` `0` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `9` `7` |
| `random` | `5` `6` |
| `skiphit` | `6` `2` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `9` |
| `contrarian` | `7` `8` |
| `dreambook` | `2` `0` |
| `highest-frequency` | `1` `6` |
| `hot` | `7` `5` |
| `llm-fewshot` | `8` `9` |
| `moonphase` | `9` `2` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `8` `0` |
| `random` | `1` `6` |
| `skiphit` | `9` `6` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `6` `7` |
| `contrarian` | `4` `4` `2` |
| `dreambook` | `9` `9` `0` |
| `highest-frequency` | `4` `6` `4` |
| `hot` | `4` `9` `6` |
| `llm-fewshot` | `4` `3` `1` |
| `moonphase` | `5` `2` `8` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `7` `6` `4` |
| `random` | `6` `3` `8` |
| `skiphit` | `9` `2` `0` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `5` `7` |
| `contrarian` | `4` `2` `5` |
| `dreambook` | `2` `4` `3` |
| `highest-frequency` | `0` `6` `4` |
| `hot` | `0` `7` `6` |
| `llm-fewshot` | `0` `9` `4` |
| `moonphase` | `8` `8` `5` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `4` `6` `7` |
| `random` | `1` `7` `4` |
| `skiphit` | `1` `3` `5` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `8` `5` `1` |
| `contrarian` | `0` `9` `7` `1` |
| `dreambook` | `2` `5` `9` `3` |
| `highest-frequency` | `1` `1` `9` `5` |
| `hot` | `5` `6` `1` `7` |
| `llm-fewshot` | `5` `4` `4` `5` |
| `moonphase` | `4` `3` `9` `5` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `4` `1` `5` `4` |
| `random` | `1` `3` `6` `6` |
| `skiphit` | `1` `1` `9` `3` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `8` `3` `9` |
| `contrarian` | `1` `0` `8` `4` |
| `dreambook` | `9` `6` `6` `7` |
| `highest-frequency` | `1` `0` `8` `3` |
| `hot` | `4` `1` `8` `9` |
| `llm-fewshot` | `8` `0` `8` `3` |
| `moonphase` | `9` `5` `1` `1` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `1` `5` `6` `8` |
| `random` | `2` `2` `0` `3` |
| `skiphit` | `5` `0` `4` `3` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `8` `5` `4` `2` |
| `contrarian` | `7` `2` `2` `6` `2` |
| `dreambook` | `7` `4` `2` `3` `2` |
| `highest-frequency` | `3` `1` `2` `6` `2` |
| `hot` | `7` `5` `2` `9` `6` |
| `llm-fewshot` | `3` `5` `2` `7` `1` |
| `moonphase` | `3` `7` `8` `2` `4` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `3` `3` `0` `6` `6` |
| `random` | `3` `0` `2` `9` `5` |
| `skiphit` | `1` `3` `2` `8` `0` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `5` `8` `9` `0` `2` |
| `contrarian` | `5` `2` `1` `6` `2` |
| `dreambook` | `5` `6` `8` `7` `3` |
| `highest-frequency` | `5` `3` `1` `7` `4` |
| `hot` | `1` `0` `8` `3` `6` |
| `llm-fewshot` | `5` `7` `6` `7` `1` |
| `moonphase` | `1` `3` `0` `1` `9` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `1` `3` `2` `5` `5` |
| `random` | `8` `6` `9` `7` `2` |
| `skiphit` | `6` `7` `0` `7` `4` |

<sub>Updated 2026-09-25 10:36 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**3222** predictions scored across **62** days. Combined, they've hit **1112** numbers where pure chance predicts **1134.1** (z = **-0.69**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `birthday` | 33 | 17 | 11.9 | 0.52/draw | +1.59 | 3 (Powerball) |
| `random` | 291 | 117 | 102.3 | 0.40/draw | +1.53 | 3 (NY Win 4) |
| `positional` | 246 | 98 | 86.1 | 0.40/draw | +1.35 | 3 (NY Win 4) |
| `contrarian` | 215 | 82 | 75.6 | 0.38/draw | +0.78 | 2 (NY Numbers (Pick 3)) |
| `numerology` | 215 | 81 | 75.6 | 0.38/draw | +0.66 | 3 (NY Numbers (Pick 3)) |
| `persistent` | 215 | 80 | 75.6 | 0.37/draw | +0.54 | 3 (NY Win 4) |
| `benford` | 33 | 13 | 11.9 | 0.39/draw | +0.34 | 3 (Mega Millions) |
| `highest-frequency` | 253 | 89 | 89.0 | 0.35/draw | +0.01 | 2 (Mega Millions) |
| `moonphase` | 215 | 74 | 75.6 | 0.34/draw | -0.19 | 2 (NY Win 4) |
| `llm-tuned` | 90 | 30 | 31.7 | 0.33/draw | -0.32 | 3 (NY Win 4) |
| `skiphit` | 215 | 71 | 75.6 | 0.33/draw | -0.56 | 3 (NY Win 4) |
| `balanced` | 33 | 10 | 11.9 | 0.30/draw | -0.59 | 2 (Mega Millions) |
| `antibalanced` | 33 | 10 | 11.9 | 0.30/draw | -0.59 | 2 (Powerball) |
| `unpopular` | 45 | 14 | 16.2 | 0.31/draw | -0.59 | 2 (Mega Millions) |
| `hot` | 291 | 92 | 102.3 | 0.32/draw | -1.08 | 3 (NY Numbers (Pick 3)) |
| `delta` | 45 | 12 | 16.2 | 0.27/draw | -1.12 | 1 (Powerball) |
| `llm-fewshot` | 281 | 85 | 98.8 | 0.30/draw | -1.47 | 3 (NY Win 4) |
| `cold` | 291 | 87 | 102.3 | 0.30/draw | -1.60 | 3 (NY Win 4) |
| `dreambook` | 182 | 50 | 63.7 | 0.27/draw | -1.81 | 2 (NY Numbers (Pick 3)) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-09-25 10:36 UTC</sub>
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
