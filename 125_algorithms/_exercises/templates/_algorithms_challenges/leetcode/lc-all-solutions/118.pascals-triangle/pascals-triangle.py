c_ Solution(object):
  ___ generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    ans = [[1] * n ___ n __ r..(1, numRows + 1)]
    ___ i __ r..(1, numRows + 1):
      ___ j __ r..(0, i - 2):
        ans[i - 1][1 + j] = ans[i - 2][j] + ans[i - 2][j + 1]
    r.. ans
