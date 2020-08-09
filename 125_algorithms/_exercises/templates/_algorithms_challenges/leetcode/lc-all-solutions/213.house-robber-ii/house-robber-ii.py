class Solution(object
  ___ rob(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ le.(nums) __ 0 or nums is None:
      r_ 0
    __ le.(nums) <= 2:
      r_ max(nums[:])
    # If we rob the first house, the problem becomes how to rob houses except the last one.
    # If we rob the last house, the problem becomes how to rob houses ecept the first one.
    r_ max(self.robHelper(nums[1:]), self.robHelper(nums[:le.(nums) - 1]))

  ___ robHelper(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    pp = nums[0]
    p = max(pp, nums[1])
    ___ i in range(2, le.(nums)):
      tmp = p
      p = max(pp + nums[i], p)
      pp = tmp
    r_ p
