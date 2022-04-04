c_ Solution(o..
  ___ permute  nums
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res    # list
    visited = s..([])

    ___ dfs(nums, p.., res, visited
      __ l..(p..) __ l..(nums
        res.a..(p.. + [])
        r..

      ___ i __ r..(0, l..(nums:
        # if i > 0 and nums[i - 1] == nums[i]:
        #     continue
        __ i n.. __ visited:
          visited.add(i)
          p...a..(nums[i])
          dfs(nums, p.., res, visited)
          p...pop()
          visited.discard(i)

    dfs(nums, [], res, visited)
    r.. res
