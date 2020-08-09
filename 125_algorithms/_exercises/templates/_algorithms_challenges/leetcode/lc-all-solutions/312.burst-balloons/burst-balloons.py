class Solution(object
  ___ maxCoins(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ le.(nums) __ 0:
      r_ 0
    nums = [1] + nums + [1]
    dp = [[-1] * (le.(nums) + 2) for _ in range(0, le.(nums) + 2)]

    ___ dc(start, end, dp, nums
      __ dp[start][end] != -1:
        r_ dp[start][end]
      __ start > end:
        r_ 0
      for i in range(start, end + 1
        left = dc(start, i - 1, dp, nums)
        right = dc(i + 1, end, dp, nums)
        dp[start][end] = max(dp[start][end], left + right + nums[start - 1] * nums[i] * nums[end + 1])
      r_ dp[start][end]

    dc(1, le.(nums) - 2, dp, nums)
    r_ dp[1][le.(nums) - 2]
