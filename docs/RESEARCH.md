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

### Third-party APIs (APIVerve, magayo, lotteryresultsapi, collectapi)

All add auth/quotas/lag and none beat the free government feeds. Fallback only.

### Draw schedule (ET)

- Powerball: Mon/Wed/Sat 10:59 PM — 5 of 69 white + 1 of 26
- Mega Millions: Tue/Fri 11:00 PM — 5 of 70 white + 1 of 24 (since Apr 2025; **never pool stats across rule eras**)
- NY Numbers/Win 4: daily, midday 2:30 PM + evening 10:30 PM
- Take 5: daily, midday + evening

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
