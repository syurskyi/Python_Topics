c_ Solution(o..
  ___ findDuplicates  nums
    ans    # list
    ___ i __ r..(0, l..(nums:
      w.... nums[nums[i] - 1] != nums[i]:
        tmp  nums[nums[i] - 1]
        nums[nums[i] - 1] = nums[i]
        nums[i] = tmp
    ___ i __ r..(0, l..(nums:
      __ i + 1 != nums[i]:
        ans.a..(nums[i])
    r.. ans
