c_ Solution(o..
  ___ subsetsWithDup  nums
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    ___ dfs(start, nums, p.., res, visited
      res.a..(p.. + [])

      ___ i __ r..(start, l..(nums:
        __ start !_ i a.. nums[i] __ nums[i - 1]:
          _____
        __ i n.. __ visited:
          visited[i] 1
          p...a..(nums[i])
          dfs(i + 1, nums, p.., res, visited)
          p...p.. )
          del visited[i]

    nums.s..()
    res    # list
    visited    # dict
    dfs(0, nums, [], res, visited)
    r.. res
