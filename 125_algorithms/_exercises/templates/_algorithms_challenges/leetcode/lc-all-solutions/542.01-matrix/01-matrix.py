from collections ______ deque


class Solution(object
  ___ updateMatrix(self, matrix
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    queue = deque([])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    ___ i in range(le.(matrix)):
      ___ j in range(le.(matrix[0])):
        __ matrix[i][j] __ 0:
          queue.append((i, j))
        __ matrix[i][j] __ 1:
          matrix[i][j] = -1

    w___ queue:
      i, j = queue.popleft()
      ___ di, dj in directions:
        ni, nj = i + di, j + dj
        __ 0 <= ni < le.(matrix) and 0 <= nj < le.(matrix[0]) and matrix[ni][nj] __ -1:
          matrix[ni][nj] = matrix[i][j] + 1
          queue.append((ni, nj))
    r_ matrix
