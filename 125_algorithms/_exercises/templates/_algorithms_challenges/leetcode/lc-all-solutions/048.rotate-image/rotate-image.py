c_ Solution(object):
  ___ rotate  matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    __ l..(matrix) __ 0:
      r..
    h = l..(matrix)
    w = l..(matrix[0])
    ___ i __ r..(0, h):
      ___ j __ r..(0, w / 2):
        matrix[i][j], matrix[i][w - j - 1] = matrix[i][w - j - 1], matrix[i][j]

    ___ i __ r..(0, h):
      ___ j __ r..(0, w - 1 - i):
        matrix[i][j], matrix[w - 1 - j][h - 1 - i] = matrix[w - 1 - j][h - 1 - i], matrix[i][j]
