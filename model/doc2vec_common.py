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
    model = Doc2Vec(size=50)
    model.build_vocab(train_corpus)
    model.train(train_corpus, total_examples=model.corpus_count, epochs=500)
    self._model = model

  def save(self, path: str):
    # ディレクトリ作成
    pickle.dump(self, open(path, "wb"))

  def infer_vector(self, text: str):
    input_ = self._preprocessor.preprocess(text)
    return self._model.infer_vector(input_, steps=50)

  def find_neighbors(self, vec):
    return self._model.docvecs.most_similar([vec])


def load(path: str):
  return pickle.load(open(path, "rb"))


def infer(model: Doc2Vec, document):
  pass
