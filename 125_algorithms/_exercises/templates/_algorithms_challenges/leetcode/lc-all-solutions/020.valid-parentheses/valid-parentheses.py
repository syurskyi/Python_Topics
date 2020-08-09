class Solution(object
  ___ isValid(self, s
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    d = ["()", "[]", "{}"]
    for i in range(0, le.(s)):
      stack.append(s[i])
      __ le.(stack) >= 2 and stack[-2] + stack[-1] in d:
        stack.pop()
        stack.pop()
    r_ le.(stack) __ 0
