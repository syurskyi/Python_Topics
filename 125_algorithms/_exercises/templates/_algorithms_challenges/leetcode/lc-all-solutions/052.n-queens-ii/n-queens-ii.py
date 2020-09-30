class Solution(object
  ___ totalNQueens(self, n
    """
    :type n: int
    :rtype: int
    """

    ___ dfs(path, n
      __ le.(path) __ n:
        r_ 1
      res = 0
      ___ i __ range(n
        __ i not __ path and isValidQueen(path, i
          path.append(i)
          res += dfs(path, n)
          path.p..
      r_ res

    ___ isValidQueen(path, k
      ___ i __ range(le.(path)):
        __ abs(k - path[i]) __ abs(le.(path) - i
          r_ False
      r_ True

    r_ dfs(  # list, n)
