class Solution(object):
  ___ spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    __ l..(matrix) __ 0 o. l..(matrix[0]) __ 0:
      r.. []
    ans    # list
    left, up, down, right = 0, 0, l..(matrix) - 1, l..(matrix[0]) - 1
    w.... left <= right a.. up <= down:
      ___ i __ r..(left, right + 1):
        ans += matrix[up][i],
      up += 1
      ___ i __ r..(up, down + 1):
        ans += matrix[i][right],
      right -= 1
      ___ i __ reversed(r..(left, right + 1)):
        ans += matrix[down][i],
      down -= 1
      ___ i __ reversed(r..(up, down + 1)):
        ans += matrix[i][left],
      left += 1
    r.. ans[:(l..(matrix) * l..(matrix[0]))]
