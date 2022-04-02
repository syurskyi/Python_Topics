c_ Solution(o..
  ___ removeElement  nums, val
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    slow = -1
    ___ i __ r..(0, l..(nums)):
      __ nums[i] != val:
        slow += 1
        nums[slow] = nums[i]
    r.. slow + 1
