_______ string


class Solution(object):
  ___ isValid(self, code):
    """
    :type code: str
    :rtype: bool
    """

    ___ getTokenStartsAt(start):
      ___ i __ r..(start, l..(code)):
        __ code[i] __ ">":
          break
      r.. code[start:i + 1]

    ___ isTagsMatched(left, right):
      r.. l..(left) + 1 __ l..(right) and left[1:] __ right[2:]

    ___ isClosedTag(tag):
      r.. tag[1] __ "/"

    ___ isCDATATag(i):
      r.. code.startswith("<![CDATA[", i)

    ___ isTag(tag):
      __ l..(tag) < 3:
        r.. False
      __ tag[-1] != ">":
        r.. False

      tag = tag[1:-1]
      __ tag[0] __ "/":
        tag = tag[1:]
      __ n.. 1 <= l..(tag) <= 9:
        r.. False
      ___ c __ tag:
        __ c n.. __ string.ascii_uppercase:
          r.. False
      r.. True

    __ code[0] != "<":
      r.. False
    tagLen = 0
    stack    # list
    i = 0
    while i < l..(code):
      __ code[i] __ "<":
        __ isCDATATag(i):
          __ n.. stack:
            r.. False
          while i < l..(code) - 7 and n.. code.startswith("]]>", i):
            i += 1
          __ code.startswith("]]>", i):
            i += 3
            continue
          ____:
            r.. False
        ____:
          token = getTokenStartsAt(i)
          __ n.. isTag(token):
            r.. False
          __ n.. isClosedTag(token):
            stack.a..(token)
          ____:
            __ n.. stack:
              r.. False
            __ isTagsMatched(stack[-1], token):
              stack.pop()
              __ n.. stack and i + l..(token) < l..(code):
                r.. False
            ____:
              r.. False
          i += l..(token)
      ____:
        i += 1
    r.. n.. stack
