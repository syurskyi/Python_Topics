c_ Solution(o..
  ___ searchMatrix  matrix, target
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    __ l..(matrix) __ 0 o. l..(matrix[0]) __ 0:
      r.. F..

    m = l..(matrix)
    n = l..(matrix[0])

    start, end = 0, m * n - 1
    w.... start + 1 < end:
      mid = start + (end - start) / 2
      __ matrix[mid / n][mid % n] > target:
        end = mid
      ____ matrix[mid / n][mid % n] < target:
        start = mid
      ____
        r.. T..
    __ matrix[start / n][start % n] __ target:
      r.. T..
    __ matrix[end / n][end % n] __ target:
      r.. T..
    r.. F..
