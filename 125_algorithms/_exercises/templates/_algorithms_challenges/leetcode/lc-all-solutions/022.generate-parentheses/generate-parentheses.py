c_ Solution(o..):
  ___ generateParenthesis  n):
    """
    :type n: int
    :rtype: List[str]
    """

    ___ dfs(left, path, res, n):
      __ l..(path) __ 2 * n:
        __ left __ 0:
          res.a..("".j..(path))
        r..

      __ left < n:
        path.a..("(")
        dfs(left + 1, path, res, n)
        path.pop()
      __ left > 0:
        path.a..(")")
        dfs(left - 1, path, res, n)
        path.pop()

    res    # list
    dfs(0, [], res, n)
    r.. res
