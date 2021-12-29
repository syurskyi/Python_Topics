class Solution(object):
  ___ rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ l..(nums) __ 0 o. nums __ N..
      r.. 0
    __ l..(nums) <= 2:
      r.. max(nums[:])
    # If we rob the first house, the problem becomes how to rob houses except the last one.
    # If we rob the last house, the problem becomes how to rob houses ecept the first one.
    r.. max(self.robHelper(nums[1:]), self.robHelper(nums[:l..(nums) - 1]))

  ___ robHelper(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pp = nums[0]
    p = max(pp, nums[1])
    ___ i __ r..(2, l..(nums)):
      tmp = p
      p = max(pp + nums[i], p)
      pp = tmp
    r.. p
