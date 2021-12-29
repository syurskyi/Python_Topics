class Solution(object):
  ___ rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ len(nums) == 0 or nums is None:
      return 0
    __ len(nums) <= 2:
      return max(nums[:])
    # If we rob the first house, the problem becomes how to rob houses except the last one.
    # If we rob the last house, the problem becomes how to rob houses ecept the first one.
    return max(self.robHelper(nums[1:]), self.robHelper(nums[:len(nums) - 1]))

  ___ robHelper(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pp = nums[0]
    p = max(pp, nums[1])
    for i in range(2, len(nums)):
      tmp = p
      p = max(pp + nums[i], p)
      pp = tmp
    return p
