class Solution(object):
  ___ twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    ___ i, num __ enumerate(nums):
      __ target - num __ d:
        r.. [d[target - num], i]
      d[num] = i
    # no special case handling because it's assumed that it has only one solution

