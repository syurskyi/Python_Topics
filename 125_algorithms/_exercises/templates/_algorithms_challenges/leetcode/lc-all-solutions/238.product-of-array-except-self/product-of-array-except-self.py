class Solution(object):
  # better way
  ___ productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dp = [1] * l..(nums)
    ___ i __ r..(1, l..(nums)):
      dp[i] = dp[i - 1] * nums[i - 1]
    prod = 1
    ___ i __ reversed(r..(0, l..(nums))):
      dp[i] = dp[i] * prod
      prod *= nums[i]
    r.. dp
