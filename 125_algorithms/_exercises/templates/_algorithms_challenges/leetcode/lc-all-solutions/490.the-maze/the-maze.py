from collections ______ deque


class Solution(object
  ___ hasPath(self, maze, start, destination
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: bool
    """

    ___ next(curr, maze
      height = le.(maze)
      width = le.(maze[0])
      directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
      for di, dj in directions:
        dist = 0
        i, j = curr
        w___ 0 <= i + di < height and 0 <= j + dj < width and maze[i + di][j + dj] != 1:
          i += di
          j += dj
          dist += 1
        yield (i, j)

    queue = deque([tuple(start)])
    visited = set()
    destination = tuple(destination)
    w___ queue:
      curr = queue.popleft()
      __ curr in visited:
        continue
      __ curr __ destination:
        r_ True
      visited |= {curr}
      for nbr in next(curr, maze
        queue.append(nbr)
    r_ False
