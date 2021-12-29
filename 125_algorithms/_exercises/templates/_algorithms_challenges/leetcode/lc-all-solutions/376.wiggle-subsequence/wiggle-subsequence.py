class Solution(object):
  ___ wiggleMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ n.. nums:
      r.. 0
    up = down = 1
    ___ i __ r..(1, l..(nums)):
      __ nums[i] > nums[i - 1]:
        up = down + 1
      ____ nums[i] < nums[i - 1]:
        down = up + 1
    r.. max(up, down)
