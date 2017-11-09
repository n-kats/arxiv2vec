import argparse


def add_argument_for_dataset(parser: argparse.ArgumentParser):
  subparsers = parser.add_subparsers(dest="dataset_mode")
  add_argument_for_json_arxiv_data(
      subparsers.add_parser("json_arxiv", help="arXivのデータを今回用に加工"))
  add_argument_for_merge_json(
      subparsers.add_parser("merge_json", help="jsonファイルの統合"))


def add_argument_for_json_arxiv_data(parser: argparse.ArgumentParser):
  parser.add_argument('--input', required=True, nargs='+')
  parser.add_argument('--output', required=True)


def add_argument_for_merge_json(parser: argparse.ArgumentParser):
  parser.add_argument('--input', required=True, nargs='+')
  parser.add_argument('--output', required=True)
