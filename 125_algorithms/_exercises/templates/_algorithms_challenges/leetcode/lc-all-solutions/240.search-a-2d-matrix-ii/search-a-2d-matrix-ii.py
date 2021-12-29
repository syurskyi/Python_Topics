class Solution(object):
  ___ searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    ___ binarySearch(nums, target):
      start, end = 0, l..(nums) - 1
      w.... start + 1 < end:
        mid = start + (end - start) / 2
        __ nums[mid] > target:
          end = mid
        ____ nums[mid] < target:
          start = mid
        ____:
          r.. True
      __ nums[start] __ target:
        r.. True
      __ nums[end] __ target:
        r.. True
      r.. False

    ___ nums __ matrix:
      __ binarySearch(nums, target):
        r.. True
    r.. False
