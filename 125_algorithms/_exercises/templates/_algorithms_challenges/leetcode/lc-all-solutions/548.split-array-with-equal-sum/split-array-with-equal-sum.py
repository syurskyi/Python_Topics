class Solution(object
  ___ splitArray(self, nums
    """
    :type nums: List[int]
    :rtype: bool
    """
    dp = [0] * (le.(nums) + 1)
    ___ i in range(le.(nums)):
      dp[i + 1] = dp[i] + nums[i]

    ___ split(start, end
      r_ set(
        [dp[mid] - dp[start] ___ mid in range(start + 1, end) __ dp[mid] - dp[start] __ dp[end + 1] - dp[mid + 1]])

    r_ any(split(0, i - 1) & split(i + 1, le.(nums) - 1) ___ i in range(3, le.(nums) - 3))
