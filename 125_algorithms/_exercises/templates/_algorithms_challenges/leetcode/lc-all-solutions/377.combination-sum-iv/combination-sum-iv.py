class Solution(object
  ___ combinationSum4(self, nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    dp = [0] * (target + 1)
    dp[0] = 1

    ___ i __ range(1, target + 1
      ___ j __ range(1, le.(nums) + 1
        __ i - nums[j - 1] >= 0:
          dp[i] += dp[i - nums[j - 1]]
    r_ dp[-1]
