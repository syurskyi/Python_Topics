c_ Solution(o..
  ___ removeDuplicates  nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ l..(nums) <= 2:
      r.. l..(nums)
    cnt = 0
    j = 1
    ___ i __ r..(1, l..(nums)):
      __ nums[i] __ nums[i - 1]:
        cnt += 1
        __ cnt < 2:
          nums[j] = nums[i]
          j += 1
      ____:
        nums[j] = nums[i]
        j += 1
        cnt = 0
    r.. j
