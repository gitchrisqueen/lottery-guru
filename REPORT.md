# Lottery Guru — Strategy Leaderboard

_Generated 2026-08-10 11:31 UTC. Null hypothesis: no strategy beats chance. A strategy is only interesting if |z| stays large as n grows — expect them all to converge to z ≈ 0._

## Powerball

Null expectation: 0.3623 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| random | 7 | 4 | 2.536 | 0.984 | 0.3252 | 0 |
| highest-frequency | 4 | 2 | 1.449 | 0.49 | 0.6244 | 0 |
| delta | 7 | 2 | 2.536 | -0.36 | 0.7186 | 0 |
| cold | 7 | 1 | 2.536 | -1.032 | 0.3019 | 0 |
| llm-tuned | 4 | 0 | 1.449 | -1.288 | 0.1976 | 0 |
| llm-fewshot | 6 | 0 | 2.174 | -1.578 | 0.1146 | 0 |
| unpopular | 7 | 0 | 2.536 | -1.704 | 0.0883 | 0 |
| hot | 7 | 0 | 2.536 | -1.704 | 0.0883 | 0 |

## Mega Millions

Null expectation: 0.3571 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| highest-frequency | 2 | 2 | 0.714 | 1.627 | 0.1038 | 0 |
| unpopular | 5 | 2 | 1.786 | 0.171 | 0.8639 | 0 |
| random | 5 | 2 | 1.786 | 0.171 | 0.8639 | 0 |
| hot | 5 | 2 | 1.786 | 0.171 | 0.8639 | 0 |
| delta | 5 | 2 | 1.786 | 0.171 | 0.8639 | 0 |
| cold | 5 | 2 | 1.786 | 0.171 | 0.8639 | 0 |
| llm-fewshot | 4 | 1 | 1.429 | -0.383 | 0.7014 | 0 |
| llm-tuned | 2 | 0 | 0.714 | -0.904 | 0.3662 | 0 |

## NY Numbers (Pick 3)

Null expectation: 0.3000 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| highest-frequency | 13 | 9 | 3.9 | 2.722 | 0.0065 | 0 |
| hot | 27 | 14 | 8.1 | 2.185 | 0.0289 | 0 |
| llm-tuned | 10 | 5 | 3.0 | 1.217 | 0.2235 | 0 |
| random | 27 | 10 | 8.1 | 0.704 | 0.4816 | 0 |
| cold | 27 | 10 | 8.1 | 0.704 | 0.4816 | 0 |
| llm-fewshot | 23 | 8 | 6.9 | 0.441 | 0.6589 | 0 |
| positional | 27 | 8 | 8.1 | -0.037 | 0.9705 | 0 |

## NY Win 4

Null expectation: 0.4000 matches per prediction.

| Strategy | n | Observed | Expected | z | p | Straights |
|---|---|---|---|---|---|---|
| positional | 30 | 15 | 12.0 | 0.913 | 0.3613 | 0 |
| llm-tuned | 10 | 5 | 4.0 | 0.527 | 0.5982 | 0 |
| highest-frequency | 14 | 6 | 5.6 | 0.178 | 0.8586 | 0 |
| cold | 30 | 12 | 12.0 | 0.0 | 1.0 | 0 |
| random | 30 | 11 | 12.0 | -0.304 | 0.7609 | 0 |
| llm-fewshot | 26 | 9 | 10.4 | -0.458 | 0.6472 | 0 |
| hot | 30 | 9 | 12.0 | -0.913 | 0.3613 | 0 |

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

