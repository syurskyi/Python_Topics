class Solution(object
  ___ wiggleMaxLength(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ not nums:
      r_ 0
    up = down = 1
    ___ i in range(1, le.(nums)):
      __ nums[i] > nums[i - 1]:
        up = down + 1
      ____ nums[i] < nums[i - 1]:
        down = up + 1
    r_ max(up, down)
