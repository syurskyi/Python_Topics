class Solution(object):
  ___ searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    __ l..(matrix) __ 0 o. l..(matrix[0]) __ 0:
      r.. False

    m = l..(matrix)
    n = l..(matrix[0])

    start, end = 0, m * n - 1
    while start + 1 < end:
      mid = start + (end - start) / 2
      __ matrix[mid / n][mid % n] > target:
        end = mid
      ____ matrix[mid / n][mid % n] < target:
        start = mid
      ____:
        r.. True
    __ matrix[start / n][start % n] __ target:
      r.. True
    __ matrix[end / n][end % n] __ target:
      r.. True
    r.. False
