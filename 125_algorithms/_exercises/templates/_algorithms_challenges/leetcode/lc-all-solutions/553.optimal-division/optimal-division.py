class Solution(object):
  ___ optimalDivision(self, nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    __ len(nums) < 3:
      return "/".join(map(str, nums))
    return "%s/(%s)" % (nums[0], "/".join(map(str, nums[1:])))
