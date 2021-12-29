____ collections _______ deque


class Solution(object):
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
        while 0 <= i + di < height and 0 <= j + dj < width and maze[i + di][j + dj] != 1:
          i += di
          j += dj
          dist += 1
        yield (i, j)

    queue = deque([tuple(start)])
    visited = set()
    destination = tuple(destination)
    while queue:
      curr = queue.popleft()
      __ curr __ visited:
        continue
      __ curr __ destination:
        r.. True
      visited |= {curr}
      ___ nbr __ next(curr, maze):
        queue.a..(nbr)
    r.. False
