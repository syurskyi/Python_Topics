c_ Solution(o..
  ___ multiply  A, B
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    ret [[0 ___ j __ r..(l..(B[0]] ___ i __ r..(l..(A]

    ___ i, row __ e..(A
      ___ k, a __ e..(row
        __ a:
          ___ j, b __ e..(B[k]
            __ b:
              ret[i][j] += a * b
    r.. ret
