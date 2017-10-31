from abc import ABCMeta, abstractmethod
from typing import List, Iterator

from gensim.utils import simple_preprocess
from preprocess.tex_doc import split_tex_doc


class AbsPreprocessor(metaclass=ABCMeta):
  @abstractmethod
  def preprocess(self, line: str) -> List[str]:
    pass


class SimplePreprocessor(AbsPreprocessor):
  def __init__(
      self,
      deacc: bool = False,
      min_len: int = 2,
      max_len: int = 15) -> None:
    self._deacc = deacc
    self._min_len = min_len
    self._max_len = max_len

  def preprocess(self, line: str) -> List[str]:
    return simple_preprocess(
        deacc=self._deacc,
        min_len=self._min_len,
        max_len=self._max_len)


class TeXMixedTextPreprocessor(AbsPreprocessor):
  """
  $で囲まれた範囲を一つの単語とみなす
  """
  def __init__(self, ):
    pass

  def _tokenize(self, line: str) -> Iterator[str]:
    return split_tex_doc(line)

  def _fix_token(self, token: str) -> str:
    token = token.lower()
    if token[-1] in ",.":
      token = token[:-1]
    return token

  def _accept(self, token: str) -> bool:
    return True

  def preprocess(self, line: str) -> List[str]:
    tokens = self._tokenize(line)
    tokens = map(self._fix_token, tokens)
    tokens = filter(self._accept, tokens)
    return list(tokens)
