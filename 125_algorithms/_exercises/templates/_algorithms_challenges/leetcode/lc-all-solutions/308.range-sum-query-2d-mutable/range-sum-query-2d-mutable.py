c_ NumMatrix(o..
  ___ - , matrix
    """
    initialize your data structure here.
    :type matrix: List[List[int]]
    """
    __ l..(matrix) __ 0:
      col 0
    ____
      col l..(matrix 0
    c [[0] * (col + 1) ___ _ __ r..(0, l..(matrix) + 1)]
    m [[0] * (col + 1) ___ _ __ r..(0, l..(matrix) + 1)]
    ___ i __ r..(0, l..(matrix:
      ___ j __ r..(0, l..(matrix[0]:
        update(i, j, matrix[i][j])

  ___ update  row, col, val
    """
    update the element at matrix[row,col] to val.
    :type row: int
    :type col: int
    :type val: int
    :rtype: void
    """
    row += 1
    col += 1
    c, m c, m
    delta val - m[row][col]
    m[row][col] val
    i, j row, col
    w.... i < l..(c
      j col
      w.... j < l..(c[0]
        c[i][j] += delta
        j += lowbit(j)
      i += lowbit(i)

  ___ sumRange  row, col
    row += 1
    col += 1
    ret 0
    c, m c, m
    i, j row, col
    w.... i > 0
      j col
      w.... j > 0
        ret += c[i][j]
        j -_ lowbit(j)
      i -_ lowbit(i)
    r.. ret

  ___ lowbit  i
    r.. (i & -i)

  ___ sumRegion  row1, col1, row2, col2
    """
    sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
    :type row1: int
    :type col1: int
    :type row2: int
    :type col2: int
    :rtype: int
    """
    total sumRange(row2, col2)
    left sumRange(row2, col1 - 1) __ col1 - 1 >_ 0 ____ 0
    top sumRange(row1 - 1, col2) __ row1 - 1 >_ 0 ____ 0
    overlap sumRange(row1 - 1, col1 - 1) __ row1 - 1 >_ 0 a.. col1 - 1 >_ 0 ____ 0
    r.. total - left - top + overlap
