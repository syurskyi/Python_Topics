class Solution(object):
  ___ totalNQueens(self, n):
    """
    :type n: int
    :rtype: int
    """

    ___ dfs(path, n):
      __ len(path) == n:
        return 1
      res = 0
      for i in range(n):
        __ i not in path and isValidQueen(path, i):
          path.append(i)
          res += dfs(path, n)
          path.pop()
      return res

    ___ isValidQueen(path, k):
      for i in range(len(path)):
        __ abs(k - path[i]) == abs(len(path) - i):
          return False
      return True

    return dfs([], n)
