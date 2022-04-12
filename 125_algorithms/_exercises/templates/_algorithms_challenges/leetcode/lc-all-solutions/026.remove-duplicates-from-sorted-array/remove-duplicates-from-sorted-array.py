c_ Solution(o..
  ___ removeDuplicates  nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ l..(nums) <_ 1:
      r.. l..(nums)
    slow 0
    ___ i __ r..(1, l..(nums:
      __ nums[i] !_ nums[slow]:
        slow += 1
        nums[slow] nums[i]
    r.. slow + 1
