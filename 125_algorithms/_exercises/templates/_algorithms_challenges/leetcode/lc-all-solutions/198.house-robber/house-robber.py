class Solution(object):
  ___ rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ len(nums) == 0:
      return 0
    __ len(nums) <= 2:
      return max(nums)
    dp = [0 for i in range(0, 2)]
    dp[0] = nums[0]
    dp[1] = max(nums[1], nums[0])
    for i in range(2, len(nums)):
      dp[i % 2] = max(dp[(i - 1) % 2], dp[(i - 2) % 2] + nums[i])
    return dp[(len(nums) - 1) % 2]
