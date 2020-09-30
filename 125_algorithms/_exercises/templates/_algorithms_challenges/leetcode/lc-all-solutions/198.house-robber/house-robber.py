class Solution(object
  ___ rob(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ le.(nums) __ 0:
      r_ 0
    __ le.(nums) <= 2:
      r_ ma.(nums)
    dp = [0 ___ i __ range(0, 2)]
    dp[0] = nums[0]
    dp[1] = ma.(nums[1], nums[0])
    ___ i __ range(2, le.(nums)):
      dp[i % 2] = ma.(dp[(i - 1) % 2], dp[(i - 2) % 2] + nums[i])
    r_ dp[(le.(nums) - 1) % 2]
