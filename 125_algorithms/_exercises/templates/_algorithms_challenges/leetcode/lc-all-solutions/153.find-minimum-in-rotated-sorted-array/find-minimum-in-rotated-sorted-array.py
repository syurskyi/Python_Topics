class Solution(object
  ___ findMin(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    start, end, mid = 0, le.(nums) - 1, 0
    w___ start + 1 < end:
      mid = start + (end - start) / 2
      __ nums[start] <= nums[mid]:
        start = mid
      ____
        end = mid
    r_ min(nums[0], nums[start], nums[end])
