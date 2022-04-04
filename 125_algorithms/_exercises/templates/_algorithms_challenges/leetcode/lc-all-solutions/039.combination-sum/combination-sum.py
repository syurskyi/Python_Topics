c_ Solution(o..
  ___ combinationSum  candidates, target
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    ___ dfs(candidates, start, target, p.., res
      __ target __ 0:
        r.. res.a..(p.. + [])

      ___ i __ r..(start, l..(candidates:
        __ target - candidates[i] >= 0:
          p...a..(candidates[i])
          dfs(candidates, i, target - candidates[i], p.., res)
          p...p.. )

    res    # list
    dfs(candidates, 0, target, [], res)
    r.. res
