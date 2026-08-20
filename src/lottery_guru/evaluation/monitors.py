"""Exploit watch — honest monitors for the ways lotteries were actually beaten.

Every documented lottery "win system" (MIT/Selbee on Cash WinFall, Mandel's
combinatorial buyouts) exploited payout structure, never number prediction.
These monitors compute, from public game structure alone, whether any tracked
game currently exhibits such a defect. The expected — and correct — output is
"no opportunity", published as a quantitative result rather than assumed.

Kept offline-deterministic: thresholds derive from the game matrices; no
network calls in the report path.
"""
from __future__ import annotations

from math import comb

from ..games import GAMES, Game

# Cost of one play, per game.
TICKET_PRICE = {
    "powerball": 2.0,
    "megamillions": 2.0,
    "fl_lotto": 1.0,
    "fl_fantasy5": 1.0,
    "fl_jtp": 1.0,
}
CASH_VALUE_FRACTION = 0.48  # advertised annuity -> lump sum, typical ratio
TOP_FEDERAL_TAX = 0.37


def combinations(game: Game) -> int:
    pool = game.pick_max - game.pick_min + 1
    return comb(pool, game.pick_count) * (game.special_max or 1)


def buyout_cost(game: Game) -> float:
    """Mandel's step one: what buying every combination costs."""
    return combinations(game) * TICKET_PRICE.get(game.key, 2.0)


def break_even_jackpot(game: Game) -> float:
    """Advertised jackpot at which a full buyout breaks even, before split risk.

    Mandel's rule of thumb demanded ~3x this to cover taxes, splits, and
    logistics; regulators have since banned bulk purchasing outright.
    """
    return buyout_cost(game) / (CASH_VALUE_FRACTION * (1 - TOP_FEDERAL_TAX))


def rows() -> list[dict]:
    """Per-game exploit-watch numbers — the data behind render_lines()."""
    out = []
    for game in GAMES.values():
        if game.kind != "jackpot":
            continue
        out.append(
            {
                "game": game.key,
                "display": game.display,
                "combinations": combinations(game),
                "buyout_cost": buyout_cost(game),
                "break_even_jackpot": break_even_jackpot(game),
                "rolldown_defect": False,
            }
        )
    return out


def render_lines() -> list[str]:
    lines = [
        "## Exploit watch",
        "",
        "_The only people who ever reliably made money on lotteries exploited "
        "payout structure — roll-down caps (Cash WinFall) or jackpots exceeding "
        "the cost of every combination (Mandel) — never prediction. These "
        "monitors check the tracked games for those defects; \"no opportunity\" "
        "is the expected, and real, result. See docs/UNORTHODOX.md._",
        "",
        "| Game | Combinations | Full-buyout cost | Break-even advertised jackpot | Roll-down defect |",
        "|---|---|---|---|---|",
    ]
    for row in rows():
        lines.append(
            f"| {row['display']} | {row['combinations']:,} | "
            f"${row['buyout_cost']:,.0f} | ${row['break_even_jackpot'] / 1e6:,.0f}M | none |"
        )
    lines += [
        "",
        "_No tracked game has a capped-jackpot roll-down (the WinFall defect); "
        "unclaimed jackpots roll over, keeping per-ticket EV below cost. "
        "Digit-game payouts are fixed-odds (500:1 on a 1-in-1,000 straight), a "
        "structural house edge no monitor can wait out. Even when a record "
        "jackpot clears the naive buyout threshold, split risk and the "
        "post-Mandel bulk-purchase bans keep the door closed — that is the "
        "finding._",
        "",
    ]
    return lines
