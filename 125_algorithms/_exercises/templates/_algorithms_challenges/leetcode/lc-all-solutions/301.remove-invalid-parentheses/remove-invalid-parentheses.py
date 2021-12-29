class Solution(object):
  ___ removeInvalidParentheses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """

    ___ isValid(s):
      stack = []
      for c in s:
        __ c == "(":
          stack.append("(")
        elif c == ")":
          stack.append(")")
          __ len(stack) >= 2 and stack[-2] + stack[-1] == "()":
            stack.pop()
            stack.pop()
      return len(stack)

    ___ dfs(s, res, cache, length):
      __ s in cache:
        return

      __ len(s) == length:
        __ isValid(s) == 0:
          res.append(s)
          return

      for i in range(0, len(s)):
        __ s[i] == "(" or s[i] == ")" and len(s) - 1 >= length:
          dfs(s[:i] + s[i + 1:], res, cache, length)
          cache.add(s[:i] + s[i + 1:])

    prepLeft = ""
    for i in range(0, len(s)):
      __ s[i] == "(":
        prepLeft += s[i:]
        break
      elif s[i] != ")":
        prepLeft += s[i]

    prepRight = ""
    for i in reversed(range(0, len(prepLeft))):
      __ prepLeft[i] == ")":
        prepRight += prepLeft[:i + 1][::-1]
        break
      elif prepLeft[i] != "(":
        prepRight += prepLeft[i]

    s = prepRight[::-1]
    length = len(s) - isValid(s)
    res = []
    cache = set()
    dfs(s, res, cache, length)
    return res
