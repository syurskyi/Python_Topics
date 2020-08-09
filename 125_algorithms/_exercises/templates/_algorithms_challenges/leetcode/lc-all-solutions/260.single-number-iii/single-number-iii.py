class Solution(object
  ___ singleNumber(self, nums
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    xor = 0
    ___ num in nums:
      xor ^= num

    xor = xor & -xor
    a, b = 0, 0
    ___ num in nums:
      __ num & xor:
        a ^= num
      ____
        b ^= num

    r_ a, b
