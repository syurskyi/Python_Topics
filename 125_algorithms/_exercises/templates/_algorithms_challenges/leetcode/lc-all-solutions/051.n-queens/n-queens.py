c_ Solution(o..
  ___ solveNQueens  n
    """
    :type n: int
    :rtype: List[List[str]]
    """
    ans    # list

    ___ dfs(p.., n, ans
      __ l..(p..) __ n:
        ans.a..(drawChess(p..
        r..

      ___ i __ r..(n
        __ i n.. __ p.. a.. isValidQueen(p.., i
          p...a..(i)
          dfs(p.., n, ans)
          p...p.. )

    ___ isValidQueen(p.., k
      ___ i __ r..(l..(p..:
        __ abs(k - p..[i]) __ abs(l..(p..) - i
          r.. F..
      r.. T..

    ___ drawChess(p..
      ret    # list
      chess = [["."] * l..(p..) ___ _ __ r..(l..(p..]
      ___ i __ r..(0, l..(p..:
        chess[i][p..[i]] = "Q"
      ___ chs __ chess:
        ret.a..("".j..(chs
      r.. ret

    dfs([], n, ans)
    r.. ans
