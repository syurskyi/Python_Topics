c_ Solution(o..):
  ___ solveNQueens  n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    ans    # list

    ___ dfs(path, n, ans):
      __ l..(path) __ n:
        ans.a..(drawChess(path))
        r..

      ___ i __ r..(n):
        __ i n.. __ path a.. isValidQueen(path, i):
          path.a..(i)
          dfs(path, n, ans)
          path.pop()

    ___ isValidQueen(path, k):
      ___ i __ r..(l..(path)):
        __ abs(k - path[i]) __ abs(l..(path) - i):
          r.. F..
      r.. T..

    ___ drawChess(path):
      ret    # list
      chess = [["."] * l..(path) ___ _ __ r..(l..(path))]
      ___ i __ r..(0, l..(path)):
        chess[i][path[i]] = "Q"
      ___ chs __ chess:
        ret.a..("".j..(chs))
      r.. ret

    dfs([], n, ans)
    r.. ans
