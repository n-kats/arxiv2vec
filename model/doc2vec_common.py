import pickle
from typing import Iterator

from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument


class Doc2VecModel:
  def __init__(self, preprocessor):
    self._preprocessor = preprocessor
    self._model = None

  def train(self, train_docs: Iterator[str]):
    train_corpus = [TaggedDocument(self._preprocessor.preprocess(txt), [i]) for i, txt in enumerate(train_docs)]
    model = Doc2Vec(size=50, min_count=2, iter=10000)
    model.build_vocab(train_corpus)
    model.train(train_corpus, total_examples=model.corpus_count, epochs=5)
    self._model = model

  def save(self, path: str):
    # ディレクトリ作成
    pickle.dump(self, open(path, "wb"))


def load(path: str):
  return pickle.load(open(path, "rb"))


def infer(model: Doc2Vec, document):
  pass
