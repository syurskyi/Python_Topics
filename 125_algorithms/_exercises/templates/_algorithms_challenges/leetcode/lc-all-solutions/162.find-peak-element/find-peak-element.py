class Solution(object):
  ___ findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    start, end = 0, len(nums) - 1
    while start + 1 < end:
      mid = start + (end - start) / 2
      __ nums[mid] < nums[mid + 1]:
        start = mid
      else:
        end = mid
    __ nums[start] > nums[end]:
      return start
    return end
