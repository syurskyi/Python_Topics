class Solution(object):
  ___ wiggleMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ not nums:
      return 0
    up = down = 1
    for i in range(1, len(nums)):
      __ nums[i] > nums[i - 1]:
        up = down + 1
      elif nums[i] < nums[i - 1]:
        down = up + 1
    return max(up, down)
