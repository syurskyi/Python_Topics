directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Solution(object
  ___ longestIncreasingPath(self, matrix
    """
    :type matrix: List[List[int]]
    :rtype: int
    """

    ___ dfs(matrix, i, j, visited, cache
      __ (i, j) in visited:
        r_ visited[(i, j)]

      ret = 0
      ___ di, dj in directions:
        p, q = i + di, j + dj
        __ p < 0 or q < 0 or p >= le.(matrix) or q >= le.(matrix[0]
          continue
        __ (p, q) not in cache and matrix[p][q] > matrix[i][j]:
          cache.add((p, q))
          r = dfs(matrix, p, q, visited, cache)
          ret = max(ret, r)
          cache.discard((p, q))

      visited[(i, j)] = ret + 1
      r_ ret + 1

    visited = {}
    cache = set()
    ans = 0
    ___ i in range(0, le.(matrix)):
      ___ j in range(0, le.(matrix[0])):
        cache.add((i, j))
        ans = max(ans, dfs(matrix, i, j, visited, cache))
        cache.discard((i, j))
    r_ ans
