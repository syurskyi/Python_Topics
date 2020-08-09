class Solution(object
  ___ generate(self, numRows
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    ans = [[1] * n ___ n in range(1, numRows + 1)]
    ___ i in range(1, numRows + 1
      ___ j in range(0, i - 2
        ans[i - 1][1 + j] = ans[i - 2][j] + ans[i - 2][j + 1]
    r_ ans
