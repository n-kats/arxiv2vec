from typing import List, NamedTuple
from typing import Union


class TaggedDocument(NamedTuple):
  words: List[str]
  tags: List[Union[int, str]]
