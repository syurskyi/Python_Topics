____ collections _______ deque


class Solution(object):
  ___ updateMatrix(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    queue = deque([])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    ___ i __ r..(l..(matrix)):
      ___ j __ r..(l..(matrix[0])):
        __ matrix[i][j] __ 0:
          queue.a..((i, j))
        __ matrix[i][j] __ 1:
          matrix[i][j] = -1

    w.... queue:
      i, j = queue.popleft()
      ___ di, dj __ directions:
        ni, nj = i + di, j + dj
        __ 0 <= ni < l..(matrix) a.. 0 <= nj < l..(matrix[0]) a.. matrix[ni][nj] __ -1:
          matrix[ni][nj] = matrix[i][j] + 1
          queue.a..((ni, nj))
    r.. matrix
