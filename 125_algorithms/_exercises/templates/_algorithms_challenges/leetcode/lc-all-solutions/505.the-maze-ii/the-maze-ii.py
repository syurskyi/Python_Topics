c_ Solution(o..
  ___ shortestDistance  maze, ball, hole
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: int
    """

    ___ next(curr, maze
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
        y.. (i, j), dist

    heap = [(0, t..(ball))]
    visited = s..()
    hole = t..(hole)
    w.... heap:
      dist, curr = heapq.heappop(heap)
      __ curr __ visited:
        _____
      visited |= {curr}
      __ curr __ hole:
        r.. dist
      ___ pos, incDist __ next(curr, maze
        heapq.heappush(heap, (dist + incDist, pos))

    r.. -1
