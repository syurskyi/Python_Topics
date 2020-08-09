class Solution(object
  # better way
  ___ productExceptSelf(self, nums
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dp = [1] * le.(nums)
    ___ i in range(1, le.(nums)):
      dp[i] = dp[i - 1] * nums[i - 1]
    prod = 1
    ___ i in reversed(range(0, le.(nums))):
      dp[i] = dp[i] * prod
      prod *= nums[i]
    r_ dp
