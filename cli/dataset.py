def add_argument_for_dataset(parser):
  subparsers = parser.add_subparsers(dest="dataset_mode")
  add_argument_for_json_arxiv_data(
      subparsers.add_parser("json_arxiv", help="arXivのデータを今回用に加工"))


def add_argument_for_json_arxiv_data(parser):
  parser.add_argument('--input', required=True, nargs='+')
  parser.add_argument('--output', required=True)
