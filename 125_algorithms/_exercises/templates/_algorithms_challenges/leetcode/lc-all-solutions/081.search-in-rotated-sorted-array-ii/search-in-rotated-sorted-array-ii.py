c_ Solution(o..
  ___ s..  nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    start, end = 0, l..(nums) - 1
    w.... start + 1 < end:
      mid = start + (end - start) / 2
      __ nums[mid] __ target:
        r.. T..
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
      r.. T..
    __ nums[end] __ target:
      r.. T..
    r.. F..
