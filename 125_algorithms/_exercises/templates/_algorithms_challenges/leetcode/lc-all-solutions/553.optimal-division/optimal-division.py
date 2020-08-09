class Solution(object
  ___ optimalDivision(self, nums
    """
    :type nums: List[int]
    :rtype: str
    """
    __ le.(nums) < 3:
      r_ "/".join(map(str, nums))
    r_ "%s/(%s)" % (nums[0], "/".join(map(str, nums[1:])))
