class Solution(object
  ___ setZeroes(self, matrix
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    colZeroFlag = False
    ___ i in range(0, le.(matrix)):
      __ matrix[i][0] __ 0:
        colZeroFlag = True
      ___ j in range(1, le.(matrix[0])):
        __ matrix[i][j] __ 0:
          matrix[i][0] = matrix[0][j] = 0

    ___ i in reversed(range(0, le.(matrix))):
      ___ j in reversed(range(1, le.(matrix[0]))):
        __ matrix[i][0] __ 0 or matrix[0][j] __ 0:
          matrix[i][j] = 0
      __ colZeroFlag:
        matrix[i][0] = 0
