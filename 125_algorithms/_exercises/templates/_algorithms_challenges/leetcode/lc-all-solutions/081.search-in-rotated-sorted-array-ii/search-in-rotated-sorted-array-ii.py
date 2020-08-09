class Solution(object
  ___ search(self, nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    start, end = 0, le.(nums) - 1
    w___ start + 1 < end:
      mid = start + (end - start) / 2
      __ nums[mid] __ target:
        r_ True
      __ nums[start] < nums[mid]:
        __ nums[start] <= target <= nums[mid]:
          end = mid
        ____
          start = mid
      ____ nums[start] > nums[mid]:
        __ nums[mid] <= target <= nums[end]:
          start = mid
        ____
          end = mid
      ____
        start += 1

    __ nums[start] __ target:
      r_ True
    __ nums[end] __ target:
      r_ True
    r_ False
