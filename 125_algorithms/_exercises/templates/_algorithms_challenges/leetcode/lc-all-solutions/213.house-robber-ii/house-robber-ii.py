c_ Solution(o..
  ___ rob  nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ l..(nums) __ 0 o. nums __ N..
      r.. 0
    __ l..(nums) <_ 2:
      r.. m..(nums | )
    # If we rob the first house, the problem becomes how to rob houses except the last one.
    # If we rob the last house, the problem becomes how to rob houses ecept the first one.
    r.. m..(robHelper(nums[1:]), robHelper(nums[:l..(nums) - 1]

  ___ robHelper  nums
    """
    :type nums: List[int]
    :rtype: int
    """
    pp = nums[0]
    p = m..(pp, nums[1])
    ___ i __ r..(2, l..(nums:
      tmp  p
      p = m..(pp + nums[i], p)
      pp = tmp
    r.. p
