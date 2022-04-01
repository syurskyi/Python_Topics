c_ Solution(o..):
  ___ permuteUnique  nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res    # list
    nums.s..()

    ___ dfs(nums, res, path, visited):
      __ l..(path) __ l..(nums):
        res.a..(path + [])
        r..

      ___ i __ r..(l..(nums)):
        __ i __ visited:
          _____
        __ i > 0 a.. nums[i] __ nums[i - 1] a.. i - 1 n.. __ visited:
          _____
        visited |= {i}
        path.a..(nums[i])
        dfs(nums, res, path, visited)
        path.pop()
        visited -= {i}

    dfs(nums, res, [], s..())
    r.. res
