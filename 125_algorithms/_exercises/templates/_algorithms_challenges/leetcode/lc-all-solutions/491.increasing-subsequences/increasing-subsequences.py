class Solution(object):
  ___ findSubsequences(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []

    ___ dfs(nums, start, path, ans):
      __ len(path) >= 2:
        ans.append(tuple(path + []))

      for i in range(start, len(nums)):
        __ i != start and nums[i] == nums[i - 1]:
          continue
        __ path and nums[i] < path[-1]:
          continue
        path.append(nums[i])
        dfs(nums, i + 1, path, ans)
        path.pop()

    dfs(nums, 0, [], ans)
    return list(set(ans))
