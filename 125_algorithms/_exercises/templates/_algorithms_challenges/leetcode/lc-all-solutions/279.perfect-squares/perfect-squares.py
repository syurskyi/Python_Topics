class Solution(object):
  ___ numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    squares    # list
    j = 1
    while j * j <= n:
      squares.a..(j * j)
      j += 1
    level = 0
    queue = [n]
    visited = [False] * (n + 1)
    while queue:
      level += 1
      temp    # list
      ___ q __ queue:
        ___ factor __ squares:
          __ q - factor __ 0:
            r.. level
          __ q - factor < 0:
            break
          __ visited[q - factor]:
            continue
          temp.a..(q - factor)
          visited[q - factor] = True
      queue = temp
    r.. level
