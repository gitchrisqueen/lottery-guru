# 🎰 Lottery Guru

An automated, honest lottery-prediction experiment. Every day it:

1. **Pulls real drawing results** (Powerball, Mega Millions, NY Numbers, NY Win 4) from official open-data feeds
2. **Generates predictions** from a portfolio of strategies — statistical folk methods plus an LLM arm
3. **Scores yesterday's predictions** against the actual drawings once results land
4. **Updates a leaderboard** ([REPORT.md](REPORT.md)) comparing every strategy to the exact null hypothesis

Periodically, a local **LLM fine-tuning loop** (MLX on Apple Silicon) trains on the accumulated history to measure whether predictions "improve" over time.

## Today's board

<!-- PREDICTIONS:START -->
### 🎟️ Predictions for 2026-07-27

_These are experiment outputs, not advice. Every arm is expected to score at chance — see the [leaderboard](REPORT.md)._

**Powerball**

| Strategy | Predicted |
|---|---|
| `cold` | `11` `15` `23` `33` `54` + `09` |
| `delta` | `04` `11` `13` `26` `35` + `25` |
| `hot` | `18` `28` `52` `56` `64` + `14` |
| `llm-fewshot` | `04` `09` `30` `54` `60` + `11` |
| `random` | `08` `12` `18` `24` `36` + `18` |
| `unpopular` | `34` `40` `54` `57` `64` + `14` |

**NY Numbers (Pick 3) — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `0` `2` |
| `hot` | `3` `8` `4` |
| `llm-fewshot` | `8` `0` `3` |
| `positional` | `4` `0` `3` |
| `random` | `0` `5` `1` |

**NY Numbers (Pick 3) — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `0` `2` |
| `hot` | `3` `8` `4` |
| `llm-fewshot` | `4` `7` `1` |
| `positional` | `8` `4` `3` |
| `random` | `7` `7` `5` |

**NY Win 4 — evening**

| Strategy | Predicted |
|---|---|
| `cold` | `7` `1` `2` `5` |
| `hot` | `6` `5` `2` `1` |
| `llm-fewshot` | `4` `5` `5` `1` |
| `positional` | `2` `0` `0` `0` |
| `random` | `0` `2` `6` `2` |

**NY Win 4 — midday**

| Strategy | Predicted |
|---|---|
| `cold` | `1` `7` `0` `5` |
| `hot` | `6` `5` `2` `1` |
| `llm-fewshot` | `7` `3` `5` `9` |
| `positional` | `4` `2` `2` `2` |
| `random` | `2` `5` `8` `1` |

<sub>Updated 2026-07-27 11:24 UTC</sub>
<!-- PREDICTIONS:END -->

Full board: [PREDICTIONS.md](PREDICTIONS.md) · Leaderboard: [REPORT.md](REPORT.md)

## Track record

<!-- SCOREBOARD:START -->
### 📊 How it's performing

**62** predictions scored across **3** days. Combined, they've hit **19** numbers where pure chance predicts **21.8** (z = **-0.63**).

| Strategy | Scored | Hits | Chance predicts | Hit rate | vs chance (z) | Best single |
|---|---|---|---|---|---|---|
| `positional` | 12 | 6 | 4.2 | 0.50/draw | +0.93 | 1 (NY Numbers (Pick 3)) |
| `hot` | 14 | 6 | 4.9 | 0.43/draw | +0.51 | 2 (NY Numbers (Pick 3)) |
| `random` | 14 | 4 | 4.9 | 0.29/draw | -0.44 | 1 (NY Numbers (Pick 3)) |
| `delta` | 2 | 0 | 0.7 | 0.00/draw | -0.91 | 0 |
| `unpopular` | 2 | 0 | 0.7 | 0.00/draw | -0.91 | 0 |
| `cold` | 14 | 3 | 4.9 | 0.21/draw | -0.91 | 1 (Mega Millions) |
| `llm-fewshot` | 4 | 0 | 1.4 | 0.00/draw | -1.25 | 0 |

_**Reading this:** `z` measures how far a strategy sits from pure chance in standard deviations. Values bouncing around 0 mean it is performing exactly as randomness predicts — which is the expected result. It would take a sustained |z| > 3 over many draws to suggest anything real, and no strategy is expected to get there._

<sub>Updated 2026-07-27 11:24 UTC</sub>
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
| `llm-tuned` | local MLX model, LoRA-tuned on accumulated history | chance (measured rigorously) |

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
cadence: monthly, once ≥60 scored days exist. A hosted alternative
(Fireworks.ai serverless LoRA, <$1/run) is documented in
[docs/RESEARCH.md](docs/RESEARCH.md).

## Data sources

- **NY Open Data (Socrata)** — official, free, no auth; nightly refresh.
  Powerball `d6yy-54nr`, Mega Millions `5xaw-6ayf`, Numbers/Win4 `hsys-3def`.
- **Texas Lottery CSVs** — used as an integrity cross-check for Powerball.

## Disclaimer

This is a statistics/ML measurement project, not gambling advice. Expected
value of every lottery ticket is strongly negative; nothing here changes that.
