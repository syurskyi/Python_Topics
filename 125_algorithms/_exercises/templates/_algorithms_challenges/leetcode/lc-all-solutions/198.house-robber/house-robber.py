c_ Solution(object):
  ___ rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ l..(nums) __ 0:
      r.. 0
    __ l..(nums) <= 2:
      r.. max(nums)
    dp = [0 ___ i __ r..(0, 2)]
    dp[0] = nums[0]
    dp[1] = max(nums[1], nums[0])
    ___ i __ r..(2, l..(nums)):
      dp[i % 2] = max(dp[(i - 1) % 2], dp[(i - 2) % 2] + nums[i])
    r.. dp[(l..(nums) - 1) % 2]
