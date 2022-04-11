c_ Solution(o..
  ___ searchInsert  nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    lo 0
    hi l..(nums)
    w.... lo < hi:
      mid lo + (hi - lo) / 2
      __ nums[mid] > target:
        hi mid
      ____ nums[mid] < target:
        lo mid + 1
      ____
        r.. mid
    r.. lo
