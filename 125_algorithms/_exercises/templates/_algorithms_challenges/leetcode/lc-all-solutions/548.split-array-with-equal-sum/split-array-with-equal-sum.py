class Solution(object):
  ___ splitArray(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dp = [0] * (l..(nums) + 1)
    ___ i __ r..(l..(nums)):
      dp[i + 1] = dp[i] + nums[i]

    ___ s..(start, end):
      r.. set(
        [dp[mid] - dp[start] ___ mid __ r..(start + 1, end) __ dp[mid] - dp[start] __ dp[end + 1] - dp[mid + 1]])

    r.. any(s..(0, i - 1) & s..(i + 1, l..(nums) - 1) ___ i __ r..(3, l..(nums) - 3))
