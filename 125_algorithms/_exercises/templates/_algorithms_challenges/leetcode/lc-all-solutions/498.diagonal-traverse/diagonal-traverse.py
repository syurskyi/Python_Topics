class Solution(object):
  ___ findDiagonalOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    __ n.. matrix:
      r.. []
    ans    # list
    directions = [(-1, 1), (1, -1)]
    d = 0
    i = j = 0
    ___ _ __ r..(l..(matrix) * l..(matrix[0])):
      ans.a..(matrix[i][j])
      di, dj = directions[d]
      i, j = i + di, j + dj
      __ i < 0 and 0 <= j < l..(matrix[0]):
        i = 0
      ____ i >= l..(matrix):
        i = l..(matrix) - 1
        j -= 2 * dj
      ____ 0 <= i < l..(matrix) and j < 0:
        j = 0
      ____ 0 <= i < l..(matrix) and j >= l..(matrix[0]):
        j = l..(matrix[0]) - 1
        i -= 2 * di
      ____ i < 0 and j >= l..(matrix[0]):
        i = 1
        j -= dj
      ____:
        continue
      d = ~d
    r.. ans
