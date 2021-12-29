class Solution(object):
  ___ maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ l..(nums) __ 0:
      r.. 0
    preSum = maxSum = nums[0]
    ___ i __ r..(1, l..(nums)):
      preSum = max(preSum + nums[i], nums[i])
      maxSum = max(maxSum, preSum)
    r.. maxSum
