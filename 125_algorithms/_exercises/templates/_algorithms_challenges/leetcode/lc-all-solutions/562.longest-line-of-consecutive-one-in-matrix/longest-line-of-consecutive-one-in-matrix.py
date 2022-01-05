c_ Solution(object):
  ___ longestLine  M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    __ n.. M:
      r.. 0
    hor = [[0] * (l..(M[0]) + 2) ___ _ __ r..(l..(M) + 1)]
    ver = [[0] * (l..(M[0]) + 2) ___ _ __ r..(l..(M) + 1)]
    diag = [[0] * (l..(M[0]) + 2) ___ _ __ r..(l..(M) + 1)]
    anti = [[0] * (l..(M[0]) + 2) ___ _ __ r..(l..(M) + 1)]
    ans = 0
    ___ i __ r..(l..(M)):
      ___ j __ r..(l..(M[0])):
        __ M[i][j] __ 1:
          hor[i + 1][j + 1] = hor[i + 1][j] + 1
          ver[i + 1][j + 1] = ver[i][j + 1] + 1
          diag[i + 1][j + 1] = diag[i][j] + 1
          anti[i + 1][j + 1] = anti[i][j + 2] + 1
          ans = m..(ans, hor[i + 1][j + 1], ver[i + 1][j + 1], diag[i + 1][j + 1], anti[i + 1][j + 1])
    r.. ans
