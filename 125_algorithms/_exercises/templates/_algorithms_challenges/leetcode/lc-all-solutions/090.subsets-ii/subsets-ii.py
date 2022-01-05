c_ Solution(o..):
  ___ subsetsWithDup  nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    ___ dfs(start, nums, path, res, visited):
      res.a..(path + [])

      ___ i __ r..(start, l..(nums)):
        __ start != i a.. nums[i] __ nums[i - 1]:
          _____
        __ i n.. __ visited:
          visited[i] = 1
          path.a..(nums[i])
          dfs(i + 1, nums, path, res, visited)
          path.pop()
          del visited[i]

    nums.s..()
    res    # list
    visited    # dict
    dfs(0, nums, [], res, visited)
    r.. res
