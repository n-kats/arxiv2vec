import argparse

from cli.dataset import add_argument_for_dataset
from cli.train import (
    add_argument_to_train,
    parse_train_args,
    )


def add_argument_for_document(parser):
  parser.add_argument('--document')
  parser.add_argument('--preprocess')


def add_argument_to_infer(parser):
  add_argument_for_document(parser)
  parser.add_argument('--load_model')


def parse_args(args):
  """
  argsはsys.argv[1:]を想定している
  """
  parser = argparse.ArgumentParser()
  subparsers = parser.add_subparsers(dest="mode")
  add_argument_to_train(subparsers.add_parser("train", help="学習"))
  add_argument_to_infer(subparsers.add_parser("infer", help="実行"))
  add_argument_for_dataset(subparsers.add_parser("dataset", help="dataset"))
  return parser.parse_known_args(args)
