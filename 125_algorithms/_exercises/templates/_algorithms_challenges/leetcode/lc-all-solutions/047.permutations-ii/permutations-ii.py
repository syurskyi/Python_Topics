class Solution(object):
  ___ permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res    # list
    nums.sort()

    ___ dfs(nums, res, path, visited):
      __ l..(path) __ l..(nums):
        res.a..(path + [])
        r..

      ___ i __ r..(l..(nums)):
        __ i __ visited:
          continue
        __ i > 0 and nums[i] __ nums[i - 1] and i - 1 n.. __ visited:
          continue
        visited |= {i}
        path.a..(nums[i])
        dfs(nums, res, path, visited)
        path.pop()
        visited -= {i}

    dfs(nums, res, [], set())
    r.. res
