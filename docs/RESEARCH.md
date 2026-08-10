# Research Findings

Condensed from three research passes (data sources, prediction strategies, LLM fine-tuning), 2026-07-25.

## 1. Data sources (verified live)

### Primary: NY Open Data (Socrata, data.ny.gov)

Free, no auth required (optional free app token removes throttling). JSON via SoQL
(`/resource/{id}.json?$order=draw_date DESC&$limit=N`) or bulk CSV
(`/api/views/{id}/rows.csv?accessType=DOWNLOAD`). All datasets refresh in a nightly batch
**~07:30–09:00 UTC (~3:30–5:00 AM ET)** — results appear the morning after the draw.

| Game | Dataset ID | Fields | History |
|---|---|---|---|
| Powerball | `d6yy-54nr` | `draw_date`, `winning_numbers` ("n1..n5 PB" — 6th token is the Powerball), `multiplier` | 2010→ |
| Mega Millions | `5xaw-6ayf` | `draw_date`, `winning_numbers` (5 white), `mega_ball` (separate field) | 2002→ |
| NY Numbers (Pick 3) + Win 4 | `hsys-3def` | one row/date: `midday_daily`, `evening_daily`, `midday_win_4`, `evening_win_4` | 1980→ |
| Take 5 | `dg63-4siq` | `midday_winning_numbers`, `evening_winning_numbers` (5 of 39, daily ×2) | 1992→ |

Avoid: Cash4Life `kwxv-fwze` — game retired Feb 2026, dataset frozen.

### Secondary / intraday: Texas Lottery static CSVs

Official, no auth, full history per file, **updates intra-day** (same-day draws verified).
Base `https://www.texaslottery.com/export/sites/lottery/Games/`:
`Powerball/Winning_Numbers/powerball.csv`, `Mega_Millions/Winning_Numbers/megamillions.csv`,
`Pick_3/Winning_Numbers/pick3{morning,day,evening,night}.csv`,
`Daily_4/Winning_Numbers/daily4{morning,day,evening,night}.csv`.
Row format ex: `Powerball,7,22,2026,50,58,5,4,22,1,3` (game, M, D, Y, 5 white *unordered*, PB, multiplier).
Useful as cross-check and same-night daily-game source. Note: `pick3.csv`/`daily4.csv` (no drawtime) are 404.

### Florida Lottery PDF files (FL-only games; verified live 2026-08-09)

Florida has **no open-data portal** (nothing Socrata-like; the state's portals
are GIS-only). The official machine source is a set of **daily-regenerated PDF
history files**, full history per file, newest-first:
`https://files.floridalottery.com/exptkt/{stem}.pdf`, byte-identical mirror at
`https://apps.flalottery.com/exptkt/{stem}.pdf` (fetcher fails over automatically).

| Stem | Game | Layout notes |
|---|---|---|
| `ff` | Fantasy 5 (5/36, midday+evening) | one record/line: `8/8/26 EVENING 2 10 15 16 32`; history to 1995 (5/26 era) |
| `l6` | Florida Lotto (6/53, Wed/Sat) | **two records per text line** (2-column pages); `LOTTO` vs `LOTTO DP` label column (Double Play dropped); pre-2021 rows unlabeled; history to 1988 (6/49 era) |
| `jtp` | Jackpot Triple Play (6/46, Tue/Fri) | two records/line, no labels |
| `p2`–`p5` | Pick 2–5 (digits, midday+evening) | **three records per text line**; `E`/`M` markers; `FB n` Fireball column (post-2019 only, dropped) |
| `c3` | pre-Aug-2016 Cash 3 | frozen at the 2016 rename; optional deep-backfill stitch for Pick 3 (not wired) |

Parsing (see `data/florida.py`): date-anchored regex findall per line — handles
the multi-column layouts and skips page headers/disclaimers without a filter
list. These files are **long** (Fantasy 5 is 386 pages, the Pick files ~130) and
layout-aware extraction costs seconds per page, so pages are read lazily and
abandoned once the requested draw count is met — the daily 200-draw pull touches
a handful of pages, not the whole file. Fixtures under `tests/fixtures/fl/` were
captured from the live files by a one-shot spike workflow (removed after it
served its purpose; recoverable from git history at tag-time commit `91a18a0`). Dates are `M/D/YY`; century rule `yy >= 88 → 19yy`. The files' header date
is a **generation timestamp, not a last-draw date** (retired games' files still
regenerate) — detect new data by diffing rows, never by header. No auth, no
captcha, stable URL scheme for a decade+; fetches send a descriptive UA and the
per-game pull soft-fails so a WAF hiccup never blocks the loop. FL evening
draws (11:15 PM ET = 03:15 UTC) are in the nightly regeneration well before the
10:15 UTC pull; a lagging day self-heals via `score_pending()`.

### Third-party APIs (APIVerve, magayo, lotteryresultsapi, collectapi)

All add auth/quotas/lag and none beat the free government feeds. Fallback only.
For FL-only games magayo documents explicit FL support and is the best
structured fallback if the PDFs ever move.

### Draw schedule (ET)

- Powerball: Mon/Wed/Sat 10:59 PM — 5 of 69 white + 1 of 26
- Mega Millions: Tue/Fri 11:00 PM — 5 of 70 white + 1 of 24 (since Apr 2025; **never pool stats across rule eras**)
- NY Numbers/Win 4: daily, midday 2:30 PM + evening 10:30 PM
- Take 5: daily, midday + evening
- FL Fantasy 5: daily, midday 1:05 PM (since 2023-03-20) + evening 11:15 PM
- Florida Lotto: Wed/Sat 11:15 PM (6/53 since Oct 1999; Double Play sub-draw not tracked)
- FL Jackpot Triple Play: Tue/Fri 11:15 PM (launched Feb 2019)
- FL Pick 2–5: daily, midday 1:30 PM + evening 9:45 PM (Pick 2/5 launched Aug 2016; Fireball add-on not tracked)

Recommended pull time: **~10:00 UTC daily** (after the NY nightly batch completes).

## 2. Prediction strategies

Every draw is independent; well-run lotteries consistently pass uniformity tests (chi-square,
gap, runs — see arxiv 0806.4595). No peer-reviewed work demonstrates above-chance draw
prediction; blog LSTM attempts perform at chance (claims otherwise use in-sample leakage).
The strategies below are implemented as *hypotheses to falsify* — plus one with real EV logic.

| Strategy | Idea | Expected result |
|---|---|---|
| `random` | uniform sample — the null baseline | defines chance |
| `hot` | most frequent numbers in trailing window | chance |
| `cold` | longest-absent ("overdue") numbers — gambler's fallacy control | chance |
| `delta` | sample empirical gaps between sorted winners, cumsum | chance (delta clustering is an artifact of order statistics) |
| `positional` | per-position digit frequency for Pick 3/Win 4 | chance |
| `unpopular` | avoid human-popular combos (birthdays ≤31, sequences, grid patterns) to reduce jackpot splitting | same match rate, but **higher EV conditional on winning** (Israeli lottery study of ~800M picks; UK unpopular-number analysis) — the one defensible strategy |
| `llm` | few-shot base model & periodically fine-tuned local model | chance (measured rigorously) |
| `contrarian` | play recently drawn numbers (public under-bets them for months — Clotfelter & Cook 1993) | chance on matches; lower modeled split exposure |
| `birthday` | deliberately popular date-range picks — the mirror of `unpopular` | chance on matches; worst split exposure |
| `balanced` / `antibalanced` | folk mid-sum/3:2-parity filter, and its inversion | chance — the bands just contain more combinations |
| `skiphit` | Gail Howard skip charts + last-draw repeats | chance — fair-draw skips are memoryless |
| `benford` | Benford leading-digit weighting — **known-wrong control** (bounded uniform ranges are the textbook counterexample) | chance |
| `persistent` | Lustig same-ticket-forever (seeded per game only — documented exception) | chance; the cleanest null demo |
| `moonphase` | lunar phase folded into the seed — a seeded RNG in a costume, on purpose | chance |
| `numerology` | Pythagorean persona numbers + personal day | chance |
| `dreambook` | policy-tradition dream symbols → fixed digits (digit games only) | chance |

Full catalog with automation classification and the human-required exploits
(WinFall roll-down, Mandel buyouts, scratch tracking, syndicates):
[UNORTHODOX.md](UNORTHODOX.md). Their automatable halves run as the
"Exploit watch" monitors (`evaluation/monitors.py`) in REPORT.md.

Documented "wins" all exploited payout structure or fraud, never draw prediction:
Selbee/MIT (Cash WinFall roll-down EV), Mandel (buy all combos when jackpot > cost),
Ontario retailer fraud (forensic stats on claims), Tipton (rigged RNG rootkit).
Abrams & Garibaldi (Am. Math. Monthly 2010): rollovers can make EV positive but variance
means you still shouldn't play.

## 3. Null-hypothesis baselines (what "no skill" scores)

**Powerball (5/69 + 1/26), one ticket vs one draw:**
- White matches ~ Hypergeometric(N=69, K=5, n=5): **E = 25/69 ≈ 0.3623**, var ≈ 0.3242
- PMF: P(0)=.67840, P(1)=.28267, P(2)=.037073, P(3)=.0017939, P(4)=2.85e-5, P(5)=8.9e-8
- P(red) = 1/26 ≈ 0.03846
- Over D predictions: z = (observed − 0.3623·D) / √(0.3242·D)

**Mega Millions (5/70 + 1/24):** E[white] = 25/70 ≈ 0.3571; P(mega) = 1/24.

**Pick 3 (3 ordered digits 0–9):** per-position P = 1/10; matches ~ Binomial(3, 0.1),
E = 0.3; P(straight) = 1/1000. **Win 4:** Binomial(4, 0.1), E = 0.4; P(straight) = 1/10000.

### Scoring metrics
1. Match counts vs hypergeometric/binomial expectation; cumulative z-score + p-value per strategy
2. Log-loss for strategies that emit probability vectors (uniform NLL is the bar)
3. Simulated prize EV (spend vs winnings — makes the house edge visceral)
4. Randomness test suite on the draws themselves, per rule era
5. `unpopular` scores identically to random on matches by design — its edge is only visible in modeled co-winner counts

## 4. LLM fine-tuning (July 2026 landscape)

- **OpenAI fine-tuning: winding down** (closed to new users; all job creation ends Jan 2027). Do not build on it.
- **Anthropic: no public fine-tuning API** (confirmed; few-shot + prompt caching is their path — we use Claude for the no-training LLM control arm).
- **Gemini: tuning removed from standard API**, Vertex-only. Too heavy.
- **Local (primary): MLX-LM** (`pip install mlx-lm`, v0.31.x) on Apple Silicon.
  `mlx_lm.lora` QLoRA on `mlx-community/Qwen3-4B-Instruct-*-4bit` or `Llama-3.2-3B-Instruct-4bit`;
  chat-format JSONL (`train/valid/test.jsonl`); 3–4B 4-bit fits in 16 GB, trains in minutes. Cost $0.
  (Unsloth is still CUDA-first — not the Mac path.)
- **Hosted (secondary): Fireworks.ai** — LoRA SFT ≈ $0.50/M train tokens, serverless adapter
  inference (no dedicated GPU). A year of daily examples ≈ 0.2M tokens ≈ <$1/run.
- Practical dataset floor ~50–100 examples; daily records give 365/yr.

### Eval protocol for the LLM arms
- **Time-ordered splits only** (train past → test future). Never random shuffles.
- Compare four arms on the identical test window: random baseline, frequency baseline,
  base-model few-shot, fine-tuned model.
- Metrics: mean matches vs null, per-number marginal vs uniform (chi-square),
  valid-JSON rate, prediction entropy over sampled outputs (watch for mode collapse
  toward recent/frequent numbers — the expected failure mode).
- Sample at temp ~0.7–1.0 N times per prompt; also record the temp-0 modal prediction.

## Key sources

- NY Open Data: https://data.ny.gov/resource/d6yy-54nr.json (+ `5xaw-6ayf`, `hsys-3def`, `dg63-4siq`)
- Texas Lottery CSV exports: https://www.texaslottery.com/export/sites/lottery/Games/
- Lotto randomness auditing: https://arxiv.org/pdf/0806.4595
- Israeli lottery pick-popularity study: https://www.cambridge.org/core/journals/judgment-and-decision-making/article/patterns-in-manually-selected-numbers-in-the-israeli-lottery/F7167C1DD46E4876DAFCDDD6CE8F238C
- Unpopular-number EV: http://understandinguncertainty.org/it-possible-improve-your-chances-winning-big-national-lottery.html
- Abrams & Garibaldi "Finding good bets in the lottery": Am. Math. Monthly 117(1) 2010
- Rosenthal, Ontario lottery fraud analysis: https://probability.ca/jeff/ftpdir/lotteryart.pdf
- Cash WinFall / Selbee: https://highline.huffingtonpost.com/articles/en/lotto-winners/
- Hot Lotto RNG fraud: https://en.wikipedia.org/wiki/Hot_Lotto_fraud_scandal
- MLX-LM LoRA docs: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md
- Fireworks fine-tuning: https://docs.fireworks.ai
- LSTM-at-chance writeups: https://github.com/Ahmad-Alam/Lottery-Prediction , https://medium.com/mind-code/statistical-deception-predicting-lottery-numbers-with-ai-d555b521e5a5
