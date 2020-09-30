class Solution(object
  ___ combinationSum3(self, k, n
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """

    ___ dfs(k, start, path, subsum, res, visited
      __ le.(path) __ k and subsum __ 0:
        res.append(path +   # list)
        r_
      __ le.(path) >= k or subsum <= 0:
        r_

      ___ i __ range(start, 10
        __ visited[i] __ 0:
          visited[i] = 1
          path.append(i)
          dfs(k, i + 1, path, subsum - i, res, visited)
          visited[i] = 0
          path.p..

    visited = [0] * 10
    res =   # list
    dfs(k, 1,   # list, n, res, visited)
    r_ res
