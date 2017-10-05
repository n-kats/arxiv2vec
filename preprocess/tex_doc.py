from typing import List


class NoUpdateState:
  def update_list(self, line: str, tokens: List[str]):
    pass


class NoUpdateCloseState:
  def close(self, n: int):
    return NoUpdateState()


class SafelyCloseState:
  head: int
  def close(self, n: int):
    return EndOfWordState(head=self.head, tail=n-1)


class UnsafelyCloseState:
  def close(self, n: int):
    return SyntaxErrorState()


class WaitNewTokenState(NoUpdateState, NoUpdateCloseState):
  def read(self, i, c):
    if c == ' ':
      return self
    if c == '$':
      return HeadOfTeXState(head=i)
    return InPlainState(head=i)


class InPlainState(NoUpdateState, SafelyCloseState):
  def __init__(self, head):
    self.head = head
    super(InPlainState, self).__init__()

  def read(self, i, c):
    if c == ' ':
      return EndOfWordState(head=self.head, tail=i - 1)
    if c == '$':
      return BorderOfPlainToTeXState(plain_head=self.head, plain_tail=i - 1)
    return self


class HeadOfTeXState(NoUpdateState, UnsafelyCloseState):
  def __init__(self, head):
    self.head = head
    super(HeadOfTeXState, self).__init__()

  def read(self, i, c):
    if c == '$':
      return InDoubleTeXState(head=self.head)
    return InTeXState(head=self.head)


class InTeXState(NoUpdateState, UnsafelyCloseState):
  def __init__(self, head):
    self.head = head
    super(InTeXState, self).__init__()

  def read(self, i, c):
    if c == '$':
      return EndOfWordState(head=self.head, tail=i)
    return self


class EndOfWordState(NoUpdateCloseState):
  def __init__(self, head, tail):
    self.head = head
    self.tail = tail
    super(EndOfWordState, self).__init__()

  def read(self, i, c):
    if c == ' ':
      return WaitNewTokenState()
    if c == '$':
      return HeadOfTeXState(head=i)
    return InPlainState(head=i)

  def update_list(self, line: str, tokens: List[str]):
    tokens.append(line[self.head: self.tail + 1])


class BorderOfPlainToTeXState(UnsafelyCloseState):
  def __init__(self, plain_head, plain_tail):
    self.plain_head = plain_head
    self.plain_tail = plain_tail
    super(BorderOfPlainToTeXState, self).__init__()

  def read(self, i, c):
    if c == '$':
      return InDoubleTeXState(head=i - 1)
    return InTeXState(head=i - 1)

  def update_list(self, line: str, tokens: List[str]):
    tokens.append(line[self.plain_head: self.plain_tail + 1])


class InDoubleTeXState(NoUpdateState, UnsafelyCloseState):
  def __init__(self, head):
    self.head = head
    super(InDoubleTeXState, self).__init__()

  def read(self, i, c):
    if c == '$':
      return EndingDoubleTeXState(head=self.head)
    return self


class EndingDoubleTeXState(NoUpdateState, UnsafelyCloseState):
  def __init__(self, head):
    self.head = head
    super(EndingDoubleTeXState, self).__init__()

  def read(self, i, c):
    if c == '$':
      return EndOfWordState(head=self.head, tail=i)
    return SyntaxErrorState()


class SyntaxErrorState(NoUpdateState, UnsafelyCloseState):
  def read(self, i, c):
    return self


def split_tex_doc(line):
  tokens = []
  state = WaitNewTokenState()
  rstripped = line.rstrip()
  for i, c in enumerate(rstripped):
    state = state.read(i, c)
    state.update_list(line, tokens)
  state = state.close(len(rstripped))
  state.update_list(line, tokens)
  return tokens
