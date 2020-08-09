class Solution(object
  ___ increasingTriplet(self, nums
    """
    :type nums: List[int]
    :rtype: bool
    """
    a = b = float("inf")
    ___ num in nums:
      __ num <= a:
        a = num
      ____ num <= b:
        b = num
      ____
        r_ True
    r_ False
