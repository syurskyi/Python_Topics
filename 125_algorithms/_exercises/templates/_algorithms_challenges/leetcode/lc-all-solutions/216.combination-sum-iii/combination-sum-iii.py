c_ Solution(o..
  ___ combinationSum3  k, n
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """

    ___ dfs(k, start, p.., subsum, res, visited
      __ l..(p..) __ k a.. subsum __ 0:
        res.a..(p.. + [])
        r..
      __ l..(p..) >= k o. subsum <= 0:
        r..

      ___ i __ r..(start, 10
        __ visited[i] __ 0:
          visited[i] = 1
          p...a..(i)
          dfs(k, i + 1, p.., subsum - i, res, visited)
          visited[i] = 0
          p...p.. )

    visited = [0] * 10
    res    # list
    dfs(k, 1, [], n, res, visited)
    r.. res
