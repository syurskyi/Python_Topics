class Solution(object
  ___ searchMatrix(self, matrix, target
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    ___ binarySearch(nums, target
      start, end = 0, le.(nums) - 1
      w___ start + 1 < end:
        mid = start + (end - start) / 2
        __ nums[mid] > target:
          end = mid
        ____ nums[mid] < target:
          start = mid
        ____
          r_ True
      __ nums[start] __ target:
        r_ True
      __ nums[end] __ target:
        r_ True
      r_ False

    for nums in matrix:
      __ binarySearch(nums, target
        r_ True
    r_ False
