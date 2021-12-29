class Solution(object):
  ___ generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """

    ___ dfs(left, path, res, n):
      __ l..(path) __ 2 * n:
        __ left __ 0:
          res.a..("".join(path))
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
