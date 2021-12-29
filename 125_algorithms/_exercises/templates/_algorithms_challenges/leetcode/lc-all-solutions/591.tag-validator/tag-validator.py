import string


class Solution(object):
  ___ isValid(self, code):
    """
    :type code: str
    :rtype: bool
    """

    ___ getTokenStartsAt(start):
      for i in range(start, len(code)):
        __ code[i] == ">":
          break
      return code[start:i + 1]

    ___ isTagsMatched(left, right):
      return len(left) + 1 == len(right) and left[1:] == right[2:]

    ___ isClosedTag(tag):
      return tag[1] == "/"

    ___ isCDATATag(i):
      return code.startswith("<![CDATA[", i)

    ___ isTag(tag):
      __ len(tag) < 3:
        return False
      __ tag[-1] != ">":
        return False

      tag = tag[1:-1]
      __ tag[0] == "/":
        tag = tag[1:]
      __ not 1 <= len(tag) <= 9:
        return False
      for c in tag:
        __ c not in string.ascii_uppercase:
          return False
      return True

    __ code[0] != "<":
      return False
    tagLen = 0
    stack = []
    i = 0
    while i < len(code):
      __ code[i] == "<":
        __ isCDATATag(i):
          __ not stack:
            return False
          while i < len(code) - 7 and not code.startswith("]]>", i):
            i += 1
          __ code.startswith("]]>", i):
            i += 3
            continue
          else:
            return False
        else:
          token = getTokenStartsAt(i)
          __ not isTag(token):
            return False
          __ not isClosedTag(token):
            stack.append(token)
          else:
            __ not stack:
              return False
            __ isTagsMatched(stack[-1], token):
              stack.pop()
              __ not stack and i + len(token) < len(code):
                return False
            else:
              return False
          i += len(token)
      else:
        i += 1
    return not stack
