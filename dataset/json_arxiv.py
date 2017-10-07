import json
import os
import re

NEW_LINE_RGX = re.compile("\n\s*")


def run(inputs: str, output: str):
  output_abs = os.path.abspath(output)
  with open(output_abs, "w") as f_out:
    for input_ in inputs:
      input_abs = os.path.abspath(input_)
      for obj in json.load(open(input_abs)):
        f_out.write(_fix_needless_new_line(obj["summary"]) + "\n")


def _fix_needless_new_line(s: str):
  return re.sub(NEW_LINE_RGX, " ", s)
