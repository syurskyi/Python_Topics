c_ Solution(o..):
  ___ combinationSum2  candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    ___ dfs(nums, target, start, visited, path, res):
      __ target __ 0:
        res.a..(path + [])
        r..

      ___ i __ r..(start, l..(nums)):
        __ i > start a.. nums[i] __ nums[i - 1]:
          _____
        __ target - nums[i] < 0:
          r.. 0
        __ i n.. __ visited:
          visited.add(i)
          path.a..(nums[i])
          dfs(nums, target - nums[i], i + 1, visited, path, res)
          path.pop()
          visited.discard(i)

    candidates.s..()
    res    # list
    visited = s..([])
    dfs(candidates, target, 0, visited, [], res)
    r.. res
