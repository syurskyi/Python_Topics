directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


c_ Solution(object):
  ___ longestIncreasingPath(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """

    ___ dfs(matrix, i, j, visited, cache):
      __ (i, j) __ visited:
        r.. visited[(i, j)]

      ret = 0
      ___ di, dj __ directions:
        p, q = i + di, j + dj
        __ p < 0 o. q < 0 o. p >= l..(matrix) o. q >= l..(matrix[0]):
          _____
        __ (p, q) n.. __ cache a.. matrix[p][q] > matrix[i][j]:
          cache.add((p, q))
          r = dfs(matrix, p, q, visited, cache)
          ret = max(ret, r)
          cache.discard((p, q))

      visited[(i, j)] = ret + 1
      r.. ret + 1

    visited    # dict
    cache = set()
    ans = 0
    ___ i __ r..(0, l..(matrix)):
      ___ j __ r..(0, l..(matrix[0])):
        cache.add((i, j))
        ans = max(ans, dfs(matrix, i, j, visited, cache))
        cache.discard((i, j))
    r.. ans
