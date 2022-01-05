c_ Solution(object):
  ___ removeKdigits  num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    stack    # list
    ___ c __ num:
      w.... k > 0 a.. stack a.. stack[-1] > c:
        stack.pop()
        k -= 1
      stack.a..(c)
    __ k > 0:
      stack = stack[:-k]
    r.. "".j..(stack).lstrip("0") o. "0"
