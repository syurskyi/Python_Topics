c_ Solution(o..):
  ___ permute  nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res    # list
    visited = set([])

    ___ dfs(nums, path, res, visited):
      __ l..(path) __ l..(nums):
        res.a..(path + [])
        r..

      ___ i __ r..(0, l..(nums)):
        # if i > 0 and nums[i - 1] == nums[i]:
        #     continue
        __ i n.. __ visited:
          visited.add(i)
          path.a..(nums[i])
          dfs(nums, path, res, visited)
          path.pop()
          visited.discard(i)

    dfs(nums, [], res, visited)
    r.. res
