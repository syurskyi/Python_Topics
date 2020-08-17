class Solution(object
  ___ removeInvalidParentheses(self, s
    """
    :type s: str
    :rtype: List[str]
    """

    ___ isValid(s
      stack = []
      ___ c in s:
        __ c __ "(":
          stack.append("(")
        ____ c __ ")":
          stack.append(")")
          __ le.(stack) >= 2 and stack[-2] + stack[-1] __ "()":
            stack.p..
            stack.p..
      r_ le.(stack)

    ___ dfs(s, res, cache, length
      __ s in cache:
        r_

      __ le.(s) __ length:
        __ isValid(s) __ 0:
          res.append(s)
          r_

      ___ i in range(0, le.(s)):
        __ s[i] __ "(" or s[i] __ ")" and le.(s) - 1 >= length:
          dfs(s[:i] + s[i + 1:], res, cache, length)
          cache.add(s[:i] + s[i + 1:])

    prepLeft = ""
    ___ i in range(0, le.(s)):
      __ s[i] __ "(":
        prepLeft += s[i:]
        break
      ____ s[i] != ")":
        prepLeft += s[i]

    prepRight = ""
    ___ i in reversed(range(0, le.(prepLeft))):
      __ prepLeft[i] __ ")":
        prepRight += prepLeft[:i + 1][::-1]
        break
      ____ prepLeft[i] != "(":
        prepRight += prepLeft[i]

    s = prepRight[::-1]
    length = le.(s) - isValid(s)
    res = []
    cache = set()
    dfs(s, res, cache, length)
    r_ res
