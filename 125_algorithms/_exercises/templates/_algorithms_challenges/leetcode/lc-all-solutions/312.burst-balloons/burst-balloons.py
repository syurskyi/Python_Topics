class Solution(object):
  ___ maxCoins(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ len(nums) == 0:
      return 0
    nums = [1] + nums + [1]
    dp = [[-1] * (len(nums) + 2) for _ in range(0, len(nums) + 2)]

    ___ dc(start, end, dp, nums):
      __ dp[start][end] != -1:
        return dp[start][end]
      __ start > end:
        return 0
      for i in range(start, end + 1):
        left = dc(start, i - 1, dp, nums)
        right = dc(i + 1, end, dp, nums)
        dp[start][end] = max(dp[start][end], left + right + nums[start - 1] * nums[i] * nums[end + 1])
      return dp[start][end]

    dc(1, len(nums) - 2, dp, nums)
    return dp[1][len(nums) - 2]
