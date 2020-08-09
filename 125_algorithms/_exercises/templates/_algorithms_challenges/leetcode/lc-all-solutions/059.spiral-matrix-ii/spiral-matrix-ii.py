class Solution(object
  ___ generateMatrix(self, n
    """
    :type n: int
    :rtype: List[List[int]]
    """
    ans = [[0] * n ___ _ in range(n)]
    left, right, up, down = 0, n - 1, 0, n - 1
    k = 1
    w___ left <= right and up <= down:
      ___ i in range(left, right + 1
        ans[up][i] = k
        k += 1
      up += 1
      ___ i in range(up, down + 1
        ans[i][right] = k
        k += 1
      right -= 1
      ___ i in reversed(range(left, right + 1)):
        ans[down][i] = k
        k += 1
      down -= 1
      ___ i in reversed(range(up, down + 1)):
        ans[i][left] = k
        k += 1
      left += 1
    r_ ans
