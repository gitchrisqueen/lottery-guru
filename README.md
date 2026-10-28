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
### 🎟️ Predictions for 2026-10-28

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Powerball**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `05` `06` `22` `27` + `06` |
| `balanced` | `14` `27` `38` `42` `45` + `20` |
| `benford` | `05` `13` `14` `23` `33` + `04` |
| `birthday` | `01` `09` `19` `26` `28` + `03` |
| `cold` | `27` `43` `60` `63` `66` + `21` |
| `contrarian` | `04` `21` `26` `44` `57` + `01` |
| `delta` | `08` `14` `37` `39` `40` + `01` |
| `highest-frequency` | `14` `19` `21` `23` `40` + `01` |
| `hot` | `03` `14` `21` `42` `64` + `03` |
| `llm-fewshot` | `46` `57` `58` `61` `68` + `22` |
| `moonphase` | `12` `19` `21` `23` `65` + `21` |
| `numerology` | `10` `12` `20` `24` `36` + `11` |
| `persistent` | `13` `21` `23` `32` `66` + `01` |
| `random` | `19` `37` `40` `46` `56` + `23` |
| `skiphit` | `15` `18` `26` `29` `50` + `01` |
| `unpopular` | `32` `40` `50` `51` `64` + `20` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `7` `8` |
| `contrarian` | `9` `1` `1` |
| `dreambook` | `7` `2` `3` |
| `highest-frequency` | `7` `1` `3` |
| `hot` | `5` `9` `6` |
| `llm-fewshot` | `3` `7` `9` |
| `moonphase` | `0` `4` `4` |
| `numerology` | `1` `1` `5` |
| `persistent` | `4` `3` `3` |
| `positional` | `6` `5` `0` |
| `random` | `7` `4` `3` |
| `skiphit` | `9` `6` `1` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `7` `8` |
| `contrarian` | `9` `1` `0` |
| `dreambook` | `0` `4` `2` |
| `highest-frequency` | `4` `1` `1` |
| `hot` | `5` `9` `6` |
| `llm-fewshot` | `6` `5` `9` |
| `moonphase` | `8` `5` `7` |
| `numerology` | `1` `1` `5` |
| `persistent` | `4` `3` `3` |
| `positional` | `5` `3` `1` |
| `random` | `7` `8` `1` |
| `skiphit` | `9` `1` `1` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `9` `0` `3` |
| `contrarian` | `3` `6` `7` `5` |
| `dreambook` | `8` `4` `1` `0` |
| `highest-frequency` | `0` `4` `1` `5` |
| `hot` | `6` `4` `8` `7` |
| `llm-fewshot` | `0` `7` `0` `8` |
| `moonphase` | `6` `4` `4` `8` |
| `numerology` | `1` `1` `5` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `0` `2` `1` `1` |
| `random` | `2` `7` `4` `7` |
| `skiphit` | `0` `6` `1` `5` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `9` `0` `7` |
| `contrarian` | `3` `6` `7` `4` |
| `dreambook` | `4` `0` `9` `3` |
| `highest-frequency` | `4` `6` `9` `7` |
| `hot` | `4` `6` `8` `9` |
| `llm-fewshot` | `4` `3` `9` `9` |
| `moonphase` | `0` `6` `0` `7` |
| `numerology` | `1` `1` `5` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `4` `2` `9` `3` |
| `random` | `3` `6` `8` `7` |
| `skiphit` | `5` `6` `1` `4` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `04` `06` `07` `09` `30` |
| `balanced` | `03` `04` `22` `29` `33` |
| `benford` | `04` `10` `18` `23` `33` |
| `birthday` | `01` `05` `10` `29` `30` |
| `cold` | `03` `05` `20` `21` `22` |
| `contrarian` | `07` `25` `28` `33` `36` |
| `delta` | `02` `03` `06` `16` `22` |
| `highest-frequency` | `07` `10` `12` `29` `33` |
| `hot` | `01` `08` `30` `33` `35` |
| `llm-fewshot` | `11` `12` `15` `16` `21` |
| `moonphase` | `03` `04` `07` `10` `12` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `07` `12` `23` `29` `36` |
| `skiphit` | `02` `14` `20` `29` `36` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `07` `13` `15` `31` `35` |
| `balanced` | `04` `07` `14` `25` `29` |
| `benford` | `04` `12` `18` `24` `34` |
| `birthday` | `04` `05` `08` `10` `18` |
| `cold` | `14` `22` `29` `33` `36` |
| `contrarian` | `08` `09` `25` `29` `32` |
| `delta` | `08` `17` `29` `30` `36` |
| `highest-frequency` | `08` `14` `22` `29` `36` |
| `hot` | `01` `08` `26` `30` `36` |
| `llm-fewshot` | `02` `16` `26` `28` `32` |
| `moonphase` | `02` `16` `19` `21` `22` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `06` `13` `18` `21` `27` |
| `skiphit` | `11` `14` `28` `31` `36` |

**Florida Lotto**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `25` `31` `38` `39` `45` `53` |
| `balanced` | `06` `12` `16` `33` `41` `49` |
| `benford` | `04` `13` `15` `26` `38` `52` |
| `birthday` | `02` `07` `10` `11` `21` `23` |
| `cold` | `02` `12` `17` `23` `41` `53` |
| `contrarian` | `08` `16` `18` `25` `49` `53` |
| `delta` | `13` `21` `27` `39` `47` `53` |
| `highest-frequency` | `23` `26` `40` `45` `50` `53` |
| `hot` | `06` `08` `33` `34` `42` `53` |
| `llm-fewshot` | `03` `05` `28` `40` `45` `51` |
| `moonphase` | `01` `13` `26` `29` `40` `42` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `05` `10` `32` `33` `38` `50` |
| `random` | `06` `23` `26` `32` `40` `45` |
| `skiphit` | `03` `08` `20` `31` `45` `50` |
| `unpopular` | `19` `40` `45` `46` `50` `51` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `0` |
| `contrarian` | `2` `0` |
| `dreambook` | `4` `9` |
| `highest-frequency` | `4` `1` |
| `hot` | `1` `4` |
| `llm-fewshot` | `7` `8` |
| `moonphase` | `6` `8` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `4` `5` |
| `random` | `0` `1` |
| `skiphit` | `9` `1` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `9` |
| `contrarian` | `3` `2` |
| `dreambook` | `3` `1` |
| `highest-frequency` | `1` `1` |
| `hot` | `6` `8` |
| `llm-fewshot` | `1` `3` |
| `moonphase` | `1` `7` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `6` `6` |
| `random` | `9` `6` |
| `skiphit` | `5` `3` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `9` `0` |
| `contrarian` | `4` `4` `5` |
| `dreambook` | `4` `7` `3` |
| `highest-frequency` | `4` `6` `0` |
| `hot` | `8` `4` `0` |
| `llm-fewshot` | `2` `6` `0` |
| `moonphase` | `5` `5` `0` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `3` `5` `4` |
| `random` | `4` `9` `1` |
| `skiphit` | `7` `6` `3` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `3` `1` `4` |
| `contrarian` | `2` `7` `5` |
| `dreambook` | `8` `4` `1` |
| `highest-frequency` | `5` `1` `1` |
| `hot` | `9` `1` `7` |
| `llm-fewshot` | `5` `9` `2` |
| `moonphase` | `9` `6` `3` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `5` `5` `0` |
| `random` | `5` `0` `0` |
| `skiphit` | `3` `0` `7` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `4` `0` `7` |
| `contrarian` | `3` `6` `2` `4` |
| `dreambook` | `7` `3` `0` `9` |
| `highest-frequency` | `1` `4` `0` `5` |
| `hot` | `1` `8` `5` `4` |
| `llm-fewshot` | `1` `8` `6` `6` |
| `moonphase` | `7` `4` `3` `3` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `7` `0` `8` `5` |
| `random` | `4` `5` `0` `7` |
| `skiphit` | `0` `0` `1` `3` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `7` `6` `0` |
| `contrarian` | `2` `0` `4` `7` |
| `dreambook` | `1` `6` `2` `8` |
| `highest-frequency` | `1` `4` `2` `8` |
| `hot` | `7` `4` `0` `8` |
| `llm-fewshot` | `3` `4` `2` `3` |
| `moonphase` | `9` `3` `2` `4` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `7` `2` `2` `8` |
| `random` | `5` `7` `3` `2` |
| `skiphit` | `8` `4` `0` `0` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `4` `3` `7` `8` |
| `contrarian` | `7` `5` `0` `0` `6` |
| `dreambook` | `9` `8` `0` `0` `3` |
| `highest-frequency` | `5` `1` `1` `8` `4` |
| `hot` | `7` `4` `1` `3` `0` |
| `llm-fewshot` | `5` `1` `7` `8` `1` |
| `moonphase` | `5` `6` `1` `8` `0` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `9` `2` `5` `2` `3` |
| `random` | `7` `9` `2` `9` `1` |
| `skiphit` | `5` `9` `8` `8` `2` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `4` `8` `7` `0` |
| `contrarian` | `8` `2` `0` `7` `4` |
| `dreambook` | `2` `0` `5` `3` `3` |
| `highest-frequency` | `2` `1` `6` `4` `4` |
| `hot` | `2` `0` `1` `6` `8` |
| `llm-fewshot` | `0` `5` `6` `6` `2` |
| `moonphase` | `5` `2` `0` `8` `2` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `3` `4` `4` `8` `2` |
| `random` | `2` `1` `9` `4` `3` |
| `skiphit` | `5` `5` `3` `9` `3` |

<sub>Updated 2026-10-28 10:30 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**5213** predictions scored across **95** days. Combined, they've hit **1814** numbers where pure chance predicts **1834.9** (z = **-0.52**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `benford` | 57 | 28 | 20.5 | 0.49/draw | +1.76 | 3 (Mega Millions) |
| `random` | 449 | 176 | 157.9 | 0.39/draw | +1.53 | 3 (NY Win 4) |
| `birthday` | 57 | 26 | 20.5 | 0.46/draw | +1.29 | 3 (Powerball) |
| `positional` | 380 | 142 | 133.0 | 0.37/draw | +0.82 | 3 (NY Win 4) |
| `balanced` | 57 | 24 | 20.5 | 0.42/draw | +0.82 | 2 (Mega Millions) |
| `persistent` | 373 | 139 | 131.1 | 0.37/draw | +0.73 | 3 (NY Win 4) |
| `highest-frequency` | 411 | 150 | 144.5 | 0.36/draw | +0.48 | 3 (NY Win 4) |
| `numerology` | 373 | 132 | 131.1 | 0.35/draw | +0.08 | 3 (NY Numbers (Pick 3)) |
| `cold` | 449 | 158 | 157.9 | 0.35/draw | +0.01 | 3 (NY Win 4) |
| `antibalanced` | 57 | 20 | 20.5 | 0.35/draw | -0.13 | 2 (Powerball) |
| `skiphit` | 373 | 128 | 131.1 | 0.34/draw | -0.29 | 3 (NY Win 4) |
| `llm-tuned` | 90 | 30 | 31.7 | 0.33/draw | -0.32 | 3 (NY Win 4) |
| `contrarian` | 373 | 127 | 131.1 | 0.34/draw | -0.38 | 3 (NY Win 4) |
| `llm-fewshot` | 438 | 145 | 154.0 | 0.33/draw | -0.77 | 3 (NY Win 4) |
| `moonphase` | 373 | 121 | 131.1 | 0.32/draw | -0.93 | 3 (NY Numbers (Pick 3)) |
| `unpopular` | 69 | 20 | 24.9 | 0.29/draw | -1.04 | 2 (Mega Millions) |
| `dreambook` | 316 | 98 | 110.6 | 0.31/draw | -1.26 | 2 (NY Numbers (Pick 3)) |
| `delta` | 69 | 18 | 24.9 | 0.26/draw | -1.47 | 1 (Powerball) |
| `hot` | 449 | 132 | 157.9 | 0.29/draw | -2.17 | 3 (NY Numbers (Pick 3)) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-10-28 10:30 UTC</sub>
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
