import json
import os

from dataset.utils import fix_needless_new_line


def run(inputs: str, output: str):
  output_abs = os.path.abspath(output)
  with open(output_abs, "w") as f_out:
    for input_ in inputs:
      input_abs = os.path.abspath(input_)
      for obj in json.load(open(input_abs)):
        f_out.write(fix_needless_new_line(obj["summary"]) + "\n")
