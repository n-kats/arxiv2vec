import json
import os

from dataset.utils import fix_needless_new_line


def run(inputs: str, output: str):
  output_abs = os.path.abspath(output)
  data = []
  for input_ in inputs:
    input_abs = os.path.abspath(input_)
    data += json.load(open(input_abs))
  for i, data_per_paper in enumerate(data):
    data[i]["summary"] = fix_needless_new_line(data[i]["summary"])

  with open(output_abs, "w") as f_out:
    json.dump(data, f_out)
