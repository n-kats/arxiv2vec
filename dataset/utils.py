import re

NEW_LINE_RGX = re.compile("\n\s*")
HEAD_LINE_RGX = re.compile("^\s*")


def fix_needless_new_line(s: str) -> str:
  return re.sub(HEAD_LINE_RGX, "", re.sub(NEW_LINE_RGX, " ", s))
