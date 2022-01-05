c_ Solution(object):
  ___ combinationSum3  k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """

    ___ dfs(k, start, path, subsum, res, visited):
      __ l..(path) __ k a.. subsum __ 0:
        res.a..(path + [])
        r..
      __ l..(path) >= k o. subsum <= 0:
        r..

      ___ i __ r..(start, 10):
        __ visited[i] __ 0:
          visited[i] = 1
          path.a..(i)
          dfs(k, i + 1, path, subsum - i, res, visited)
          visited[i] = 0
          path.pop()

    visited = [0] * 10
    res    # list
    dfs(k, 1, [], n, res, visited)
    r.. res
