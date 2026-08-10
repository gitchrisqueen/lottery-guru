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
import time

import requests

from ..games import Game
from .sources import Draw

PRIMARY_BASE = "https://files.floridalottery.com/exptkt"
MIRROR_BASE = "https://apps.flalottery.com/exptkt"
TIMEOUT = 60
RETRIES = 3  # rounds over both hosts
BACKOFF_BASE = 20.0  # seconds before the next round; doubles each round
REQUEST_SPACING = 2.0  # courtesy gap so seven games aren't fetched as a burst
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
    """Fetch one history PDF, trying both hosts with backoff between rounds.

    The CDN in front of these files answers a burst of large downloads by
    refusing the TLS handshake outright (SSLV3_ALERT_HANDSHAKE_FAILURE) rather
    than returning an HTTP status, and it keeps refusing for a while. Pulling
    seven games back-to-back is exactly that burst, so requests are spaced and
    retried, and every host's error is reported — reporting only the last one
    hides which host actually failed and how.
    """
    errors: list[str] = []
    for attempt in range(RETRIES):
        for base in (PRIMARY_BASE, MIRROR_BASE):
            time.sleep(REQUEST_SPACING)
            try:
                resp = requests.get(
                    f"{base}/{stem}.pdf", headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT
                )
                resp.raise_for_status()
                return resp.content
            except requests.RequestException as exc:
                host = base.split("/")[2]
                errors.append(f"attempt {attempt + 1} {host}: {type(exc).__name__}: {exc}")
        if attempt < RETRIES - 1:
            time.sleep(BACKOFF_BASE * 2**attempt)
    raise RuntimeError(f"FL {stem}.pdf unavailable; " + "; ".join(errors))


def iter_page_texts(pdf_bytes: bytes):
    """Yield each page's text, lazily.

    Layout-aware extraction is expensive (seconds per page on the 130-page
    Pick files), so pages are yielded one at a time and the caller stops as
    soon as it has enough draws. The files are newest-first, so the daily
    pull touches a handful of pages instead of all of them.
    """
    import io

    import pdfplumber

    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            yield page.extract_text(layout=True) or ""


def fetch_draws(game: Game, limit: int = 200) -> list[Draw]:
    draws: list[Draw] = []
    for text in iter_page_texts(_download(game.fl_pdf_stem)):
        draws.extend(parse_text(game, text))
        if limit is not None and len(draws) >= limit:
            break
    return draws[:limit] if limit is not None else draws
