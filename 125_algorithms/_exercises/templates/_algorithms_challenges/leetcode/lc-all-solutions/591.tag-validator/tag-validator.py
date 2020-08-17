______ string


class Solution(object
  ___ isValid(self, code
    """
    :type code: str
    :rtype: bool
    """

    ___ getTokenStartsAt(start
      ___ i in range(start, le.(code)):
        __ code[i] __ ">":
          break
      r_ code[start:i + 1]

    ___ isTagsMatched(left, right
      r_ le.(left) + 1 __ le.(right) and left[1:] __ right[2:]

    ___ isClosedTag(tag
      r_ tag[1] __ "/"

    ___ isCDATATag(i
      r_ code.startswith("<![CDATA[", i)

    ___ isTag(tag
      __ le.(tag) < 3:
        r_ False
      __ tag[-1] != ">":
        r_ False

      tag = tag[1:-1]
      __ tag[0] __ "/":
        tag = tag[1:]
      __ not 1 <= le.(tag) <= 9:
        r_ False
      ___ c in tag:
        __ c not in string.ascii_uppercase:
          r_ False
      r_ True

    __ code[0] != "<":
      r_ False
    tagLen = 0
    stack = []
    i = 0
    w___ i < le.(code
      __ code[i] __ "<":
        __ isCDATATag(i
          __ not stack:
            r_ False
          w___ i < le.(code) - 7 and not code.startswith("]]>", i
            i += 1
          __ code.startswith("]]>", i
            i += 3
            continue
          ____
            r_ False
        ____
          token = getTokenStartsAt(i)
          __ not isTag(token
            r_ False
          __ not isClosedTag(token
            stack.append(token)
          ____
            __ not stack:
              r_ False
            __ isTagsMatched(stack[-1], token
              stack.p..
              __ not stack and i + le.(token) < le.(code
                r_ False
            ____
              r_ False
          i += le.(token)
      ____
        i += 1
    r_ not stack
