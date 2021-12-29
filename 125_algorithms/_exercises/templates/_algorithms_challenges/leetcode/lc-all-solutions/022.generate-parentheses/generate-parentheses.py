class Solution(object):
  ___ generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """

    ___ dfs(left, path, res, n):
      __ len(path) == 2 * n:
        __ left == 0:
          res.append("".join(path))
        return

      __ left < n:
        path.append("(")
        dfs(left + 1, path, res, n)
        path.pop()
      __ left > 0:
        path.append(")")
        dfs(left - 1, path, res, n)
        path.pop()

    res = []
    dfs(0, [], res, n)
    return res
