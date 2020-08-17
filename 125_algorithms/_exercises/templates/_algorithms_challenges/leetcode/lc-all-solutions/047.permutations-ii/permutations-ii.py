class Solution(object
  ___ permuteUnique(self, nums
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()

    ___ dfs(nums, res, path, visited
      __ le.(path) __ le.(nums
        res.append(path + [])
        r_

      ___ i in range(le.(nums)):
        __ i in visited:
          continue
        __ i > 0 and nums[i] __ nums[i - 1] and i - 1 not in visited:
          continue
        visited |= {i}
        path.append(nums[i])
        dfs(nums, res, path, visited)
        path.p..
        visited -= {i}

    dfs(nums, res, [], set())
    r_ res
