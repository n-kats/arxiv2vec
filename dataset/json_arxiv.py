import json
import os
import re

NEW_LINE_RGX = re.compile("\n\s*")


def run(input_: str, output: str):
  input_abs = os.path.abspath(input_)
  output_abs = os.path.abspath(output)
  with open(input_abs) as f_in, open(output_abs, "w") as f_out:
    for l in f_in:
      obj = json.loads(l)
      f_out.write(_fix_needless_new_line(obj["abstract"]) + "\n")


def _fix_needless_new_line(s: str):
  return re.sub(NEW_LINE_RGX, " ", s)
