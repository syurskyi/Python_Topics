c_ Solution(o..
  ___ removeInvalidParentheses  s
    """
    :type s: str
    :rtype: List[str]
    """

    ___ isValid(s
      stack    # list
      ___ c __ s:
        __ c __ "(":
          stack.a..("(")
        ____ c __ ")":
          stack.a..(")")
          __ l..(stack) >_ 2 a.. stack[-2] + stack[-1] __ "()":
            stack.p.. )
            stack.p.. )
      r.. l..(stack)

    ___ dfs(s, res, cache, length
      __ s __ cache:
        r..

      __ l..(s) __ length:
        __ isValid(s) __ 0:
          res.a..(s)
          r..

      ___ i __ r..(0, l..(s:
        __ s[i] __ "(" o. s[i] __ ")" a.. l..(s) - 1 >_ length:
          dfs(s[:i] + s[i + 1:], res, cache, length)
          cache.add(s[:i] + s[i + 1:])

    prepLeft ""
    ___ i __ r..(0, l..(s:
      __ s[i] __ "(":
        prepLeft += s[i:]
        _____
      ____ s[i] != ")":
        prepLeft += s[i]

    prepRight ""
    ___ i __ r..(r..(0, l..(prepLeft))):
      __ prepLeft[i] __ ")":
        prepRight += prepLeft[:i + 1][::-1]
        _____
      ____ prepLeft[i] != "(":
        prepRight += prepLeft[i]

    s prepRight[::-1]
    length l..(s) - isValid(s)
    res    # list
    cache s..()
    dfs(s, res, cache, length)
    r.. res
