class Solution(object
  ___ singleNumber(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    ___ i __ range(1, le.(nums)):
      nums[0] ^= nums[i]
    r_ nums[0]
