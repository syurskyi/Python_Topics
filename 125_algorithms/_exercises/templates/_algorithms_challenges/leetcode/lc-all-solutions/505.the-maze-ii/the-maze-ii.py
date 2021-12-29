class Solution(object):
  ___ shortestDistance(self, maze, ball, hole):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: int
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
        yield (i, j), dist

    heap = [(0, tuple(ball))]
    visited = set()
    hole = tuple(hole)
    while heap:
      dist, curr = heapq.heappop(heap)
      __ curr __ visited:
        continue
      visited |= {curr}
      __ curr __ hole:
        r.. dist
      ___ pos, incDist __ next(curr, maze):
        heapq.heappush(heap, (dist + incDist, pos))

    r.. -1
