from argparse import Namespace
import pickle
from typing import (
    Any,
    Optional,
    Callable,
    Dict,
    NewType,
    cast,
)

import numpy as np


Model = NewType("Model", object)
_actions: Dict[str, Callable[[Model, Namespace], None]] = {}


def by_action_name(
    name: Optional[str] = None,
    actions: Dict[str, Callable[[Model, Namespace], None]] = _actions,
) -> Callable[[Callable], None]:
  def _action(fn: Callable):
    key: str = name or fn.__name__
    assert key not in _actions
    _actions[key] = fn
  return _action


def run_action(
    action_name: str,
    model: Model,
    args: Namespace,
):
  _actions[action_name](model, args)


def run(args: Namespace):
  model = load_model(args.load_model)
  run_action(args.infer_mode, model, args)


def load_model(path: str) -> Model:
  return cast(Model, pickle.load(cast(Any, open(path, "rb"))))


@by_action_name()
def show_vector(model: Model, args: Namespace):
  """
  文章に対し評価し、そのベクトルを表示する
  """
  for input_ in args.input_texts:
    text = _get_input_text(input_)
    vec = model.infer_vector(text)
    print(input_)
    print(vec)


@by_action_name()
def compare(model: Model, args: Namespace):
  vec_l = model.infer_vector(_get_input_text(args.input_texts[0]))
  vec_r = model.infer_vector(_get_input_text(args.input_texts[1]))
  vec_l /= np.sqrt(sum(vec_l * vec_l))
  vec_r /= np.sqrt(sum(vec_r * vec_r))
  print("cos = ", sum(vec_r * vec_l))


@by_action_name()
def find_neighbors(model: Model, args: Namespace):
  """
  近傍探索を行う
  """
  targets = open(args.train_data).readlines()
  for input_ in args.input_texts:
    print(f"--- INPUT: {input_}")
    vec = model.infer_vector(_get_input_text(input_))
    top_scores = model.find_neighbors(vec)
    for order, (i, score) in enumerate(top_scores):
      print("---", order + 1, i, score)
      print(targets[i])


def _get_input_text(fname: str) -> str:
  return "".join(open(fname))
