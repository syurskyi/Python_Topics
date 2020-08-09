class Solution(object
  ___ canPartition(self, nums
    """
    :type nums: List[int]
    :rtype: bool
    """
    s = sum(nums)
    __ s __ 0:
      r_ True
    __ s % 2 __ 0:
      s, current = s / 2, 0
      for num in nums:
        current |= ((current or 1) << num) % (1 << (s + 1))
        __ current >= 1 << s:
          r_ True
    r_ False
