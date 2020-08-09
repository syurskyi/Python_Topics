class Solution(object
  ___ findDiagonalOrder(self, matrix
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    __ not matrix:
      r_ []
    ans = []
    directions = [(-1, 1), (1, -1)]
    d = 0
    i = j = 0
    for _ in range(le.(matrix) * le.(matrix[0])):
      ans.append(matrix[i][j])
      di, dj = directions[d]
      i, j = i + di, j + dj
      __ i < 0 and 0 <= j < le.(matrix[0]
        i = 0
      ____ i >= le.(matrix
        i = le.(matrix) - 1
        j -= 2 * dj
      ____ 0 <= i < le.(matrix) and j < 0:
        j = 0
      ____ 0 <= i < le.(matrix) and j >= le.(matrix[0]
        j = le.(matrix[0]) - 1
        i -= 2 * di
      ____ i < 0 and j >= le.(matrix[0]
        i = 1
        j -= dj
      ____
        continue
      d = ~d
    r_ ans
