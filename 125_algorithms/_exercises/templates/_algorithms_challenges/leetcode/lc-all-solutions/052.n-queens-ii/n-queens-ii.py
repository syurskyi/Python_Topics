c_ Solution(o..
  ___ totalNQueens  n
    """
    :type n: int
    :rtype: int
    """

    ___ dfs(p.., n
      __ l..(p..) __ n:
        r.. 1
      res 0
      ___ i __ r..(n
        __ i n.. __ p.. a.. isValidQueen(p.., i
          p...a..(i)
          res += dfs(p.., n)
          p...p.. )
      r.. res

    ___ isValidQueen(p.., k
      ___ i __ r..(l..(p..:
        __ a..(k - p..[i]) __ a..(l..(p..) - i
          r.. F..
      r.. T..

    r.. dfs([], n)
