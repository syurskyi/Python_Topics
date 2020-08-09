class Solution(object
  ___ singleNumber(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(1, le.(nums)):
      nums[0] ^= nums[i]
    r_ nums[0]
