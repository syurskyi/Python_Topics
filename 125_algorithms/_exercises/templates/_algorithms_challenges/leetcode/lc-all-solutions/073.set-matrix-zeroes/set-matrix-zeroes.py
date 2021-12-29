class Solution(object):
  ___ setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    colZeroFlag = False
    ___ i __ r..(0, l..(matrix)):
      __ matrix[i][0] __ 0:
        colZeroFlag = True
      ___ j __ r..(1, l..(matrix[0])):
        __ matrix[i][j] __ 0:
          matrix[i][0] = matrix[0][j] = 0

    ___ i __ reversed(r..(0, l..(matrix))):
      ___ j __ reversed(r..(1, l..(matrix[0]))):
        __ matrix[i][0] __ 0 o. matrix[0][j] __ 0:
          matrix[i][j] = 0
      __ colZeroFlag:
        matrix[i][0] = 0
