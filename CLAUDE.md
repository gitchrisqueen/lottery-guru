# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this project is

An automated, honest lottery-prediction experiment. A daily GitHub Actions loop
pulls real drawing results, generates predictions from a portfolio of
strategies, scores them against actual drawings, and updates REPORT.md. The
scientific framing is central: **the null hypothesis (no strategy beats
chance) is expected to hold** — the project measures that convergence.
Never add code or copy that implies predictions can actually beat the lottery.

Read [docs/PLAN.md](docs/PLAN.md) (architecture, milestones),
[docs/RESEARCH.md](docs/RESEARCH.md) (data sources, strategy literature,
null-hypothesis math), and [docs/UNORTHODOX.md](docs/UNORTHODOX.md) (folk
strategy catalog; human-required exploits and their monitor halves) before
making non-trivial changes.

## Commands

```bash
pip install -e ".[dev]"          # install with test deps
pytest                            # run the test suite
lottery-guru daily                # pull + score + predict + report (cron entry point)
lottery-guru pull --limit 2000    # backfill draw history
lottery-guru predict [--date YYYY-MM-DD] [--no-llm]
lottery-guru score                # score predictions whose results arrived (idempotent)
lottery-guru report               # regenerate REPORT.md
lottery-guru board                # render PREDICTIONS.md + README marker sections
lottery-guru site [--out dist]    # build the static GitHub Pages dashboard (HTML + JSON)
lottery-guru usage [--summary-only]       # log/report Fireworks usage → data/usage/fireworks.jsonl
lottery-guru finetune export|train|eval   # MLX fine-tuning (macOS only)
lottery-guru finetune train --provider fireworks --min-scored-days 60  # hosted (CI; monthly workflow)
lottery-guru finetune deploy [--only-if-drawings jackpot] | teardown   # tuned-model GPU (teardown stops billing)
```

## Architecture

- `src/lottery_guru/games.py` — game definitions (Powerball 5/69+1/26,
  Mega Millions 5/70+1/24, NY Numbers, NY Win 4, and the FL games:
  Fantasy 5 5/36, Lotto 6/53, Jackpot Triple Play 6/46, Pick 2–5) and draw
  schedules. FL jackpot games have **no special ball** (`special_max=None`) —
  every arm must handle that. `TUNED_ARM_GAMES` gates GPU deployment days.
- `src/lottery_guru/data/` — Socrata fetchers (data.ny.gov), FL PDF fetcher
  (`florida.py`: files.floridalottery.com/exptkt/*.pdf, mirror failover,
  date-anchored regex parsing — Florida has no open-data portal), TX CSV
  cross-check, JSON storage under `data/` (**git is the database**; raw draws,
  predictions, and evaluations are committed by the daily workflow). Each
  game's pull soft-fails independently — one bad feed never blocks the loop.
- `src/lottery_guru/strategies/` — each strategy is `(predict_fn, applicable_fn)`
  in `REGISTRY`. The LLM arm (`llm.py`) is provider-pluggable: Ollama
  (default, native `/api/chat` with JSON-schema `format`) or Anthropic.
  Two arms sit outside `REGISTRY` because they need more than
  `(game, history, rng)`, and are driven from `predictor.py`: the LLM arms,
  and `consensus.py` (`highest-frequency`), which ranks numbers by how many
  *other arms* picked them **for that one drawing** — never pooled across
  games or draw times. It is not `hot`: `hot` ranks by numbers actually drawn.
- `src/lottery_guru/evaluation/` — scoring vs exact hypergeometric/binomial
  null moments, cumulative z-tests, REPORT.md rendering (arms with
  n < `report.MIN_N` = 50 are flagged "not yet interpretable", never
  dropped), `monitors.py`
  (the "Exploit watch" section: Mandel-gate buyout math and roll-down
  structural flags — offline-deterministic, expected verdict "no
  opportunity"), and `board.py`
  (PREDICTIONS.md + the README `PREDICTIONS`/`SCOREBOARD` marker sections).
  README sections are spliced between HTML comment markers — never hand-edit
  content inside them; it is regenerated every run.
- `src/lottery_guru/predictor.py` — daily orchestration; `score_pending()` is
  idempotent and self-heals late-arriving results.
- `src/lottery_guru/finetune/` — time-ordered JSONL export + MLX-LM LoRA wrapper
  (local) + Fireworks.ai LoRA client (`fireworks.py`, trained monthly by
  `.github/workflows/monthly-finetune.yml`; the tuned model name is recorded in
  `data/finetune/fireworks.json` and served by the `llm-tuned` arm). Serving
  needs an on-demand GPU deployment that **bills while it exists** — the daily
  loop deploys, predicts, and tears down; teardown runs on `always()` and
  sweeps orphans. Never add a code path that creates a deployment without a
  guaranteed teardown.

## Hard rules

- **Determinism:** statistical strategies must be reproducible per
  (strategy, game, date, draw_time) via `seeded_rng()`. Never use unseeded
  randomness in a strategy. One documented exception: `persistent` seeds
  from (strategy, game) only — an unchanging ticket is its hypothesis; it is
  still fully deterministic. `moonphase`/`numerology` fold values derived
  from the newest history date into the seed, which stays a pure function of
  the inputs.
- **Time-ordered splits only** in fine-tuning: train on the past, test on the
  future. Never shuffle draws across the split boundary.
- **Never pool stats across rule eras** (Mega Millions changed to 5/70+1/24 in
  April 2025 — see `MEGAMILLIONS_ERA_START`).
- **LLM arm is best-effort:** it must never block or fail the daily loop;
  errors are warnings, and absence of credentials means clean skip.
- The scoring math in `evaluation/scoring.py` is verified against the exact
  hypergeometric PMF (Powerball var ≈ 0.31629) — don't "fix" it without
  re-deriving.

## Environment variables

| Var | Purpose |
|---|---|
| `OLLAMA_API_KEY` | Ollama Cloud auth (LLM arm; set as repo secret) |
| `OLLAMA_HOST` | Alternative Ollama endpoint (e.g. `http://localhost:11434`) |
| `LOTTERY_GURU_LLM_PROVIDER` | Force `ollama` or `anthropic` |
| `LOTTERY_GURU_LLM_MODEL` | Override model (default `gpt-oss:20b`) |
| `ANTHROPIC_API_KEY` | Anthropic provider (optional) |
| `FIREWORKS_API_KEY` | Fireworks.ai auth: monthly fine-tune + `llm-tuned` arm (repo secret) |
| `FIREWORKS_ACCOUNT_ID` | Fireworks.ai account slug (optional; auto-resolved from the key) |
| `LOTTERY_GURU_FT_BASE_MODEL` | Override the Fireworks fine-tune base model |
| `SOCRATA_APP_TOKEN` | Optional; lifts data.ny.gov throttling |

## Testing

`pytest` must pass before any push. Tests are network-free (live feeds are
exercised only by the daily workflow). When adding a strategy, extend
`tests/test_strategies.py` — validity, determinism, and applicability are the
required assertions.

## Cross-project context
Global rules for every session live in `~/.claude/CLAUDE.md` (sourced from the CQC Boss Vault, `00-Home/CLAUDE.global.md`). The vault is at `$CQC_VAULT` (fallback: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/CQC Boss Vault`); read it as plain files.
- This project's vault note: `60-Projects/Side-Products.md` (section "Lottery Guru") (create it per `00-Home/Vault-Conventions.md` if missing).
- Handoff packets: `80-Handoffs/HO-<date>-<n>-<slug>.md` per `80-Handoffs/Handoff-Protocol.md`.
- Tracker: none recorded (portfolio work items: `christopherqueenconsulting/gitchrisqueen` issues, per `60-Projects/Portfolio-Inbound-Plan-2026-09-03.md`).
- Other projects: look them up in `00-Home/Source-Map.md`; write anything another project needs to the vault, not to auto-memory.
- Decisions for Christopher: options with a recommendation, in chat (see `00-Home/Working-With-Christopher.md`).
