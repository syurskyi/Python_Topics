class Solution(object
  ___ numSquares(self, n
    """
    :type n: int
    :rtype: int
    """
    squares =   # list
    j = 1
    w___ j * j <= n:
      squares.append(j * j)
      j += 1
    level = 0
    queue = [n]
    visited = [False] * (n + 1)
    w___ queue:
      level += 1
      temp =   # list
      ___ q __ queue:
        ___ factor __ squares:
          __ q - factor __ 0:
            r_ level
          __ q - factor < 0:
            break
          __ visited[q - factor]:
            continue
          temp.append(q - factor)
          visited[q - factor] = True
      queue = temp
    r_ level
