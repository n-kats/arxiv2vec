import argparse


def add_argument_to_infer(parser: argparse.ArgumentParser):
  subparsers = parser.add_subparsers(dest="infer_mode")
  add_argument_to_show_vector(
      subparsers.add_parser("show_vector", help="ベクトル表示"))
  add_argument_to_compare(
      subparsers.add_parser("compare", help="比較"))
  add_argument_to_find_neighbors(
      subparsers.add_parser("find_neighbors", help="近傍探索"))


def add_argument_to_show_vector(parser: argparse.ArgumentParser):
  _add_infer_common_args(parser)


def add_argument_to_compare(parser: argparse.ArgumentParser):
  _add_infer_common_args(parser)


def add_argument_to_find_neighbors(parser: argparse.ArgumentParser):
  parser.add_argument('--train_data')
  _add_infer_common_args(parser)


def _add_infer_common_args(parser: argparse.ArgumentParser):
  parser.add_argument('--load_model')
  parser.add_argument('--input_texts', nargs="+")
