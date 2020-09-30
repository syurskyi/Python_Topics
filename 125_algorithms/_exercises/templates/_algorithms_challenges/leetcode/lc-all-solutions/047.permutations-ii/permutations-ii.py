class Solution(object
  ___ permuteUnique(self, nums
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res =   # list
    nums.sort()

    ___ dfs(nums, res, path, visited
      __ le.(path) __ le.(nums
        res.append(path +   # list)
        r_

      ___ i __ range(le.(nums)):
        __ i __ visited:
          continue
        __ i > 0 and nums[i] __ nums[i - 1] and i - 1 not __ visited:
          continue
        visited |= {i}
        path.append(nums[i])
        dfs(nums, res, path, visited)
        path.p..
        visited -= {i}

    dfs(nums, res,   # list, set())
    r_ res
