import argparse
import json
import re


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--json")
  parser.add_argument("--output_summary")
  parser.add_argument("--output_summary_dir")
  parser.add_argument("--output_id")
  parser.add_argument("--output_title")
  parser.add_argument("--target")
  return parser.parse_args()


def main():
  args = parse_args()
  data = json.load(open(args.json))
  ids = []
  summaries = []
  titles = []
  for item in data:
    if args.target in item["summary"]:
      if item["id"] not in ids:
        ids.append(item["id"])
        summaries.append(item["summary"])
        titles.append(item["title"])
  write_out(args.output_id, ids)
  write_out(args.output_summary, summaries)
  write_out(args.output_title, titles)

  for i, s in enumerate(summaries):
    with open(f"{args.output_summary_dir}/input_{i:06}.txt", "w") as f:
      f.write(s)


def write_out(fname, items):
  with open(fname, "w") as f:
    f.write("\n".join([re.sub("\s*\n\s*", " ", item) for item in items]) + "\n")


if __name__ == '__main__':
  main()
