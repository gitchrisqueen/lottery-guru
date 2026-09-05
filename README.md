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
### 🎟️ Predictions for 2026-09-05

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Powerball**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `34` `46` `57` `63` `64` + `16` |
| `balanced` | `09` `11` `28` `56` `60` + `01` |
| `benford` | `01` `21` `34` `47` `50` + `10` |
| `birthday` | `03` `06` `19` `28` `30` + `08` |
| `cold` | `01` `23` `34` `51` `52` + `19` |
| `contrarian` | `10` `17` `25` `37` `67` + `14` |
| `delta` | `05` `17` `35` `40` `42` + `25` |
| `highest-frequency` | `10` `17` `34` `35` `63` + `14` |
| `hot` | `03` `06` `58` `63` `64` + `02` |
| `llm-fewshot` | `05` `06` `13` `50` `53` + `13` |
| `moonphase` | `14` `17` `26` `34` `36` + `14` |
| `numerology` | `10` `12` `20` `23` `24` + `22` |
| `persistent` | `13` `21` `23` `32` `66` + `01` |
| `random` | `35` `37` `47` `48` `51` + `07` |
| `skiphit` | `10` `29` `31` `58` `68` + `14` |
| `unpopular` | `34` `35` `40` `46` `63` + `05` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `5` `7` |
| `contrarian` | `8` `3` `0` |
| `dreambook` | `3` `1` `6` |
| `highest-frequency` | `8` `3` `2` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `5` `5` `0` |
| `moonphase` | `5` `6` `5` |
| `numerology` | `1` `1` `8` |
| `persistent` | `4` `3` `3` |
| `positional` | `2` `8` `2` |
| `random` | `4` `9` `8` |
| `skiphit` | `8` `3` `6` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `5` `7` |
| `contrarian` | `8` `3` `6` |
| `dreambook` | `2` `0` `5` |
| `highest-frequency` | `4` `5` `4` |
| `hot` | `8` `5` `2` |
| `llm-fewshot` | `9` `5` `1` |
| `moonphase` | `4` `8` `4` |
| `numerology` | `1` `1` `8` |
| `persistent` | `4` `3` `3` |
| `positional` | `6` `4` `7` |
| `random` | `4` `7` `4` |
| `skiphit` | `8` `8` `6` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `3` `8` `2` |
| `contrarian` | `5` `7` `6` `2` |
| `dreambook` | `7` `5` `2` `8` |
| `highest-frequency` | `5` `7` `6` `2` |
| `hot` | `9` `8` `3` `2` |
| `llm-fewshot` | `3` `8` `1` `0` |
| `moonphase` | `1` `1` `7` `6` |
| `numerology` | `1` `1` `8` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `7` `0` `3` `4` |
| `random` | `2` `9` `6` `5` |
| `skiphit` | `5` `7` `0` `8` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `9` `8` `3` `2` |
| `contrarian` | `4` `7` `6` `2` |
| `dreambook` | `9` `6` `9` `7` |
| `highest-frequency` | `9` `8` `3` `2` |
| `hot` | `9` `8` `3` `2` |
| `llm-fewshot` | `3` `2` `9` `1` |
| `moonphase` | `6` `8` `3` `5` |
| `numerology` | `1` `1` `8` `5` |
| `persistent` | `5` `9` `6` `5` |
| `positional` | `9` `3` `3` `1` |
| `random` | `7` `5` `1` `9` |
| `skiphit` | `5` `7` `0` `8` |

**FL Fantasy 5 — evening**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `03` `07` `09` `26` |
| `balanced` | `08` `09` `14` `34` `35` |
| `benford` | `03` `05` `11` `13` `24` |
| `birthday` | `01` `03` `12` `16` `24` |
| `cold` | `09` `16` `17` `21` `28` |
| `contrarian` | `01` `18` `25` `30` `31` |
| `delta` | `06` `12` `17` `20` `34` |
| `highest-frequency` | `06` `11` `12` `26` `34` |
| `hot` | `06` `07` `11` `14` `36` |
| `llm-fewshot` | `04` `08` `11` `26` `34` |
| `moonphase` | `15` `26` `30` `32` `33` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `06` `15` `21` `26` `29` |
| `skiphit` | `07` `21` `25` `34` `35` |

**FL Fantasy 5 — midday**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `06` `13` `16` `17` |
| `balanced` | `06` `11` `14` `19` `25` |
| `benford` | `04` `14` `17` `24` `31` |
| `birthday` | `03` `08` `12` `25` `27` |
| `cold` | `14` `29` `30` `34` `35` |
| `contrarian` | `06` `11` `23` `31` `36` |
| `delta` | `06` `09` `22` `25` `33` |
| `highest-frequency` | `06` `14` `22` `25` `36` |
| `hot` | `02` `19` `21` `22` `36` |
| `llm-fewshot` | `07` `20` `27` `28` `35` |
| `moonphase` | `10` `16` `22` `26` `28` |
| `numerology` | `10` `12` `20` `24` `36` |
| `persistent` | `05` `14` `22` `26` `29` |
| `random` | `05` `18` `25` `26` `34` |
| `skiphit` | `06` `12` `15` `19` `34` |

**Florida Lotto**

| Strategy | Predicted |
|---|---|
| `antibalanced` | `01` `03` `29` `35` `39` `45` |
| `balanced` | `02` `12` `29` `32` `33` `39` |
| `benford` | `05` `11` `18` `20` `39` `43` |
| `birthday` | `01` `07` `10` `13` `18` `31` |
| `cold` | `01` `09` `17` `32` `43` `50` |
| `contrarian` | `05` `22` `30` `40` `48` `50` |
| `delta` | `07` `15` `16` `28` `38` `45` |
| `highest-frequency` | `01` `10` `18` `32` `45` `48` |
| `hot` | `14` `23` `29` `35` `36` `43` |
| `llm-fewshot` | `01` `04` `09` `26` `40` `48` |
| `moonphase` | `22` `24` `41` `42` `46` `48` |
| `numerology` | `10` `12` `20` `24` `30` `36` |
| `persistent` | `05` `10` `32` `33` `38` `50` |
| `random` | `09` `17` `18` `34` `40` `42` |
| `skiphit` | `10` `18` `19` `26` `32` `41` |
| `unpopular` | `11` `34` `41` `45` `48` `53` |

**FL Pick 2 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `0` `3` |
| `contrarian` | `6` `6` |
| `dreambook` | `0` `6` |
| `highest-frequency` | `0` `1` |
| `hot` | `4` `1` |
| `llm-fewshot` | `4` `8` |
| `moonphase` | `2` `4` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `0` `2` |
| `random` | `6` `1` |
| `skiphit` | `5` `3` |

**FL Pick 2 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `6` |
| `contrarian` | `4` `1` |
| `dreambook` | `3` `6` |
| `highest-frequency` | `1` `9` |
| `hot` | `8` `9` |
| `llm-fewshot` | `0` `7` |
| `moonphase` | `5` `4` |
| `numerology` | `1` `1` |
| `persistent` | `8` `1` |
| `positional` | `7` `9` |
| `random` | `1` `9` |
| `skiphit` | `3` `0` |

**FL Pick 3 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `4` `0` `5` |
| `contrarian` | `9` `3` `9` |
| `dreambook` | `0` `2` `4` |
| `highest-frequency` | `9` `2` `5` |
| `hot` | `7` `9` `5` |
| `llm-fewshot` | `4` `6` `0` |
| `moonphase` | `9` `2` `0` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `9` `9` `6` |
| `random` | `3` `8` `5` |
| `skiphit` | `3` `2` `6` |

**FL Pick 3 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `8` `7` `6` |
| `contrarian` | `4` `9` `6` |
| `dreambook` | `1` `8` `3` |
| `highest-frequency` | `8` `1` `3` |
| `hot` | `7` `6` `8` |
| `llm-fewshot` | `8` `4` `5` |
| `moonphase` | `6` `1` `0` |
| `numerology` | `1` `1` `1` |
| `persistent` | `8` `6` `4` |
| `positional` | `2` `1` `4` |
| `random` | `8` `7` `3` |
| `skiphit` | `1` `8` `9` |

**FL Pick 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `6` `1` `2` `5` |
| `contrarian` | `2` `9` `8` `8` |
| `dreambook` | `5` `2` `3` `5` |
| `highest-frequency` | `2` `1` `3` `5` |
| `hot` | `9` `1` `5` `0` |
| `llm-fewshot` | `3` `4` `4` `5` |
| `moonphase` | `6` `3` `5` `9` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `2` `3` `3` `2` |
| `random` | `2` `3` `3` `0` |
| `skiphit` | `7` `2` `8` `9` |

**FL Pick 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `2` `6` `4` |
| `contrarian` | `2` `2` `2` `6` |
| `dreambook` | `0` `0` `1` `2` |
| `highest-frequency` | `2` `2` `1` `5` |
| `hot` | `1` `3` `2` `7` |
| `llm-fewshot` | `4` `2` `5` `6` |
| `moonphase` | `8` `6` `8` `4` |
| `numerology` | `1` `1` `1` `5` |
| `persistent` | `2` `4` `6` `5` |
| `positional` | `7` `7` `8` `7` |
| `random` | `5` `7` `2` `0` |
| `skiphit` | `3` `3` `1` `8` |

**FL Pick 5 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `2` `5` `6` `4` `1` |
| `contrarian` | `5` `6` `6` `5` `7` |
| `dreambook` | `9` `8` `0` `0` `3` |
| `highest-frequency` | `1` `1` `4` `4` `7` |
| `hot` | `0` `5` `7` `3` `6` |
| `llm-fewshot` | `7` `1` `5` `3` `6` |
| `moonphase` | `4` `0` `4` `4` `7` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `1` `3` `9` `2` `7` |
| `random` | `6` `4` `4` `9` `2` |
| `skiphit` | `1` `7` `4` `4` `4` |

**FL Pick 5 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `0` `6` `1` `3` |
| `contrarian` | `4` `7` `3` `3` `8` |
| `dreambook` | `9` `4` `0` `1` `0` |
| `highest-frequency` | `7` `7` `3` `4` `4` |
| `hot` | `7` `3` `8` `4` `6` |
| `llm-fewshot` | `0` `5` `3` `4` `1` |
| `moonphase` | `4` `7` `7` `2` `3` |
| `numerology` | `1` `1` `1` `5` `4` |
| `persistent` | `5` `1` `6` `4` `4` |
| `positional` | `7` `8` `4` `7` `7` |
| `random` | `8` `7` `9` `2` `5` |
| `skiphit` | `2` `0` `8` `6` `4` |

<sub>Updated 2026-09-05 13:37 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**1867** predictions scored across **42** days. Combined, they've hit **687** numbers where pure chance predicts **659.5** (z = **+1.13**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `contrarian` | 111 | 55 | 39.1 | 0.50/draw | +2.68 | 2 (NY Numbers (Pick 3)) |
| `highest-frequency` | 144 | 61 | 50.8 | 0.42/draw | +1.51 | 2 (Mega Millions) |
| `random` | 180 | 74 | 63.6 | 0.41/draw | +1.38 | 2 (Mega Millions) |
| `skiphit` | 111 | 47 | 39.1 | 0.42/draw | +1.33 | 3 (NY Win 4) |
| `numerology` | 111 | 45 | 39.1 | 0.41/draw | +0.99 | 3 (NY Numbers (Pick 3)) |
| `positional` | 149 | 59 | 52.4 | 0.40/draw | +0.96 | 2 (NY Win 4) |
| `birthday` | 19 | 9 | 6.8 | 0.47/draw | +0.88 | 2 (Powerball) |
| `benford` | 19 | 9 | 6.8 | 0.47/draw | +0.88 | 3 (Mega Millions) |
| `persistent` | 111 | 43 | 39.1 | 0.39/draw | +0.65 | 2 (NY Numbers (Pick 3)) |
| `hot` | 180 | 67 | 63.6 | 0.37/draw | +0.46 | 3 (NY Numbers (Pick 3)) |
| `llm-tuned` | 79 | 27 | 27.9 | 0.34/draw | -0.18 | 3 (NY Win 4) |
| `balanced` | 19 | 6 | 6.8 | 0.32/draw | -0.34 | 2 (Mega Millions) |
| `antibalanced` | 19 | 6 | 6.8 | 0.32/draw | -0.34 | 1 (Powerball) |
| `unpopular` | 31 | 9 | 11.2 | 0.29/draw | -0.69 | 2 (Mega Millions) |
| `moonphase` | 111 | 35 | 39.1 | 0.32/draw | -0.70 | 2 (NY Win 4) |
| `delta` | 31 | 8 | 11.2 | 0.26/draw | -1.01 | 1 (Powerball) |
| `llm-fewshot` | 170 | 51 | 60.0 | 0.30/draw | -1.23 | 3 (NY Win 4) |
| `cold` | 180 | 54 | 63.6 | 0.30/draw | -1.27 | 3 (NY Win 4) |
| `dreambook` | 92 | 22 | 32.3 | 0.24/draw | -1.91 | 2 (NY Numbers (Pick 3)) |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-09-05 13:37 UTC</sub>
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
