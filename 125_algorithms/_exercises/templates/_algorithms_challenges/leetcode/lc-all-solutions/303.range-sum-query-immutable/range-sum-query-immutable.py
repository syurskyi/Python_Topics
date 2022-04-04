c_ NumArray(o..
  ___ - , nums
    """
    initialize your data structure here.
    :type nums: List[int]
    """
    dp = [0] * (l..(nums) + 1)
    ___ i __ r..(0, l..(nums:
      dp[i + 1] = dp[i] + nums[i]

  ___ sumRange  i, j
    """
    sum of elements nums[i..j], inclusive.
    :type i: int
    :type j: int
    :rtype: int
    """
    r.. dp[j + 1] - dp[i]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
