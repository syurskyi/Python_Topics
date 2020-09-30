class Solution(object
  ___ removeKdigits(self, num, k
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    stack =   # list
    ___ c __ num:
      w___ k > 0 and stack and stack[-1] > c:
        stack.p..
        k -= 1
      stack.append(c)
    __ k > 0:
      stack = stack[:-k]
    r_ "".join(stack).lstrip("0") or "0"
