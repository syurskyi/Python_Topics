class Solution(object
  ___ findMin(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = nums[0]
    start, end = 0, le.(nums) - 1
    w___ start + 1 < end:
      mid = start + (end - start) / 2
      __ nums[start] < nums[mid]:
        start = mid
      ____ nums[start] > nums[mid]:
        end = mid
      ____
        start += 1
        ans = min(ans, nums[start])

    r_ min(ans, nums[start], nums[end])
