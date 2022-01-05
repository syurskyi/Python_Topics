c_ Solution(o..):
  ___ combinationSum  candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    ___ dfs(candidates, start, target, path, res):
      __ target __ 0:
        r.. res.a..(path + [])

      ___ i __ r..(start, l..(candidates)):
        __ target - candidates[i] >= 0:
          path.a..(candidates[i])
          dfs(candidates, i, target - candidates[i], path, res)
          path.pop()

    res    # list
    dfs(candidates, 0, target, [], res)
    r.. res
