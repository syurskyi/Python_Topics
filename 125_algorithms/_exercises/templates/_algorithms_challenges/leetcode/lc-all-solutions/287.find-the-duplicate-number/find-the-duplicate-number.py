c_ Solution(o..
  ___ findDuplicate  nums
    """
    :type nums: List[int]
    :rtype: int
    """
    n = l..(nums) - 1
    start, end = 1, n
    w.... start + 1 < end:
      mid = start + (end - start) / 2
      count = 0
      ___ num __ nums:
        __ num < mid:
          count += 1
      __ count >= mid:
        end = mid
      ____
        start = mid
    __ nums.c.. start) > nums.c.. end
      r.. start
    r.. end
