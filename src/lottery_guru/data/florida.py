"""Florida Lottery fetchers.

Florida has no open-data portal; the official machine-readable source is the
set of daily-regenerated PDF history files at
https://files.floridalottery.com/exptkt/<stem>.pdf (mirror: apps.flalottery.com).
Newest-first, full history per file, M/D/YY dates.

Layouts vary per game and the PDFs flow records into 1-3 page columns, so
text extraction yields lines carrying up to three records. Parsing is
date-anchored regex findall per line, which also skips page headers and
disclaimer boilerplate without an explicit filter list:

- Fantasy 5 (ff):   ``8/8/26  EVENING  2  10  15  16  32``
- Lotto (l6):       ``08/08/26  3 - 11- 20 - 25- 40 - 42  LOTTO`` — Double
  Play rows are labeled ``LOTTO DP`` and dropped; pre-2021 rows are unlabeled.
- Triple Play (jtp): ``08/07/26  3 - 22 - 26 - 34 - 37 - 38`` (no labels).
- Pick 2-5 (p2..p5): ``08/08/26  E  6- 4- 3  FB 2`` — Fireball is an add-on
  draw, not part of the base game, and is dropped; pre-2019 rows have none.
"""
from __future__ import annotations

import re

import requests

from ..games import Game
from .sources import Draw

PRIMARY_BASE = "https://files.floridalottery.com/exptkt"
MIRROR_BASE = "https://apps.flalottery.com/exptkt"
TIMEOUT = 60
# The site sits behind a CDN/WAF; a descriptive browser-like UA avoids
# bot-blocking heuristics that a bare python-requests UA can trigger.
USER_AGENT = (
    "Mozilla/5.0 (compatible; lottery-guru/1.0; "
    "+https://github.com/gitchrisqueen/lottery-guru)"
)

# A date anchors every record: M/D/YY or MM/DD/YY, never followed by a digit
# (so the "8/09/2026 as of" generation timestamp in headers can't match).
_DATE = r"(\d{1,2}/\d{1,2}/\d{2})(?!\d)"

_DRAW_TIMES = {"MIDDAY": "midday", "EVENING": "evening", "M": "midday", "E": "evening"}


def _iso_date(mdy: str) -> str:
    m, d, y = (int(part) for part in mdy.split("/"))
    # Two-digit years span 1988 (Lotto launch) to today.
    year = 1900 + y if y >= 88 else 2000 + y
    return f"{year:04d}-{m:02d}-{d:02d}"


def _fantasy5_records(game: Game, line: str):
    pat = rf"{_DATE}\s+(MIDDAY|EVENING)\s+(\d{{1,2}}(?:\s+\d{{1,2}}){{{game.pick_count - 1}}})(?!\s*\d)"
    for date, draw_time, nums in re.findall(pat, line):
        numbers = tuple(sorted(int(n) for n in nums.split()))
        yield Draw(_iso_date(date), _DRAW_TIMES[draw_time], numbers, None)


def _dashed_jackpot_records(game: Game, line: str):
    pat = rf"{_DATE}\s+(\d{{1,2}}(?:\s*-\s*\d{{1,2}}){{{game.pick_count - 1}}})\s*(LOTTO DP|LOTTO)?"
    for date, nums, label in re.findall(pat, line):
        if label == "LOTTO DP":  # Double Play is a separate drawing — not tracked
            continue
        numbers = tuple(sorted(int(n) for n in re.split(r"\s*-\s*", nums)))
        yield Draw(_iso_date(date), "main", numbers, None)


def _digit_records(game: Game, line: str):
    pat = rf"{_DATE}\s+([EM])\s+(\d(?:\s*-\s*\d){{{game.pick_count - 1}}})(?:\s+FB\s*\d)?"
    for date, draw_time, digits in re.findall(pat, line):
        numbers = tuple(int(d) for d in re.split(r"\s*-\s*", digits))
        yield Draw(_iso_date(date), _DRAW_TIMES[draw_time], numbers, None)


def parse_text(game: Game, text: str, limit: int | None = None) -> list[Draw]:
    """Parse extracted PDF text into draws (newest-first, as the files are)."""
    if game.kind == "digit":
        extract = _digit_records
    elif game.fl_pdf_stem == "ff":
        extract = _fantasy5_records
    else:
        extract = _dashed_jackpot_records

    draws: list[Draw] = []
    for line in text.splitlines():
        for draw in extract(game, line):
            if all(game.pick_min <= n <= game.pick_max for n in draw.numbers):
                draws.append(draw)
        if limit is not None and len(draws) >= limit:
            break
    return draws[:limit] if limit is not None else draws


def _download(stem: str) -> bytes:
    last_exc: Exception | None = None
    for base in (PRIMARY_BASE, MIRROR_BASE):
        try:
            resp = requests.get(
                f"{base}/{stem}.pdf", headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT
            )
            resp.raise_for_status()
            return resp.content
        except requests.RequestException as exc:
            last_exc = exc
    raise RuntimeError(f"FL {stem}.pdf unavailable on both hosts: {last_exc}")


def _pdf_to_text(pdf_bytes: bytes) -> str:
    import io

    import pdfplumber

    pages = []
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            pages.append(page.extract_text(layout=True) or "")
    return "\n".join(pages)


def fetch_draws(game: Game, limit: int = 200) -> list[Draw]:
    text = _pdf_to_text(_download(game.fl_pdf_stem))
    return parse_text(game, text, limit=limit)
