_______ s__


c_ Solution(object):
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
      r.. l..(left) + 1 __ l..(right) a.. left[1:] __ right[2:]

    ___ isClosedTag(tag):
      r.. tag[1] __ "/"

    ___ isCDATATag(i):
      r.. code.startswith("<![CDATA[", i)

    ___ isTag(tag):
      __ l..(tag) < 3:
        r.. F..
      __ tag[-1] != ">":
        r.. F..

      tag = tag[1:-1]
      __ tag[0] __ "/":
        tag = tag[1:]
      __ n.. 1 <= l..(tag) <= 9:
        r.. F..
      ___ c __ tag:
        __ c n.. __ s__.a..:
          r.. F..
      r.. T..

    __ code[0] != "<":
      r.. F..
    tagLen = 0
    stack    # list
    i = 0
    w.... i < l..(code):
      __ code[i] __ "<":
        __ isCDATATag(i):
          __ n.. stack:
            r.. F..
          w.... i < l..(code) - 7 a.. n.. code.startswith("]]>", i):
            i += 1
          __ code.startswith("]]>", i):
            i += 3
            continue
          ____:
            r.. F..
        ____:
          token = getTokenStartsAt(i)
          __ n.. isTag(token):
            r.. F..
          __ n.. isClosedTag(token):
            stack.a..(token)
          ____:
            __ n.. stack:
              r.. F..
            __ isTagsMatched(stack[-1], token):
              stack.pop()
              __ n.. stack a.. i + l..(token) < l..(code):
                r.. F..
            ____:
              r.. F..
          i += l..(token)
      ____:
        i += 1
    r.. n.. stack
