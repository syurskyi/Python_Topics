class Solution(object
  ___ rotate(self, matrix
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    __ le.(matrix) __ 0:
      r_
    h = le.(matrix)
    w = le.(matrix[0])
    ___ i in range(0, h
      ___ j in range(0, w / 2
        matrix[i][j], matrix[i][w - j - 1] = matrix[i][w - j - 1], matrix[i][j]

    ___ i in range(0, h
      ___ j in range(0, w - 1 - i
        matrix[i][j], matrix[w - 1 - j][h - 1 - i] = matrix[w - 1 - j][h - 1 - i], matrix[i][j]
