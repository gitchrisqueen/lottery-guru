# Lottery Guru — Strategy Leaderboard

_Generated 2026-11-20 10:27 UTC. Null hypothesis: no strategy beats chance. A strategy is only interesting if |z| stays large as n grows — expect them all to converge to z ≈ 0. Arms with fewer than 50 scored draws are marked `(n<50, not yet interpretable)`: their z and p are printed for completeness but are too noisy to read as evidence either way._

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
| random | 232 | 89 | 69.6 | 2.451 | 0.0142 | 0 |
| contrarian | 200 | 69 | 60.0 | 1.225 | 0.2207 | 0 |
| llm-fewshot | 227 | 76 | 68.1 | 1.009 | 0.3129 | 0 |
| numerology | 200 | 66 | 60.0 | 0.816 | 0.4142 | 1 |
| llm-tuned _(n<50, not yet interpretable)_ | 36 | 13 | 10.8 | _0.706_ | _0.4804_ | 0 |
| highest-frequency | 216 | 70 | 64.8 | 0.681 | 0.4959 | 0 |
| dreambook | 200 | 60 | 60.0 | -0.0 | 1.0 | 0 |
| skiphit | 200 | 55 | 60.0 | -0.68 | 0.4962 | 0 |
| persistent | 200 | 55 | 60.0 | -0.68 | 0.4962 | 0 |
| hot | 232 | 64 | 69.6 | -0.708 | 0.4792 | 1 |
| moonphase | 200 | 53 | 60.0 | -0.953 | 0.3408 | 1 |
| cold | 232 | 61 | 69.6 | -1.087 | 0.2772 | 0 |
| positional | 232 | 60 | 69.6 | -1.213 | 0.2251 | 0 |

## NY Win 4

Null expectation: 0.4000 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| positional | 233 | 108 | 93.2 | 1.616 | 0.1061 | 0 |
| persistent | 201 | 88 | 80.4 | 0.893 | 0.3716 | 0 |
| skiphit | 201 | 87 | 80.4 | 0.776 | 0.4378 | 0 |
| cold | 233 | 100 | 93.2 | 0.742 | 0.4578 | 0 |
| random | 233 | 99 | 93.2 | 0.633 | 0.5265 | 0 |
| numerology | 201 | 82 | 80.4 | 0.188 | 0.8508 | 0 |
| highest-frequency | 217 | 86 | 86.8 | -0.091 | 0.9279 | 0 |
| dreambook | 201 | 76 | 80.4 | -0.517 | 0.605 | 0 |
| contrarian | 201 | 75 | 80.4 | -0.635 | 0.5256 | 0 |
| llm-tuned _(n<50, not yet interpretable)_ | 36 | 12 | 14.4 | _-0.667_ | _0.505_ | 0 |
| moonphase | 201 | 72 | 80.4 | -0.987 | 0.3234 | 0 |
| llm-fewshot | 229 | 80 | 91.6 | -1.278 | 0.2014 | 0 |
| hot | 233 | 76 | 93.2 | -1.878 | 0.0604 | 0 |

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

