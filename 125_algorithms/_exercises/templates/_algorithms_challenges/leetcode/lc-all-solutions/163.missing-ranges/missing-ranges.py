c_ Solution(o..
  ___ findMissingRanges  nums, lower, upper
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: List[str]
    """
    ans    # list
    nums [lower - 1] + nums + [upper + 1]
    ___ i __ r..(0, l..(nums) - 1
      __ nums[i] + 2 __ nums[i + 1]:
        ans.a..(s..(nums[i] + 1
      __ nums[i + 1] > nums[i] + 2:
        ans.a..(s..(nums[i] + 1) + "->" + s..(nums[i + 1] - 1
    r.. ans
