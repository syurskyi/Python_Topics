class Solution(object):
  ___ minMoves(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sum(nums) - len(nums) * min(nums)
