class NumMatrix(object):
  ___ __init__(self, matrix):
    """
    initialize your data structure here.
    :type matrix: List[List[int]]
    """
    __ l..(matrix) __ 0:
      col = 0
    ____:
      col = l..(matrix[0])
    self.c = [[0] * (col + 1) ___ _ __ r..(0, l..(matrix) + 1)]
    self.m = [[0] * (col + 1) ___ _ __ r..(0, l..(matrix) + 1)]
    ___ i __ r..(0, l..(matrix)):
      ___ j __ r..(0, l..(matrix[0])):
        self.update(i, j, matrix[i][j])

  ___ update(self, row, col, val):
    """
    update the element at matrix[row,col] to val.
    :type row: int
    :type col: int
    :type val: int
    :rtype: void
    """
    row += 1
    col += 1
    c, m = self.c, self.m
    delta = val - m[row][col]
    m[row][col] = val
    i, j = row, col
    while i < l..(c):
      j = col
      while j < l..(c[0]):
        c[i][j] += delta
        j += self.lowbit(j)
      i += self.lowbit(i)

  ___ sumRange(self, row, col):
    row += 1
    col += 1
    ret = 0
    c, m = self.c, self.m
    i, j = row, col
    while i > 0:
      j = col
      while j > 0:
        ret += c[i][j]
        j -= self.lowbit(j)
      i -= self.lowbit(i)
    r.. ret

  ___ lowbit(self, i):
    r.. (i & -i)

  ___ sumRegion(self, row1, col1, row2, col2):
    """
    sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
    :type row1: int
    :type col1: int
    :type row2: int
    :type col2: int
    :rtype: int
    """
    total = self.sumRange(row2, col2)
    left = self.sumRange(row2, col1 - 1) __ col1 - 1 >= 0 ____ 0
    top = self.sumRange(row1 - 1, col2) __ row1 - 1 >= 0 ____ 0
    overlap = self.sumRange(row1 - 1, col1 - 1) __ row1 - 1 >= 0 and col1 - 1 >= 0 ____ 0
    r.. total - left - top + overlap
