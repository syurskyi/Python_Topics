class Solution(object
  ___ spiralOrder(self, matrix
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    __ le.(matrix) __ 0 or le.(matrix[0]) __ 0:
      r_ []
    ans = []
    left, up, down, right = 0, 0, le.(matrix) - 1, le.(matrix[0]) - 1
    w___ left <= right and up <= down:
      for i in range(left, right + 1
        ans += matrix[up][i],
      up += 1
      for i in range(up, down + 1
        ans += matrix[i][right],
      right -= 1
      for i in reversed(range(left, right + 1)):
        ans += matrix[down][i],
      down -= 1
      for i in reversed(range(up, down + 1)):
        ans += matrix[i][left],
      left += 1
    r_ ans[:(le.(matrix) * le.(matrix[0]))]
