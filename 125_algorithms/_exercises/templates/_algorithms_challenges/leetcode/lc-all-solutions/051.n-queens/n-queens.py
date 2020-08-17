class Solution(object
  ___ solveNQueens(self, n
    """
    :type n: int
    :rtype: List[List[str]]
    """
    ans = []

    ___ dfs(path, n, ans
      __ le.(path) __ n:
        ans.append(drawChess(path))
        r_

      ___ i in range(n
        __ i not in path and isValidQueen(path, i
          path.append(i)
          dfs(path, n, ans)
          path.p..

    ___ isValidQueen(path, k
      ___ i in range(le.(path)):
        __ abs(k - path[i]) __ abs(le.(path) - i
          r_ False
      r_ True

    ___ drawChess(path
      ret = []
      chess = [["."] * le.(path) ___ _ in range(le.(path))]
      ___ i in range(0, le.(path)):
        chess[i][path[i]] = "Q"
      ___ chs in chess:
        ret.append("".join(chs))
      r_ ret

    dfs([], n, ans)
    r_ ans
