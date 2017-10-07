import argparse

from cli.dataset import add_argument_for_dataset


def add_argument_for_document(parser):
  parser.add_argument('--document')
  parser.add_argument('--preprocess')


def add_argument_to_train(parser):
  add_argument_for_document(parser)
  parser.add_argument('--save_model')


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


def add_model_detail_args(parser):
  add_model_args(parser)
  add_preprocess_args(parser)


def add_model_args(parser):
  pass


def add_preprocess_args(parser):
  subparsers = parser.add_subparsers(dest="preprocess_mode")
  add_argument_to_tex(subparsers.add_parser("tex", help="$\\TeX$"))
  add_argument_to_normal(subparsers.add_parser("normal", help="素朴な方法"))
