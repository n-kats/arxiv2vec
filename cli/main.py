import sys

import cli
import dataset.json_arxiv
from cli import parse_args


def main():
  args, unknown = parse_args(sys.argv[1:])
  mode = args.mode
  if mode == "train":
    """
    trainの場合は、モデルや前処理の設定が混在して、
    それらを分離するために複数のparserを使っている
    """
    model_args, unknown = cli.parse_model_args(unknown)
    preprocess = cli.parse_preprocess_args(
        args.preprocess, unknown)
    train.run(
        document=args.document,
        model_args=model_config,
        preprocess_args=preprocess,
        save_model=args.save_model)
  elif mode == "infer":
    infer.run(
        document=args.document,
        load_model=args.load_model)
  elif mode == "dataset":
    dataset_mode = args.dataset_mode
    if dataset_mode == "json_arxiv":
      dataset.json_arxiv.run(args.input, args.output)
    else:
      raise NotImplementedError(f"対応するモード({dataset_mode})が未実装です")
  else:
    raise NotImplementedError(f"対応するモード({mode})が未実装です")


if __name__ == '__main__':
  main()
