from typing import List
import argparse


def add_argument_to_train(parser: argparse.ArgumentParser):
  """
  何もしない
  """


def parse_train_args(args: List[str]):
  parser = argparse.ArgumentParser()
  parser.add_argument("--model", required=True)
  parser.add_argument("--preprocess", required=True)
  args_train, unknown = parser.parse_known_args(args)
  add_document_args(parser)
  add_model_args(args_train.model, parser)
  add_preprocess_args(args_train.preprocess, parser)
  return parser.parse_args(args)


def add_model_args(model_name: str, parser: argparse.ArgumentParser):
  parser.add_argument('--save_model', required=True)


def add_document_args(parser: argparse.ArgumentParser):
  parser.add_argument('--train_data', required=True)


def add_preprocess_args(
    preprocess_name: str,
    parser: argparse.ArgumentParser):
  pass
