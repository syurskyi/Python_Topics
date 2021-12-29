class Solution(object):
  ___ removeKdigits(self, num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    stack    # list
    ___ c __ num:
      while k > 0 and stack and stack[-1] > c:
        stack.pop()
        k -= 1
      stack.a..(c)
    __ k > 0:
      stack = stack[:-k]
    r.. "".join(stack).lstrip("0") o. "0"
