c_ NumMatrix(o..):
  ___ - , matrix):
    """
    initialize your data structure here.
    :type matrix: List[List[int]]
    """
    dp = [[0] * l..(matrix[0]) ___ i __ r..(0, l..(matrix))]
    ___ i __ r..(0, l..(matrix)):
      ___ j __ r..(0, l..(matrix[0])):
        __ i __ 0:
          dp[0][j] = dp[0][j - 1] + matrix[i][j]
        ____ j __ 0:
          dp[i][0] = dp[i - 1][0] + matrix[i][j]
        ____:
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i][j]

  ___ sumRegion  row1, col1, row2, col2):
    """
    sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
    :type row1: int
    :type col1: int
    :type row2: int
    :type col2: int
    :rtype: int
    """
    dp = dp

    diagSum = dp[row1 - 1][col1 - 1]
    totalSum = dp[row2][col2]
    leftSum = dp[row2][col1 - 1]
    upSum = dp[row1 - 1][col2]
    __ row1 __ 0:
      upSum = 0
      diagSum = 0
    __ col1 __ 0:
      leftSum = 0
      diagSum = 0
    r.. totalSum - leftSum - upSum + diagSum
