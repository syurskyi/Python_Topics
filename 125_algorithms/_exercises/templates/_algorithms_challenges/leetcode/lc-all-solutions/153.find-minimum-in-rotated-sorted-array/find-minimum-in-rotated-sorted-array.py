c_ Solution(o..
  ___ findMin  nums
    """
    :type nums: List[int]
    :rtype: int
    """
    start, end, mid = 0, l..(nums) - 1, 0
    w.... start + 1 < end:
      mid = start + (end - start) / 2
      __ nums[start] <= nums[mid]:
        start = mid
      ____
        end = mid
    r.. m..(nums[0], nums[start], nums[end])
