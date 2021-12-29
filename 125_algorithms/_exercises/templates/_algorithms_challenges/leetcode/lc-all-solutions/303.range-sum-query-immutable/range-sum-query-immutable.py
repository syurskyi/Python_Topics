class NumArray(object):
  ___ __init__(self, nums):
    """
    initialize your data structure here.
    :type nums: List[int]
    """
    self.dp = [0] * (l..(nums) + 1)
    ___ i __ r..(0, l..(nums)):
      self.dp[i + 1] = self.dp[i] + nums[i]

  ___ sumRange(self, i, j):
    """
    sum of elements nums[i..j], inclusive.
    :type i: int
    :type j: int
    :rtype: int
    """
    r.. self.dp[j + 1] - self.dp[i]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
