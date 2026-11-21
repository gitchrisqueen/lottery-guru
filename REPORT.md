# Lottery Guru — Strategy Leaderboard

_Generated 2026-11-21 10:26 UTC. Null hypothesis: no strategy beats chance. A strategy is only interesting if |z| stays large as n grows — expect them all to converge to z ≈ 0. Arms with fewer than 50 scored draws are marked `(n<50, not yet interpretable)`: their z and p are printed for completeness but are too noisy to read as evidence either way._

## Powerball

Null expectation: 0.3623 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| random | 51 | 24 | 18.478 | 1.375 | 0.1692 | 0 |
| benford _(n<50, not yet interpretable)_ | 44 | 21 | 15.942 | _1.356_ | _0.1752_ | 0 |
| persistent _(n<50, not yet interpretable)_ | 44 | 20 | 15.942 | _1.088_ | _0.2767_ | 0 |
| birthday _(n<50, not yet interpretable)_ | 44 | 18 | 15.942 | _0.552_ | _0.5812_ | 0 |
| unpopular | 51 | 19 | 18.478 | 0.13 | 0.8966 | 0 |
| antibalanced _(n<50, not yet interpretable)_ | 44 | 16 | 15.942 | _0.016_ | _0.9876_ | 0 |
| cold | 51 | 18 | 18.478 | -0.119 | 0.9052 | 0 |
| moonphase _(n<50, not yet interpretable)_ | 44 | 15 | 15.942 | _-0.253_ | _0.8006_ | 0 |
| balanced _(n<50, not yet interpretable)_ | 44 | 15 | 15.942 | _-0.253_ | _0.8006_ | 0 |
| numerology _(n<50, not yet interpretable)_ | 44 | 14 | 15.942 | _-0.521_ | _0.6027_ | 0 |
| highest-frequency _(n<50, not yet interpretable)_ | 48 | 14 | 17.391 | _-0.87_ | _0.3841_ | 0 |
| llm-fewshot | 50 | 14 | 18.116 | -1.035 | 0.3007 | 0 |
| llm-tuned _(n<50, not yet interpretable)_ | 11 | 2 | 3.986 | _-1.064_ | _0.2871_ | 0 |
| skiphit _(n<50, not yet interpretable)_ | 44 | 11 | 15.942 | _-1.325_ | _0.1853_ | 0 |
| contrarian _(n<50, not yet interpretable)_ | 44 | 11 | 15.942 | _-1.325_ | _0.1853_ | 0 |
| hot | 51 | 13 | 18.478 | -1.364 | 0.1726 | 0 |
| delta | 51 | 11 | 18.478 | -1.862 | 0.0626 | 0 |

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
| random | 236 | 89 | 70.8 | 2.28 | 0.0226 | 0 |
| contrarian | 204 | 69 | 61.2 | 1.051 | 0.2933 | 0 |
| llm-fewshot | 231 | 77 | 69.3 | 0.975 | 0.3296 | 0 |
| numerology | 204 | 68 | 61.2 | 0.916 | 0.3595 | 1 |
| llm-tuned _(n<50, not yet interpretable)_ | 36 | 13 | 10.8 | _0.706_ | _0.4804_ | 0 |
| highest-frequency | 220 | 70 | 66.0 | 0.519 | 0.6038 | 0 |
| dreambook | 204 | 61 | 61.2 | -0.027 | 0.9785 | 0 |
| persistent | 204 | 57 | 61.2 | -0.566 | 0.5715 | 0 |
| hot | 236 | 65 | 70.8 | -0.727 | 0.4675 | 1 |
| skiphit | 204 | 55 | 61.2 | -0.835 | 0.4035 | 0 |
| cold | 236 | 63 | 70.8 | -0.977 | 0.3285 | 0 |
| moonphase | 204 | 53 | 61.2 | -1.105 | 0.2692 | 1 |
| positional | 236 | 60 | 70.8 | -1.353 | 0.1761 | 0 |

## NY Win 4

Null expectation: 0.4000 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| positional | 237 | 109 | 94.8 | 1.537 | 0.1242 | 0 |
| persistent | 205 | 90 | 82.0 | 0.931 | 0.3517 | 0 |
| random | 237 | 103 | 94.8 | 0.888 | 0.3747 | 0 |
| skiphit | 205 | 89 | 82.0 | 0.815 | 0.4152 | 0 |
| cold | 237 | 102 | 94.8 | 0.779 | 0.4357 | 0 |
| highest-frequency | 221 | 90 | 88.4 | 0.179 | 0.8576 | 0 |
| numerology | 205 | 82 | 82.0 | 0.0 | 1.0 | 0 |
| dreambook | 205 | 78 | 82.0 | -0.466 | 0.6415 | 0 |
| contrarian | 205 | 78 | 82.0 | -0.466 | 0.6415 | 0 |
| llm-tuned _(n<50, not yet interpretable)_ | 36 | 12 | 14.4 | _-0.667_ | _0.505_ | 0 |
| moonphase | 205 | 73 | 82.0 | -1.048 | 0.2948 | 0 |
| llm-fewshot | 233 | 80 | 93.2 | -1.441 | 0.1495 | 0 |
| hot | 237 | 78 | 94.8 | -1.819 | 0.0689 | 0 |

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

