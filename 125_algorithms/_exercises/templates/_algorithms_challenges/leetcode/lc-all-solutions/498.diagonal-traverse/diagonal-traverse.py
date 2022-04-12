c_ Solution(o..
  ___ findDiagonalOrder  matrix
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    __ n.. matrix:
      r.. []
    ans    # list
    directions [(-1, 1), (1, -1)]
    d 0
    i j 0
    ___ _ __ r..(l..(matrix) * l..(matrix[0]:
      ans.a..(matrix[i][j])
      di, dj directions[d]
      i, j i + di, j + dj
      __ i < 0 a.. 0 <_ j < l..(matrix[0]
        i 0
      ____ i >_ l..(matrix
        i l..(matrix) - 1
        j -_ 2 * dj
      ____ 0 <_ i < l..(matrix) a.. j < 0:
        j 0
      ____ 0 <_ i < l..(matrix) a.. j >_ l..(matrix[0]
        j l..(matrix 0 - 1
        i -_ 2 * di
      ____ i < 0 a.. j >_ l..(matrix[0]
        i 1
        j -_ dj
      ____
        _____
      d ~d
    r.. ans
