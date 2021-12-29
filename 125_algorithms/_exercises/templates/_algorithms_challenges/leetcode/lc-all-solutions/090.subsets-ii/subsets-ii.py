class Solution(object):
  ___ subsetsWithDup(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    ___ dfs(start, nums, path, res, visited):
      res.append(path + [])

      for i in range(start, len(nums)):
        __ start != i and nums[i] == nums[i - 1]:
          continue
        __ i not in visited:
          visited[i] = 1
          path.append(nums[i])
          dfs(i + 1, nums, path, res, visited)
          path.pop()
          del visited[i]

    nums.sort()
    res = []
    visited = {}
    dfs(0, nums, [], res, visited)
    return res
