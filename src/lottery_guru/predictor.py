"""Daily orchestration: pull results, generate predictions, score outcomes."""
from __future__ import annotations

import datetime as dt

from .data import sources, store
from .evaluation import scoring
from .games import GAMES, draws_on
from .strategies import REGISTRY, run_strategy, seeded_rng
from .strategies import consensus
from .strategies import llm as llm_strategy


def pull(limit: int = 200) -> dict[str, int]:
    """Fetch latest draws for all games and merge into the store."""
    added = {}
    for game in GAMES.values():
        try:
            draws = sources.fetch_draws(game, limit=limit)
        except Exception as exc:  # one bad feed must not block the other games
            print(f"WARNING: pull failed for {game.key}: {exc}")
            continue
        added[game.key] = store.merge_draws(game.key, draws)
    # integrity cross-check against the Texas Lottery feed
    pb = {d.date: d for d in store.load_draws("powerball") if d.draw_time == "main"}
    for warning in sources.cross_check_powerball(pb):
        print(f"WARNING: {warning}")
    return added


def predict(date: dt.date | None = None, include_llm: bool | None = None) -> list[dict]:
    """Generate predictions for every game drawing on `date` (default today)."""
    date = date or dt.date.today()
    date_str = date.isoformat()
    if include_llm is None:
        include_llm = llm_strategy.available()

    existing = store.load_json_list("predictions", date_str)
    seen = {(p["game"], p["draw_time"], p["strategy"]) for p in existing}
    predictions = list(existing)

    for game, draw_time in draws_on(date):
        history = [d for d in store.load_draws(game.key) if d.date < date_str]
        strategies = [name for name, (_, ok) in REGISTRY.items() if ok(game)]
        for name in strategies:
            if (game.key, draw_time, name) in seen:
                continue
            rng = seeded_rng(name, game.key, date_str, draw_time)
            pred = run_strategy(name, game, history, rng)
            predictions.append({
                "game": game.key,
                "draw_time": draw_time,
                "strategy": name,
                "numbers": list(pred.numbers),
                "special": pred.special,
            })
        llm_arms = []
        if include_llm:
            llm_arms.append(("llm-fewshot", llm_strategy.predict_fewshot))
            if llm_strategy.tuned_available():
                llm_arms.append(("llm-tuned", llm_strategy.predict_tuned))
        for name, predict_fn in llm_arms:
            if (game.key, draw_time, name) in seen:
                continue
            rng = seeded_rng(name, game.key, date_str, draw_time)
            try:
                pred = predict_fn(game, history, rng)
                predictions.append({
                    "game": game.key,
                    "draw_time": draw_time,
                    "strategy": name,
                    "numbers": list(pred.numbers),
                    "special": pred.special,
                })
            except Exception as exc:  # LLM arms are best-effort; never block the loop
                print(f"WARNING: {name} failed for {game.key}/{draw_time}: {exc}")

        # Consensus runs last: it ranks what every other arm picked for THIS
        # drawing only — never pooled across games or draw times.
        if (game.key, draw_time, consensus.NAME) not in seen:
            peers = [
                (p["numbers"], p.get("special")) for p in predictions
                if p["game"] == game.key and p["draw_time"] == draw_time
                and p["strategy"] != consensus.NAME
            ]
            if peers:  # nothing to tally means no honest consensus to report
                rng = seeded_rng(consensus.NAME, game.key, date_str, draw_time)
                numbers, special = consensus.predict(game, peers, rng)
                predictions.append({
                    "game": game.key,
                    "draw_time": draw_time,
                    "strategy": consensus.NAME,
                    "numbers": list(numbers),
                    "special": special,
                })

    if len(predictions) > len(existing):
        store.save_json_list("predictions", date_str, predictions)
    return predictions


def score_pending() -> int:
    """Score every prediction whose actual result has arrived. Idempotent."""
    scored_count = 0
    draws_cache = {key: {(d.date, d.draw_time): d for d in store.load_draws(key)} for key in GAMES}
    for date in store.all_dates("predictions"):
        preds = store.load_json_list("predictions", date)
        evals = store.load_json_list("evaluations", date)
        done = {(e["game"], e["draw_time"], e["strategy"]) for e in evals}
        changed = False
        for p in preds:
            key = (p["game"], p["draw_time"], p["strategy"])
            if key in done:
                continue
            actual = draws_cache[p["game"]].get((date, p["draw_time"]))
            if actual is None:
                continue  # result not in yet — self-heals on a later run
            game = GAMES[p["game"]]
            s = scoring.score(game, p["numbers"], p.get("special"), list(actual.numbers), actual.special)
            evals.append({
                **p,
                "actual_numbers": list(actual.numbers),
                "actual_special": actual.special,
                "score": s,
            })
            changed = True
            scored_count += 1
        if changed:
            store.save_json_list("evaluations", date, evals)
    return scored_count
