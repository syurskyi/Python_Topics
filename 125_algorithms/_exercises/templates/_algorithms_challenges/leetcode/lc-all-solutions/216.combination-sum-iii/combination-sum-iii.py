class Solution(object
  ___ combinationSum3(self, k, n
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """

    ___ dfs(k, start, path, subsum, res, visited
      __ le.(path) __ k and subsum __ 0:
        res.append(path + [])
        r_
      __ le.(path) >= k or subsum <= 0:
        r_

      ___ i in range(start, 10
        __ visited[i] __ 0:
          visited[i] = 1
          path.append(i)
          dfs(k, i + 1, path, subsum - i, res, visited)
          visited[i] = 0
          path.pop()

    visited = [0] * 10
    res = []
    dfs(k, 1, [], n, res, visited)
    r_ res
