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
    ft_sub.add_parser("deploy", help="fireworks: on-demand deployment for the recorded tuned model")
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
            record = fireworks.load_record()
            if not record:
                raise SystemExit("no tuned model on record")
            deployment = fireworks.deploy(record["model"])
            record.update({"deployed": True, "deployment": deployment,
                           "inference_model": f"{record['model']}#{deployment}"})
            fireworks.save_record(record)
            print(f"deployment ready: {deployment}")
        elif args.ft_command == "teardown":
            from .finetune import fireworks
            fireworks.teardown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
