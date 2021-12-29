class Solution(object):
  ___ numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    squares = []
    j = 1
    while j * j <= n:
      squares.append(j * j)
      j += 1
    level = 0
    queue = [n]
    visited = [False] * (n + 1)
    while queue:
      level += 1
      temp = []
      for q in queue:
        for factor in squares:
          __ q - factor == 0:
            return level
          __ q - factor < 0:
            break
          __ visited[q - factor]:
            continue
          temp.append(q - factor)
          visited[q - factor] = True
      queue = temp
    return level
