c_ Solution(o..
  ___ generateParenthesis  n
    """
    :type n: int
    :rtype: List[str]
    """

    ___ dfs(left, p.., res, n
      __ l..(p..) __ 2 * n:
        __ left __ 0:
          res.a..("".j..(p..
        r..

      __ left < n:
        p...a..("(")
        dfs(left + 1, p.., res, n)
        p...p.. )
      __ left > 0
        p...a..(")")
        dfs(left - 1, p.., res, n)
        p...p.. )

    res    # list
    dfs(0, [], res, n)
    r.. res
