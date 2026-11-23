# Lottery Guru — Strategy Leaderboard

_Generated 2026-11-23 10:28 UTC. Null hypothesis: no strategy beats chance. A strategy is only interesting if |z| stays large as n grows — expect them all to converge to z ≈ 0. Arms with fewer than 50 scored draws are marked `(n<50, not yet interpretable)`: their z and p are printed for completeness but are too noisy to read as evidence either way._

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
| random | 240 | 92 | 72.0 | 2.485 | 0.013 | 0 |
| numerology | 208 | 70 | 62.4 | 1.014 | 0.3105 | 1 |
| contrarian | 208 | 70 | 62.4 | 1.014 | 0.3105 | 0 |
| llm-fewshot | 235 | 78 | 70.5 | 0.942 | 0.3464 | 0 |
| llm-tuned _(n<50, not yet interpretable)_ | 36 | 13 | 10.8 | _0.706_ | _0.4804_ | 0 |
| highest-frequency | 224 | 71 | 67.2 | 0.489 | 0.6251 | 0 |
| dreambook | 208 | 62 | 62.4 | -0.053 | 0.9574 | 0 |
| persistent | 208 | 58 | 62.4 | -0.587 | 0.5571 | 0 |
| hot | 240 | 67 | 72.0 | -0.621 | 0.5345 | 1 |
| cold | 240 | 66 | 72.0 | -0.745 | 0.4561 | 0 |
| skiphit | 208 | 56 | 62.4 | -0.854 | 0.3931 | 0 |
| moonphase | 208 | 54 | 62.4 | -1.121 | 0.2623 | 1 |
| positional | 240 | 61 | 72.0 | -1.366 | 0.1718 | 0 |

## NY Win 4

Null expectation: 0.4000 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| positional | 241 | 111 | 96.4 | 1.567 | 0.117 | 0 |
| random | 241 | 105 | 96.4 | 0.923 | 0.3559 | 0 |
| skiphit | 209 | 91 | 83.6 | 0.853 | 0.3936 | 0 |
| persistent | 209 | 91 | 83.6 | 0.853 | 0.3936 | 0 |
| cold | 241 | 103 | 96.4 | 0.709 | 0.4786 | 0 |
| highest-frequency | 225 | 94 | 90.0 | 0.444 | 0.6567 | 0 |
| numerology | 209 | 86 | 83.6 | 0.277 | 0.782 | 0 |
| contrarian | 209 | 80 | 83.6 | -0.415 | 0.6781 | 0 |
| dreambook | 209 | 78 | 83.6 | -0.646 | 0.5185 | 0 |
| llm-tuned _(n<50, not yet interpretable)_ | 36 | 12 | 14.4 | _-0.667_ | _0.505_ | 0 |
| moonphase | 209 | 75 | 83.6 | -0.991 | 0.3215 | 0 |
| llm-fewshot | 237 | 83 | 94.8 | -1.277 | 0.2014 | 0 |
| hot | 241 | 79 | 96.4 | -1.868 | 0.0618 | 0 |

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

