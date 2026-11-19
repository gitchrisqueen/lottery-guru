# Lottery Guru — Strategy Leaderboard

_Generated 2026-11-19 10:26 UTC. Null hypothesis: no strategy beats chance. A strategy is only interesting if |z| stays large as n grows — expect them all to converge to z ≈ 0. Arms with fewer than 50 scored draws are marked `(n<50, not yet interpretable)`: their z and p are printed for completeness but are too noisy to read as evidence either way._

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
| benford _(n<50, not yet interpretable)_ | 29 | 18 | 10.357 | _2.539_ | _0.0111_ | 0 |
| birthday _(n<50, not yet interpretable)_ | 29 | 15 | 10.357 | _1.543_ | _0.123_ | 0 |
| cold _(n<50, not yet interpretable)_ | 34 | 17 | 12.143 | _1.49_ | _0.1361_ | 0 |
| skiphit _(n<50, not yet interpretable)_ | 29 | 13 | 10.357 | _0.878_ | _0.3799_ | 0 |
| balanced _(n<50, not yet interpretable)_ | 29 | 13 | 10.357 | _0.878_ | _0.3799_ | 0 |
| llm-tuned _(n<50, not yet interpretable)_ | 7 | 3 | 2.5 | _0.338_ | _0.7353_ | 0 |
| highest-frequency _(n<50, not yet interpretable)_ | 31 | 12 | 11.071 | _0.298_ | _0.7654_ | 0 |
| numerology _(n<50, not yet interpretable)_ | 29 | 11 | 10.357 | _0.214_ | _0.8309_ | 0 |
| unpopular _(n<50, not yet interpretable)_ | 34 | 10 | 12.143 | _-0.657_ | _0.5109_ | 0 |
| random _(n<50, not yet interpretable)_ | 34 | 10 | 12.143 | _-0.657_ | _0.5109_ | 0 |
| hot _(n<50, not yet interpretable)_ | 34 | 10 | 12.143 | _-0.657_ | _0.5109_ | 0 |
| delta _(n<50, not yet interpretable)_ | 34 | 10 | 12.143 | _-0.657_ | _0.5109_ | 0 |
| persistent _(n<50, not yet interpretable)_ | 29 | 8 | 10.357 | _-0.783_ | _0.4336_ | 0 |
| antibalanced _(n<50, not yet interpretable)_ | 29 | 8 | 10.357 | _-0.783_ | _0.4336_ | 0 |
| llm-fewshot _(n<50, not yet interpretable)_ | 33 | 9 | 11.786 | _-0.868_ | _0.3856_ | 0 |
| moonphase _(n<50, not yet interpretable)_ | 29 | 7 | 10.357 | _-1.115_ | _0.2647_ | 0 |
| contrarian _(n<50, not yet interpretable)_ | 29 | 6 | 10.357 | _-1.448_ | _0.1477_ | 0 |

## NY Numbers (Pick 3)

Null expectation: 0.3000 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| random | 230 | 88 | 69.0 | 2.411 | 0.0159 | 0 |
| contrarian | 198 | 69 | 59.4 | 1.313 | 0.1892 | 0 |
| llm-fewshot | 225 | 76 | 67.5 | 1.091 | 0.2755 | 0 |
| highest-frequency | 214 | 70 | 64.2 | 0.763 | 0.4454 | 0 |
| llm-tuned _(n<50, not yet interpretable)_ | 36 | 13 | 10.8 | _0.706_ | _0.4804_ | 0 |
| numerology | 198 | 64 | 59.4 | 0.629 | 0.5293 | 1 |
| dreambook | 198 | 59 | 59.4 | -0.055 | 0.9564 | 0 |
| skiphit | 198 | 55 | 59.4 | -0.602 | 0.5473 | 0 |
| hot | 230 | 64 | 69.0 | -0.634 | 0.5258 | 1 |
| persistent | 198 | 54 | 59.4 | -0.739 | 0.4602 | 0 |
| moonphase | 198 | 53 | 59.4 | -0.875 | 0.3814 | 1 |
| cold | 230 | 61 | 69.0 | -1.015 | 0.31 | 0 |
| positional | 230 | 60 | 69.0 | -1.142 | 0.2534 | 0 |

## NY Win 4

Null expectation: 0.4000 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| positional | 231 | 108 | 92.4 | 1.711 | 0.0871 | 0 |
| persistent | 199 | 87 | 79.6 | 0.874 | 0.382 | 0 |
| random | 231 | 99 | 92.4 | 0.724 | 0.4692 | 0 |
| skiphit | 199 | 85 | 79.6 | 0.638 | 0.5235 | 0 |
| cold | 231 | 98 | 92.4 | 0.614 | 0.5392 | 0 |
| numerology | 199 | 81 | 79.6 | 0.165 | 0.8686 | 0 |
| highest-frequency | 215 | 84 | 86.0 | -0.227 | 0.8202 | 0 |
| dreambook | 199 | 76 | 79.6 | -0.425 | 0.6706 | 0 |
| llm-tuned _(n<50, not yet interpretable)_ | 36 | 12 | 14.4 | _-0.667_ | _0.505_ | 0 |
| moonphase | 199 | 72 | 79.6 | -0.898 | 0.3692 | 0 |
| contrarian | 199 | 72 | 79.6 | -0.898 | 0.3692 | 0 |
| llm-fewshot | 227 | 79 | 90.8 | -1.305 | 0.1918 | 0 |
| hot | 231 | 76 | 92.4 | -1.798 | 0.0721 | 0 |

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

