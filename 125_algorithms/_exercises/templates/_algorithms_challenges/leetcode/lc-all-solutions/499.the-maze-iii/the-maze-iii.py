______ heapq


class Solution(object
  ___ findShortestWay(self, maze, ball, hole
    """
    :type maze: List[List[int]]
    :type ball: List[int]
    :type hole: List[int]
    :rtype: str
    """

    ___ next(curr, maze
      height = le.(maze)
      width = le.(maze[0])
      directions = [(-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")]
      ___ di, dj, mark in directions:
        dist = 0
        i, j = curr
        w___ 0 <= i + di < height and 0 <= j + dj < width and maze[i + di][j + dj] != 1:
          i += di
          j += dj
          dist += 1
          __ (i, j) __ hole:
            break
        yield (i, j), mark, dist

    heap = [(0, "", tuple(ball))]
    visited = set()
    hole = tuple(hole)
    w___ heap:
      dist, word, curr = heapq.heappop(heap)
      __ curr in visited:
        continue
      visited |= {curr}
      __ curr __ hole:
        r_ word
      ___ pos, mark, incDist in next(curr, maze
        heapq.heappush(heap, (dist + incDist, word + mark, pos))

    r_ "impossible"
