c_ Solution(object):
  ___ trapRainWater  heightMap):
    """
    :type heightMap: List[List[int]]
    :rtype: int
    """
    __ n.. heightMap:
      r.. 0
    h = l..(heightMap)
    w = l..(heightMap[0])
    ans = 0
    heap    # list
    visited = set()
    ___ j __ r..(w):
      heapq.heappush(heap, (heightMap[0][j], 0, j))
      heapq.heappush(heap, (heightMap[h - 1][j], h - 1, j))
      visited |= {(0, j), (h - 1, j)}
    ___ i __ r..(h):
      heapq.heappush(heap, (heightMap[i][0], i, 0))
      heapq.heappush(heap, (heightMap[i][w - 1], i, w - 1))
      visited |= {(i, 0), (i, w - 1)}
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    w.... heap:
      height, i, j = heapq.heappop(heap)
      ___ di, dj __ dirs:
        ni, nj = i + di, j + dj
        __ 0 <= ni < h a.. 0 <= nj < w a.. (ni, nj) n.. __ visited:
          ans += m..(0, height - heightMap[ni][nj])
          heapq.heappush(heap, (m..(heightMap[ni][nj], height), ni, nj))
          visited |= {(ni, nj)}
    r.. ans
