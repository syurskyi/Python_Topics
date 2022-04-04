c_ Solution(o..
  ___ canPartition  nums
    """
    :type nums: List[int]
    :rtype: bool
    """
    s = s..(nums)
    __ s __ 0:
      r.. T..
    __ s % 2 __ 0:
      s, current = s / 2, 0
      ___ num __ nums:
        current |= ((current o. 1) << num) % (1 << (s + 1
        __ current >= 1 << s:
          r.. T..
    r.. F..
