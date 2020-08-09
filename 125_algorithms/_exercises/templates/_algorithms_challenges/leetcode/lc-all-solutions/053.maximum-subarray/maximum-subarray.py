class Solution(object
  ___ maxSubArray(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ le.(nums) __ 0:
      r_ 0
    preSum = maxSum = nums[0]
    for i in range(1, le.(nums)):
      preSum = max(preSum + nums[i], nums[i])
      maxSum = max(maxSum, preSum)
    r_ maxSum
