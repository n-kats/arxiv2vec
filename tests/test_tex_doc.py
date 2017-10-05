"""
test_tex_doc
"""

import unittest

from preprocess.tex_doc import split_tex_doc


class TeXDocTest(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_something(self):
    print(split_tex_doc("$M$ is an $n$-manifold."))
    print(split_tex_doc("$$M$$ is an $n$-manifold."))
    print(split_tex_doc("2$$M$$ is not an $n$-manifold."))
    print(split_tex_doc("2$M$ is not an $n$-manifold."))
    print(split_tex_doc("2 $M$ is not an $n$-manifold."))
    print(split_tex_doc("2 $$M$$ is not an $n$-manifold."))
    print(split_tex_doc("2 $$M$ is not an $n$-manifold."))

if __name__ == '__main__':
  unittest.main()
