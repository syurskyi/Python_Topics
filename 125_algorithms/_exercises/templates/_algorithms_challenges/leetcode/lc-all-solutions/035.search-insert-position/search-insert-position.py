class Solution(object):
  ___ searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    lo = 0
    hi = len(nums)
    while lo < hi:
      mid = lo + (hi - lo) / 2
      __ nums[mid] > target:
        hi = mid
      elif nums[mid] < target:
        lo = mid + 1
      else:
        return mid
    return lo
