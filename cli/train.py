import argparse


def add_argument_to_train(parser):
  """
  何もしない
  """


def parse_train_args(args):
  parser = argparse.ArgumentParser()
  parser.add_argument("--model", required=True)
  parser.add_argument("--preprocess", required=True)
  args_train, unknown = parser.parse_known_args(args)
  add_document_args(parser)
  add_model_args(args_train.model, parser)
  add_preprocess_args(args_train.preprocess, parser)
  return parser.parse_args(args)


def add_model_args(model_name, parser):
  parser.add_argument('--save_model')


def add_document_args(parser):
  parser.add_argument('--train_data')


def add_preprocess_args(preprocess_name, parser):
  parser.add_argument("--tex", help="$\\TeX$")
  parser.add_argument("--normal", help="素朴な方法")
