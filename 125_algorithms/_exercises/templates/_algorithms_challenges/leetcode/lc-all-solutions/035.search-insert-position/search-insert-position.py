class Solution(object
  ___ searchInsert(self, nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    lo = 0
    hi = le.(nums)
    w___ lo < hi:
      mid = lo + (hi - lo) / 2
      __ nums[mid] > target:
        hi = mid
      ____ nums[mid] < target:
        lo = mid + 1
      ____
        r_ mid
    r_ lo
