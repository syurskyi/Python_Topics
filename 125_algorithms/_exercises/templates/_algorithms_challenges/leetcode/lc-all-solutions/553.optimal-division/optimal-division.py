class Solution(object):
  ___ optimalDivision(self, nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    __ l..(nums) < 3:
      r.. "/".join(map(str, nums))
    r.. "%s/(%s)" % (nums[0], "/".join(map(str, nums[1:])))
