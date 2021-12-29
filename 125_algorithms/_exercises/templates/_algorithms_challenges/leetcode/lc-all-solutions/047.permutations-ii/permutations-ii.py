class Solution(object):
  ___ permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()

    ___ dfs(nums, res, path, visited):
      __ len(path) == len(nums):
        res.append(path + [])
        return

      for i in range(len(nums)):
        __ i in visited:
          continue
        __ i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited:
          continue
        visited |= {i}
        path.append(nums[i])
        dfs(nums, res, path, visited)
        path.pop()
        visited -= {i}

    dfs(nums, res, [], set())
    return res
