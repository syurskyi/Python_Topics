c_ Solution(o..
  ___ combinationSum2  candidates, target
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    ___ dfs(nums, target, start, visited, p.., res
      __ target __ 0:
        res.a..(p.. + [])
        r..

      ___ i __ r..(start, l..(nums:
        __ i > start a.. nums[i] __ nums[i - 1]:
          _____
        __ target - nums[i] < 0:
          r.. 0
        __ i n.. __ visited:
          visited.add(i)
          p...a..(nums[i])
          dfs(nums, target - nums[i], i + 1, visited, p.., res)
          p...p.. )
          visited.discard(i)

    candidates.s..()
    res    # list
    visited s..([])
    dfs(candidates, target, 0, visited, [], res)
    r.. res
