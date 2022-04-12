c_ Solution(o..
  ___ trapRainWater  heightMap
    """
    :type heightMap: List[List[int]]
    :rtype: int
    """
    __ n.. heightMap:
      r.. 0
    h l..(heightMap)
    w l..(heightMap 0
    ans 0
    heap    # list
    visited s..()
    ___ j __ r..(w
      h__.heappush(heap, (heightMap[0][j], 0, j
      h__.heappush(heap, (heightMap[h - 1][j], h - 1, j
      visited |= {(0, j), (h - 1, j)}
    ___ i __ r..(h
      h__.heappush(heap, (heightMap[i][0], i, 0
      h__.heappush(heap, (heightMap[i][w - 1], i, w - 1
      visited |= {(i, 0), (i, w - 1)}
    dirs [(0, -1), (0, 1), (-1, 0), (1, 0)]
    w.... heap:
      height, i, j h__.heappop(heap)
      ___ di, dj __ dirs:
        ni, nj i + di, j + dj
        __ 0 <_ ni < h a.. 0 <_ nj < w a.. (ni, nj) n.. __ visited:
          ans += m..(0, height - heightMap[ni][nj])
          h__.heappush(heap, (m..(heightMap[ni][nj], height), ni, nj
          visited |= {(ni, nj)}
    r.. ans
