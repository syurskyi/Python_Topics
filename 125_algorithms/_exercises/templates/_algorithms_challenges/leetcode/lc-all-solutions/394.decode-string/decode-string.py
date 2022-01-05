c_ Solution(object):
  ___ decodeString  s):
    """
    :type s: str
    :rtype: str
    """
    num = ""
    stack = [["", 1]]
    ___ c __ s:
      __ c __ "0123456789":
        num += c
      ____ c __ "[":
        stack.a..(["", i..(num)])
        num = ""
      ____ c __ "]":
        ss, k = stack.pop()
        stack[-1][0] += ss * k
      ____:
        stack[-1][0] += c
    r.. stack[-1][0]
