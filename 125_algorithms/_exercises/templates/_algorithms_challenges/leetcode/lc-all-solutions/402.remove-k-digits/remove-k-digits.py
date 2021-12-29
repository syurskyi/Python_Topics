class Solution(object):
  ___ removeKdigits(self, num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    stack = []
    for c in num:
      while k > 0 and stack and stack[-1] > c:
        stack.pop()
        k -= 1
      stack.append(c)
    __ k > 0:
      stack = stack[:-k]
    return "".join(stack).lstrip("0") or "0"
