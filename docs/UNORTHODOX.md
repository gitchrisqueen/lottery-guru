# Unorthodox Lottery Strategies — Catalog and Automation Survey

Research pass 2026-08-09. Every folk method people report "winning with" was
classified three ways: **automated arm** (pure function of history + date +
seed → implemented in `strategies/`), **monitor** (a structural-defect
detector in `evaluation/monitors.py` — the honest half of a human-required
exploit), or **human-required** (needs capital, physical tickets, or a group;
documented here with requirements, because they cannot and should not be
code). The project's framing holds throughout: under a fair draw, every
pick-generating rule below is provably equivalent to a seeded random pick.
The only measurable differences are prize-splitting exposure and variance —
never hit rate.

## 1. Automated arms (implemented, in `REGISTRY`)

| Arm | Folk claim | Mechanical rule | Expected result |
|---|---|---|---|
| `contrarian` | — (inversion of a measured bias) | play numbers drawn in the last 3 draws | chance on matches; lower split exposure. Clotfelter & Cook (Mgmt. Sci. 1993) showed the public under-bets a number for months after it hits |
| `birthday` | dates are lucky; play birthdays | weighted sample from 1–31, months (1–12) 3× | chance on matches; **worst-case split exposure** — the deliberate mirror of `unpopular` |
| `balanced` | winning tickets have mid-range sums and 3:2 odd/even | reject-sample into the middle sum band + balanced parity | chance — the band merely contains more combinations; every combination is equiprobable |
| `antibalanced` | — (inversion) | force extreme sums or single-parity | chance on matches; shapes the crowd avoids |
| `skiphit` | Gail Howard: numbers have characteristic skip patterns; ~half of winners repeat from recent draws | carry 1–2 repeats from the last draw; fill with numbers whose current skip matches their modal historical gap | chance — fair-draw skips are geometric and memoryless |
| `benford` | winning numbers should follow Benford's law | pick the candidate ticket closest to Benford leading-digit frequencies | chance, **and wrong on its face**: bounded uniform ranges are the textbook Benford counterexample. Kept as a known-wrong negative control |
| `persistent` | Lustig: pick numbers and never change them (7 FL wins, 1993–2010) | one fixed ticket per game, forever (seeded from game key only — documented seeding exception) | chance; persistence cannot change memoryless odds. The cleanest null demo in the portfolio |
| `moonphase` | lunar phase governs luck | synodic phase angle for the draw date folded into the seed; uniform picks | chance — it is literally a seeded RNG in a costume, which is the point |
| `numerology` | Pythagorean name/birth numbers are personally lucky | persona ("Lottery Guru", b. 2026-07-01) → name number + life path + personal day → expanded into the pool | chance |
| `dreambook` | dreams map to daily 3-digit plays (Harlem numbers tradition: Parris's *H. P. Dream Book* 1926, *Policy Pete's* 1933, *Aunt Sally's* before them) | seeded daily symbol from a policy-era lexicon → its fixed digits (digit games only — dream books are natively Pick-3 instruments) | chance |

Also pre-existing: `unpopular` (the one arm with defensible EV logic — split
avoidance), `hot`, `cold`, `delta`, `positional`, the LLM arms, and
`highest-frequency` consensus.

Not implemented, considered and rejected:

- **Wheeling (covering designs).** Real mathematics — a (v, k, t) wheel
  guarantees a minimum tier *if* t of your v numbers are drawn — but it is a
  multi-ticket instrument. Scoring it against single-ticket arms without a
  cost-normalized lane (payout per dollar) would flatter it dishonestly.
  Revisit only alongside a prize-EV scoring lane.
- **Fortune-cookie corpus.** No official feed exists; the tradition's real
  lesson is the 2005-03-30 Powerball drawing, kept below as an exhibit.
- **Lottery software** (Lotto Pro, Advantage Gold, Expert Lotto). Repackaged
  skip charts + sum filters + wheels — all already covered by `skiphit`,
  `balanced`, and the wheeling rejection above. Nothing to buy or implement.

## 2. Monitors (implemented, in `evaluation/monitors.py` → REPORT.md "Exploit watch")

The people who actually made money exploited **payout structure**, never
prediction. The monitors compute, nightly and offline, whether any tracked
game exhibits those defects:

- **Mandel gate** — combinations × ticket price vs break-even advertised
  jackpot (after ~48% cash-value and 37% federal tax discounts). Powerball
  needs a ≈$1.9B advertised jackpot before a full buyout merely breaks even,
  pre-split.
- **Roll-down detector** — does any tracked game cap its jackpot and roll
  the excess into lower tiers (the WinFall defect)? Structural answer today:
  no; unclaimed jackpots roll over.

"No opportunity" is the expected and correct output, published as a result.

## 3. Human-required strategies — interpretation and requirements

These cannot be pick-generating arms. Each entry states what it actually
was, what it would require, and which automated piece this project runs.

### 3.1 Cash WinFall roll-down syndicates (MIT / Random Strategies; the Selbees)

**What it was.** Massachusetts Cash WinFall (6/46, $2) capped its jackpot at
$2M; when capped and unwon, the jackpot **rolled down** into the 5-, 4-, and
3-match tiers, pushing per-ticket EV above ticket price on those draws.
Random Strategies Investments LLC (James Harvey & Yuran Lu, out of MIT's
Random Hall) wagered ≈$17–18M for ≥$3.5M profit, 2005–2012. Jerry & Marge
Selbee (GS Investment Strategies LLC, Evart, Michigan) found the same defect
independently on Michigan's Winfall, moved to the Massachusetts game when
Michigan closed it, and netted ≈$7.75M on ≈$27M wagered over nine years. The
2012 Inspector General report found the Lottery knew and tolerated it; **the
players broke no rules**. The game was shut down in January 2012.

**Requirements to replicate.** (1) A game with a capped-jackpot roll-down —
extinct in the US since WinFall closed; (2) ≈$600k+ per roll-down draw so
the law of large numbers makes the 15–20% edge reliable; (3) retailer
cooperation to print hundreds of thousands of tickets; (4) days of physical
ticket sorting per draw (the Selbees logged 10-hour days); (5) an LLC and
written profit-sharing agreements.

**Automated half here:** the roll-down detector. If a qualifying game ever
appears among tracked games, the monitor is the tripwire.

### 3.2 Mandel-style combinatorial buyout

**What it was.** Stefan Mandel won 14 lotteries by buying **every
combination** when the jackpot sufficiently exceeded the combination count —
most famously Virginia, 1992-02-15: 6/44 = 7,059,052 combinations at $1
against a ≈$27M jackpot; his syndicate printed and processed ~7M tickets
through 100+ retail outlets, took the jackpot plus ~135,000 secondary
prizes. Investigated by IRS/FBI/CIA; no wrongdoing found. Regulators then
banned bulk purchasing and off-premises ticket printing specifically to
foreclose the method.

**Requirements to replicate.** (1) jackpot ≳3× total combination cost
(Mandel's margin for taxes, split risk, and logistics); (2) the full ticket
cost raised up front from investors; (3) bulk printing and retail
distribution — now explicitly illegal in US jurisdictions; (4) tolerance for
the catastrophic tail: a single co-winner halves the jackpot.

**Automated half here:** the Mandel gate. For Powerball (292,201,338
combinations, $584M of tickets) the break-even advertised jackpot is ≈$1.9B
before split adjustment — the monitor publishes that threshold per game.

### 3.3 Scratch-off shelf tracking (Srivastava's singleton method; remaining-prize tables)

**What it was.** Toronto statistician Mohan Srivastava found (2003) that an
Ontario tic-tac-toe scratch game leaked its winners on the visible face:
numbers appearing exactly once ("singletons") three-in-a-row marked a winner
~90% of the time, because tickets are generated to an exact prize budget.
He reported it to the lottery (it paid less than his day rate); the game was
pulled. The surviving legitimate observation: scratch games' remaining-EV
genuinely varies over their life, and every US lottery publishes
remaining-prize tables (daily/weekly), so games can be *ranked* by remaining
top-prizes per remaining ticket.

**Requirements to replicate.** Ranking is computable (state remaining-prize
pages; aggregators like LottoEdge). Execution is inherently physical: buying
specific tickets at specific retailers, and the EV virtually never crosses
ticket price (30–40% house edge on instants). The singleton-style defect
itself has been remediated industry-wide. Out of scope for a draw-game
project; anyone pursuing it needs retail access, a per-game spreadsheet of
remaining prizes vs estimated remaining tickets, and the discipline to treat
it as loss-minimization, not profit.

### 3.4 Syndicates / pools

**What they are.** N people × M tickets raises the group's chance of
*holding* a winner by exactly NM tickets' worth — while per-dollar EV is
unchanged and each share shrinks by 1/N. Pooling is variance reduction, not
edge; it was the *enabling mechanism* for 3.1 and 3.2, where the edge came
from elsewhere. **Requirements:** a written agreement (contribution,
draw window, custody of tickets, split procedure — disputes over verbal
pools are well documented), a custodian, and group patience. A simulated
syndicate arm (N tickets scored at 1/N share) was considered and deferred —
like wheels, it needs the cost-normalized scoring lane first.

### 3.5 Exhibit: the fortune-cookie split (why `unpopular` exists)

Powerball 2005-03-30 drew 22, 28, 32, 33, 39 + PB 42. **110 players** hit
the second tier with the same five whites — all from one Wonton Food fortune
slip ("22, 28, 32, 33, 39, 40") printed in ~4M cookies/day. The lottery
investigated (coincidence, all prizes paid, ≈$19M total). It is the cleanest
real-world demonstration that **correlated picks dilute prizes** — the
entire case for `unpopular` and against `birthday`, in one drawing. Roughly
70–80% of tickets are Quick Picks, which caps how much popularity distortion
self-pickers can create — and is why the split-avoidance edge is real but
small.

## Key sources

- Mass. Inspector General, Cash WinFall letter (July 2012): https://www.mass.gov/files/documents/2016/08/vv/lottery-cash-winfall-letter-july-2012.pdf
- "The Lottery Hackers" (Selbee), HuffPost Highline: https://highline.huffingtonpost.com/articles/en/lotto-winners/
- Selbee 60 Minutes segment: https://www.cbsnews.com/news/jerry-and-marge-selbee-how-a-retired-couple-won-millions-using-a-lottery-loophole-60-minutes-2019-06-09/
- Mandel method, NPR Planet Money: https://www.npr.org/sections/money/2019/07/09/726339472/the-math-whiz-who-won-the-lottery-14-times
- Srivastava singleton method, Wired (2011) via Gizmodo: https://gizmodo.com/how-a-statistician-beat-scratch-lottery-tickets-5748942
- Fortune-cookie drawing, Snopes: https://www.snopes.com/fact-check/fortune-cookie-fortune/
- Clotfelter & Cook, "The 'Gambler's Fallacy' in Lottery Play": https://www.nber.org/papers/w3769
- Baker & McHale, conscious selection in the UK National Lottery (prize-winnings distribution modeling)
- White, Garton, Robertson & White, *Playing the Numbers: Gambling in Harlem Between the Wars* (Harvard UP, 2010)
- Lottery wheeling / covering designs: https://en.wikipedia.org/wiki/Lottery_wheeling
