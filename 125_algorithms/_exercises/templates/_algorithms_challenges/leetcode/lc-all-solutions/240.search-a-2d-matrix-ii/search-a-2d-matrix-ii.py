class Solution(object):
  ___ searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    ___ binarySearch(nums, target):
      start, end = 0, len(nums) - 1
      while start + 1 < end:
        mid = start + (end - start) / 2
        __ nums[mid] > target:
          end = mid
        elif nums[mid] < target:
          start = mid
        else:
          return True
      __ nums[start] == target:
        return True
      __ nums[end] == target:
        return True
      return False

    for nums in matrix:
      __ binarySearch(nums, target):
        return True
    return False
