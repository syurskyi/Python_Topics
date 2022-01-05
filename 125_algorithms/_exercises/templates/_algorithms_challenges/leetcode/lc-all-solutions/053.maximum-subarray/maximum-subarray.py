c_ Solution(object):
  ___ maxSubArray  nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ l..(nums) __ 0:
      r.. 0
    preSum = maxSum = nums[0]
    ___ i __ r..(1, l..(nums)):
      preSum = m..(preSum + nums[i], nums[i])
      maxSum = m..(maxSum, preSum)
    r.. maxSum
