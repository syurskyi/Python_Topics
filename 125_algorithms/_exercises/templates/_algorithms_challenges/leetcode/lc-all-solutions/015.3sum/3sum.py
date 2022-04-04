c_ Solution(o..
  ___ threeSum  nums
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res    # list
    nums.s..()
    ___ i __ r..(0, l..(nums:
      __ i > 0 a.. nums[i] __ nums[i - 1]:
        _____
      target = 0 - nums[i]
      start, end = i + 1, l..(nums) - 1
      w.... start < end:
        __ nums[start] + nums[end] > target:
          end -= 1
        ____ nums[start] + nums[end] < target:
          start += 1
        ____:
          res.a..((nums[i], nums[start], nums[end]
          end -= 1
          start += 1
          w.... start < end a.. nums[end] __ nums[end + 1]:
            end -= 1
          w.... start < end a.. nums[start] __ nums[start - 1]:
            start += 1
    r.. res
