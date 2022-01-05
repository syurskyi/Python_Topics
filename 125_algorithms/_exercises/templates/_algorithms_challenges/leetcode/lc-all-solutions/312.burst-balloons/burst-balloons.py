c_ Solution(o..):
  ___ maxCoins  nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ l..(nums) __ 0:
      r.. 0
    nums = [1] + nums + [1]
    dp = [[-1] * (l..(nums) + 2) ___ _ __ r..(0, l..(nums) + 2)]

    ___ dc(start, end, dp, nums):
      __ dp[start][end] != -1:
        r.. dp[start][end]
      __ start > end:
        r.. 0
      ___ i __ r..(start, end + 1):
        left = dc(start, i - 1, dp, nums)
        right = dc(i + 1, end, dp, nums)
        dp[start][end] = m..(dp[start][end], left + right + nums[start - 1] * nums[i] * nums[end + 1])
      r.. dp[start][end]

    dc(1, l..(nums) - 2, dp, nums)
    r.. dp[1][l..(nums) - 2]
