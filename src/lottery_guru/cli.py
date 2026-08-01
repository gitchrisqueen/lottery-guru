"""lottery-guru command-line interface."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="lottery-guru")
    sub = parser.add_subparsers(dest="command", required=True)

    p_pull = sub.add_parser("pull", help="fetch latest drawing results")
    p_pull.add_argument("--limit", type=int, default=200,
                        help="rows per game (use e.g. 20000 for a full backfill)")

    p_predict = sub.add_parser("predict", help="generate today's predictions")
    p_predict.add_argument("--date", type=dt.date.fromisoformat, default=None)
    p_predict.add_argument("--no-llm", action="store_true", help="skip the LLM arm")

    sub.add_parser("score", help="score predictions whose results have arrived")
    sub.add_parser("report", help="regenerate REPORT.md")

    p_board = sub.add_parser(
        "board", help="render latest predictions to PREDICTIONS.md + README section"
    )
    p_board.add_argument("--date", default=None, help="default: most recent prediction date")

    sub.add_parser("daily", help="pull + score + predict + report (the cron entry point)")

    p_usage = sub.add_parser("usage", help="log Fireworks usage/cost to data/usage/")
    p_usage.add_argument("--days", type=int, default=1, help="window to request from billingUsage")
    p_usage.add_argument("--summary-only", action="store_true",
                         help="print totals from the committed log without calling the API")

    p_ft = sub.add_parser("finetune", help="fine-tuning pipeline")
    ft_sub = p_ft.add_subparsers(dest="ft_command", required=True)
    p_export = ft_sub.add_parser("export", help="export train/valid/test JSONL")
    p_export.add_argument("--out", default="finetune_data")
    p_export.add_argument("--max-per-game", type=int, default=500,
                          help="most recent draws per game (large value = full history)")
    p_train = ft_sub.add_parser("train", help="LoRA fine-tune (local MLX or hosted Fireworks)")
    p_train.add_argument("--data", default="finetune_data")
    p_train.add_argument("--iters", type=int, default=400, help="mlx only")
    p_train.add_argument("--provider", choices=["mlx", "fireworks"], default="mlx")
    p_train.add_argument("--epochs", type=int, default=None, help="fireworks only")
    p_train.add_argument("--min-scored-days", type=int, default=0,
                         help="fireworks only: skip cleanly (exit 0) below this many scored days")
    p_eval = ft_sub.add_parser("eval", help="held-out test loss, base vs tuned")
    p_eval.add_argument("--data", default="finetune_data")
    p_eval.add_argument("--adapter", default=None)
    p_deploy = ft_sub.add_parser(
        "deploy", help="fireworks: on-demand deployment for the recorded tuned model")
    p_deploy.add_argument("--only-if-drawings", nargs="?", const="any", default=None,
                          choices=["any", "jackpot", "digit"],
                          help="skip cleanly when no game of this kind draws today — never pay "
                               "for GPU time there is nothing to predict with (default: any)")
    p_deploy.add_argument("--date", type=dt.date.fromisoformat, default=None)
    ft_sub.add_parser("teardown", help="fireworks: delete the recorded deployment (stops GPU billing)")

    args = parser.parse_args(argv)

    from . import predictor
    from .evaluation import board, report

    if args.command == "pull":
        added = predictor.pull(limit=args.limit)
        print(json.dumps({"added": added}))
    elif args.command == "predict":
        include_llm = False if args.no_llm else None
        preds = predictor.predict(date=args.date, include_llm=include_llm)
        print(f"{len(preds)} predictions on file for {args.date or dt.date.today()}")
    elif args.command == "score":
        n = predictor.score_pending()
        print(f"scored {n} predictions")
    elif args.command == "report":
        report.write_report()
        print("wrote REPORT.md")
    elif args.command == "board":
        board.publish(date=args.date)
        print("wrote PREDICTIONS.md and updated README section")
    elif args.command == "daily":
        added = predictor.pull()
        n = predictor.score_pending()
        preds = predictor.predict()
        report.write_report()
        board.publish()
        print(json.dumps({"added": added, "scored": n, "predictions": len(preds)}))
    elif args.command == "usage":
        from .finetune import usage
        if not args.summary_only:
            usage.log_billing_usage(days=args.days)
        print(json.dumps(usage.summary(), indent=1))
    elif args.command == "finetune":
        if args.ft_command == "export":
            from .finetune import dataset
            counts = dataset.export(out_dir=args.out, max_per_game=args.max_per_game)
            print(json.dumps(counts))
        elif args.ft_command == "train":
            if args.provider == "fireworks":
                from .finetune import fireworks
                fireworks.train(data_dir=args.data, epochs=args.epochs,
                                min_scored_days=args.min_scored_days)
            else:
                from .finetune import train_mlx
                path = train_mlx.train(data_dir=args.data, iters=args.iters)
                print(f"adapter written to {path}")
        elif args.ft_command == "eval":
            from .finetune import train_mlx
            train_mlx.evaluate(data_dir=args.data, adapter_path=args.adapter)
        elif args.ft_command == "deploy":
            from .finetune import fireworks
            from .games import draws_on
            date = args.date or dt.date.today()
            if args.only_if_drawings:
                kind = args.only_if_drawings
                scheduled = [(g, t) for g, t in draws_on(date)
                             if kind == "any" or g.kind == kind]
                if not scheduled:
                    label = "" if kind == "any" else f"{kind} "
                    print(f"no {label}drawings on {date} — skipping deployment")
                    return 0
            record = fireworks.load_record()
            if not fireworks.available() or not record:
                # expected before the first fine-tune — clean skip, so the
                # daily loop is never blocked by the tuned arm
                print("no tuned model to deploy — skipping")
                return 0
            fireworks._deploy_and_record(record)
            if not fireworks.load_record().get("deployed"):
                return 1  # visible failure; callers treat the tuned arm as best-effort
            print(f"deployment ready: {fireworks.load_record()['deployment']}")
        elif args.ft_command == "teardown":
            from .finetune import fireworks
            fireworks.teardown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
