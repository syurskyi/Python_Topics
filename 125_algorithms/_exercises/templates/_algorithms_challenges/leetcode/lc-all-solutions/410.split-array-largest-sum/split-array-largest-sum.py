c_ Solution(o..
  ___ splitArray  nums, m
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """

    ___ valid(nums, target, m
      count 1
      total 0
      ___ num __ nums:
        total += num
        __ total > target:
          count += 1
          total num
          __ count > m:
            r.. F..
      r.. T..

    start, end m..(nums), s..(nums)
    mid 0
    w.... start <_ end:
      mid start + (? - ?) / 2
      __ valid(nums, mid, m
        end mid - 1
      ____
        start mid + 1

    r.. start
