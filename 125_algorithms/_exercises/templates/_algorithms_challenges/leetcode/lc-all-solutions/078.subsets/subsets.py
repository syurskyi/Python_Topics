class Solution(object):
  ___ subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    ___ dfs(nums, index, path, ans):
      ans.append(path)
      [dfs(nums, i + 1, path + [nums[i]], ans) for i in range(index, len(nums))]

    ans = []
    dfs(nums, 0, [], ans)
    return ans
