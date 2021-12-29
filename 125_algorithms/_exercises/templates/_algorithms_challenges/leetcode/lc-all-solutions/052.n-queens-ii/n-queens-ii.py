class Solution(object):
  ___ totalNQueens(self, n):
    """
    :type n: int
    :rtype: int
    """

    ___ dfs(path, n):
      __ l..(path) __ n:
        r.. 1
      res = 0
      ___ i __ r..(n):
        __ i n.. __ path and isValidQueen(path, i):
          path.a..(i)
          res += dfs(path, n)
          path.pop()
      r.. res

    ___ isValidQueen(path, k):
      ___ i __ r..(l..(path)):
        __ abs(k - path[i]) __ abs(l..(path) - i):
          r.. False
      r.. True

    r.. dfs([], n)
