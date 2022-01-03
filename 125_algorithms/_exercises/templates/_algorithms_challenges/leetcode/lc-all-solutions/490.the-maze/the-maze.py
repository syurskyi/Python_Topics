____ collections _______ deque


c_ Solution(object):
  ___ hasPath(self, maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: bool
    """

    ___ next(curr, maze):
      height = l..(maze)
      width = l..(maze[0])
      directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
      ___ di, dj __ directions:
        dist = 0
        i, j = curr
        w.... 0 <= i + di < height a.. 0 <= j + dj < width a.. maze[i + di][j + dj] != 1:
          i += di
          j += dj
          dist += 1
        y.. (i, j)

    queue = deque([tuple(start)])
    visited = set()
    destination = tuple(destination)
    w.... queue:
      curr = queue.popleft()
      __ curr __ visited:
        continue
      __ curr __ destination:
        r.. T..
      visited |= {curr}
      ___ nbr __ next(curr, maze):
        queue.a..(nbr)
    r.. F..
