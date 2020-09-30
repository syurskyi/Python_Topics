class Solution(object
  ___ decodeString(self, s
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
        stack.append(["", int(num)])
        num = ""
      ____ c __ "]":
        ss, k = stack.p..
        stack[-1][0] += ss * k
      ____
        stack[-1][0] += c
    r_ stack[-1][0]
