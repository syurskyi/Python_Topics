class Solution(object
  ___ searchMatrix(self, matrix, target
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    __ le.(matrix) __ 0 or le.(matrix[0]) __ 0:
      r_ False

    m = le.(matrix)
    n = le.(matrix[0])

    start, end = 0, m * n - 1
    w___ start + 1 < end:
      mid = start + (end - start) / 2
      __ matrix[mid / n][mid % n] > target:
        end = mid
      ____ matrix[mid / n][mid % n] < target:
        start = mid
      ____
        r_ True
    __ matrix[start / n][start % n] __ target:
      r_ True
    __ matrix[end / n][end % n] __ target:
      r_ True
    r_ False
