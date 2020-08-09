class Solution(object
  ___ findPeakElement(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    start, end = 0, le.(nums) - 1
    w___ start + 1 < end:
      mid = start + (end - start) / 2
      __ nums[mid] < nums[mid + 1]:
        start = mid
      ____
        end = mid
    __ nums[start] > nums[end]:
      r_ start
    r_ end
