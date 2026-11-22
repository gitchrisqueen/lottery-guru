# Lottery Guru — Strategy Leaderboard

_Generated 2026-11-22 10:27 UTC. Null hypothesis: no strategy beats chance. A strategy is only interesting if |z| stays large as n grows — expect them all to converge to z ≈ 0. Arms with fewer than 50 scored draws are marked `(n<50, not yet interpretable)`: their z and p are printed for completeness but are too noisy to read as evidence either way._

## Powerball

Null expectation: 0.3623 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| random | 52 | 24 | 18.841 | 1.272 | 0.2033 | 0 |
| benford _(n<50, not yet interpretable)_ | 45 | 21 | 16.304 | _1.245_ | _0.2133_ | 0 |
| persistent _(n<50, not yet interpretable)_ | 45 | 20 | 16.304 | _0.98_ | _0.3273_ | 0 |
| birthday _(n<50, not yet interpretable)_ | 45 | 18 | 16.304 | _0.449_ | _0.6531_ | 0 |
| unpopular | 52 | 20 | 18.841 | 0.286 | 0.775 | 0 |
| moonphase _(n<50, not yet interpretable)_ | 45 | 16 | 16.304 | _-0.081_ | _0.9357_ | 0 |
| antibalanced _(n<50, not yet interpretable)_ | 45 | 16 | 16.304 | _-0.081_ | _0.9357_ | 0 |
| cold | 52 | 18 | 18.841 | -0.207 | 0.8358 | 0 |
| numerology _(n<50, not yet interpretable)_ | 45 | 15 | 16.304 | _-0.346_ | _0.7295_ | 0 |
| balanced _(n<50, not yet interpretable)_ | 45 | 15 | 16.304 | _-0.346_ | _0.7295_ | 0 |
| highest-frequency _(n<50, not yet interpretable)_ | 49 | 14 | 17.754 | _-0.953_ | _0.3404_ | 0 |
| llm-tuned _(n<50, not yet interpretable)_ | 11 | 2 | 3.986 | _-1.064_ | _0.2871_ | 0 |
| llm-fewshot | 51 | 14 | 18.478 | -1.115 | 0.2648 | 0 |
| skiphit _(n<50, not yet interpretable)_ | 45 | 11 | 16.304 | _-1.406_ | _0.1597_ | 0 |
| contrarian _(n<50, not yet interpretable)_ | 45 | 11 | 16.304 | _-1.406_ | _0.1597_ | 0 |
| hot | 52 | 13 | 18.841 | -1.44 | 0.1498 | 0 |
| delta | 52 | 12 | 18.841 | -1.687 | 0.0917 | 0 |

## Mega Millions

Null expectation: 0.3571 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| benford _(n<50, not yet interpretable)_ | 30 | 18 | 10.714 | _2.38_ | _0.0173_ | 0 |
| birthday _(n<50, not yet interpretable)_ | 30 | 15 | 10.714 | _1.4_ | _0.1615_ | 0 |
| cold _(n<50, not yet interpretable)_ | 35 | 17 | 12.5 | _1.361_ | _0.1736_ | 0 |
| skiphit _(n<50, not yet interpretable)_ | 30 | 13 | 10.714 | _0.747_ | _0.4553_ | 0 |
| balanced _(n<50, not yet interpretable)_ | 30 | 13 | 10.714 | _0.747_ | _0.4553_ | 0 |
| llm-tuned _(n<50, not yet interpretable)_ | 7 | 3 | 2.5 | _0.338_ | _0.7353_ | 0 |
| highest-frequency _(n<50, not yet interpretable)_ | 32 | 12 | 11.429 | _0.181_ | _0.8566_ | 0 |
| numerology _(n<50, not yet interpretable)_ | 30 | 11 | 10.714 | _0.093_ | _0.9256_ | 0 |
| random _(n<50, not yet interpretable)_ | 35 | 12 | 12.5 | _-0.151_ | _0.8798_ | 0 |
| delta _(n<50, not yet interpretable)_ | 35 | 11 | 12.5 | _-0.454_ | _0.6501_ | 0 |
| llm-fewshot _(n<50, not yet interpretable)_ | 34 | 10 | 12.143 | _-0.657_ | _0.5109_ | 0 |
| unpopular _(n<50, not yet interpretable)_ | 35 | 10 | 12.5 | _-0.756_ | _0.4496_ | 0 |
| hot _(n<50, not yet interpretable)_ | 35 | 10 | 12.5 | _-0.756_ | _0.4496_ | 0 |
| persistent _(n<50, not yet interpretable)_ | 30 | 8 | 10.714 | _-0.887_ | _0.3753_ | 0 |
| moonphase _(n<50, not yet interpretable)_ | 30 | 8 | 10.714 | _-0.887_ | _0.3753_ | 0 |
| antibalanced _(n<50, not yet interpretable)_ | 30 | 8 | 10.714 | _-0.887_ | _0.3753_ | 0 |
| contrarian _(n<50, not yet interpretable)_ | 30 | 6 | 10.714 | _-1.54_ | _0.1236_ | 0 |

## NY Numbers (Pick 3)

Null expectation: 0.3000 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| random | 238 | 90 | 71.4 | 2.32 | 0.0203 | 0 |
| llm-fewshot | 233 | 78 | 69.9 | 1.021 | 0.3071 | 0 |
| numerology | 206 | 69 | 61.8 | 0.965 | 0.3343 | 1 |
| contrarian | 206 | 69 | 61.8 | 0.965 | 0.3343 | 0 |
| llm-tuned _(n<50, not yet interpretable)_ | 36 | 13 | 10.8 | _0.706_ | _0.4804_ | 0 |
| highest-frequency | 222 | 71 | 66.6 | 0.568 | 0.5698 | 0 |
| dreambook | 206 | 62 | 61.8 | 0.027 | 0.9786 | 0 |
| hot | 238 | 67 | 71.4 | -0.549 | 0.5831 | 1 |
| persistent | 206 | 57 | 61.8 | -0.644 | 0.5198 | 0 |
| skiphit | 206 | 56 | 61.8 | -0.778 | 0.4367 | 0 |
| cold | 238 | 63 | 71.4 | -1.048 | 0.2947 | 0 |
| moonphase | 206 | 53 | 61.8 | -1.18 | 0.238 | 1 |
| positional | 238 | 61 | 71.4 | -1.297 | 0.1945 | 0 |

## NY Win 4

Null expectation: 0.4000 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| positional | 239 | 111 | 95.6 | 1.66 | 0.0969 | 0 |
| persistent | 207 | 91 | 82.8 | 0.95 | 0.3422 | 0 |
| random | 239 | 104 | 95.6 | 0.906 | 0.3652 | 0 |
| skiphit | 207 | 90 | 82.8 | 0.834 | 0.4042 | 0 |
| cold | 239 | 103 | 95.6 | 0.798 | 0.425 | 0 |
| highest-frequency | 223 | 93 | 89.2 | 0.424 | 0.6715 | 0 |
| numerology | 207 | 84 | 82.8 | 0.139 | 0.8894 | 0 |
| contrarian | 207 | 79 | 82.8 | -0.44 | 0.6598 | 0 |
| dreambook | 207 | 78 | 82.8 | -0.556 | 0.5782 | 0 |
| llm-tuned _(n<50, not yet interpretable)_ | 36 | 12 | 14.4 | _-0.667_ | _0.505_ | 0 |
| moonphase | 207 | 74 | 82.8 | -1.019 | 0.308 | 0 |
| llm-fewshot | 235 | 81 | 94.0 | -1.413 | 0.1575 | 0 |
| hot | 239 | 78 | 95.6 | -1.897 | 0.0578 | 0 |

## Exploit watch

_The only people who ever reliably made money on lotteries exploited payout structure — roll-down caps (Cash WinFall) or jackpots exceeding the cost of every combination (Mandel) — never prediction. These monitors check the tracked games for those defects; "no opportunity" is the expected, and real, result. See docs/UNORTHODOX.md._

| Game | Combinations | Full-buyout cost | Break-even advertised jackpot | Roll-down defect |
|---|---|---|---|---|
| Powerball | 292,201,338 | $584,402,676 | $1,933M | none |
| Mega Millions | 290,472,336 | $580,944,672 | $1,921M | none |
| FL Fantasy 5 | 376,992 | $376,992 | $1M | none |
| Florida Lotto | 22,957,480 | $22,957,480 | $76M | none |
| FL Jackpot Triple Play | 9,366,819 | $9,366,819 | $31M | none |

_No tracked game has a capped-jackpot roll-down (the WinFall defect); unclaimed jackpots roll over, keeping per-ticket EV below cost. Digit-game payouts are fixed-odds (500:1 on a 1-in-1,000 straight), a structural house edge no monitor can wait out. Even when a record jackpot clears the naive buyout threshold, split risk and the post-Mandel bulk-purchase bans keep the door closed — that is the finding._

