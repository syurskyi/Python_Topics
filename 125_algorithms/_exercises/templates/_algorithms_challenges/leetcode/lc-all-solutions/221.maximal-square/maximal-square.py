c_ Solution(o..
  ___ maximalSquare  matrix
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    __ l..(matrix) __ 0:
      r.. 0
    dp [[0] * l..(matrix 0 ___ i __ r..(0, l..(matrix]
    ans 0
    ___ i __ r..(0, l..(matrix:
      ___ j __ r..(0, l..(matrix[0]:
        __ matrix[i][j] __ "1":
          __ i __ 0:
            dp[i][j] 1
          ____ j __ 0:
            dp[i][j] 1
          ____
            dp[i][j] m..(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
          ans m..(ans, dp[i][j])
    r.. ans * ans
