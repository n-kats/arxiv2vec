import sys

import cli
import dataset.json_arxiv
from cli import parse_args
from actions import train, infer


def main():
  args, unknown = parse_args(sys.argv[1:])
  mode = args.mode
  if mode == "train":
    """
    trainの場合は、モデルや前処理の設定が混在して、
    それらを分離するために複数のparserを使っている
    """
    args = cli.parse_train_args(unknown)
    train.run(args)
  elif mode == "infer":
    infer.run(args)
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
