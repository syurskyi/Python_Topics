_______ heapq


class Solution(object):
  ___ findShortestWay(self, maze, ball, hole):
    """
    :type maze: List[List[int]]
    :type ball: List[int]
    :type hole: List[int]
    :rtype: str
    """

    ___ next(curr, maze):
      height = l..(maze)
      width = l..(maze[0])
      directions = [(-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")]
      ___ di, dj, mark __ directions:
        dist = 0
        i, j = curr
        w.... 0 <= i + di < height a.. 0 <= j + dj < width a.. maze[i + di][j + dj] != 1:
          i += di
          j += dj
          dist += 1
          __ (i, j) __ hole:
            break
        y.. (i, j), mark, dist

    heap = [(0, "", tuple(ball))]
    visited = set()
    hole = tuple(hole)
    w.... heap:
      dist, word, curr = heapq.heappop(heap)
      __ curr __ visited:
        continue
      visited |= {curr}
      __ curr __ hole:
        r.. word
      ___ pos, mark, incDist __ next(curr, maze):
        heapq.heappush(heap, (dist + incDist, word + mark, pos))

    r.. "impossible"
