c_ Solution(o..
  ___ checkPossibility  nums
    """
    :type nums: List[int]
    :rtype: bool
    """
    flag = F..
    pre = f__("-inf")
    ___ i __ r..(l..(nums) - 1
      __ nums[i] < pre:
        __ nums[i + 1] >= nums[i - 1]:
          nums[i] = nums[i + 1]
        ____
          nums[i - 1] = nums[i]
        flag = T..
        _____
      pre = nums[i]
    __ n.. flag a.. l..(nums) > 1 a.. nums[-1] < nums[-2]:
      nums[-1] = nums[-2]
    pre = f__("-inf")
    ___ num __ nums:
      __ num < pre:
        r.. F..
      pre = num
    r.. T..
