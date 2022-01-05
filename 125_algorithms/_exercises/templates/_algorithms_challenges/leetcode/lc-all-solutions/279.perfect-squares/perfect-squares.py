c_ Solution(object):
  ___ numSquares  n):
    """
    :type n: int
    :rtype: int
    """
    squares    # list
    j = 1
    w.... j * j <= n:
      squares.a..(j * j)
      j += 1
    level = 0
    queue = [n]
    visited = [F..] * (n + 1)
    w.... queue:
      level += 1
      temp    # list
      ___ q __ queue:
        ___ factor __ squares:
          __ q - factor __ 0:
            r.. level
          __ q - factor < 0:
            break
          __ visited[q - factor]:
            _____
          temp.a..(q - factor)
          visited[q - factor] = T..
      queue = temp
    r.. level
