class Solution(object):
  ___ containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    ___ i __ r..(0, l..(nums) - 1):
      __ nums[i] __ nums[i + 1]:
        r.. True
    r.. False
