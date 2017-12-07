import argparse
import json
import re

import numpy as np
from sklearn.cluster import KMeans


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--npz")
  parser.add_argument("--title")
  parser.add_argument("--id")
  return parser.parse_args()


def main():
  args = parse_args()
  data = np.load(open(args.npz, "rb"))["vectors"]
  ids = open(args.id).readlines()
  titles = open(args.title).readlines()
  classes = classify(data)
  for id_, title, class_ in zip(ids, titles, classes):
    print(f"{class_} {title}\n\t{id_}")

def classify(data):
  km = KMeans(
      n_clusters=9,
      init='k-means++',
      n_init=10,
      max_iter=300,
      tol=1e-04,
      random_state=0)
  return km.fit_predict(data)


if __name__ == '__main__':
  main()
