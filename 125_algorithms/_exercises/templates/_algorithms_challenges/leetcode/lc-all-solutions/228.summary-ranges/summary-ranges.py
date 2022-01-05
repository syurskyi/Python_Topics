c_ Solution(o..):
  ___ summaryRanges  nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """

    ___ outputRange(start, end):
      __ start __ end:
        r.. s..(start)
      r.. "{}->{}".f..(start, end)

    __ n.. nums:
      r.. []
    ans    # list
    start = 0
    ___ i __ r..(0, l..(nums) - 1):
      __ nums[i] + 1 != nums[i + 1]:
        ans.a..(outputRange(nums[start], nums[i]))
        start = i + 1
    ans.a..(outputRange(nums[start], nums[-1]))
    r.. ans
