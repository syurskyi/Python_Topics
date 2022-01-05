c_ Solution(object):
  ___ fourSum  nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.s..()
    res    # list
    ___ i __ r..(0, l..(nums)):
      __ i > 0 a.. nums[i] __ nums[i - 1]:
        _____
      ___ j __ r..(i + 1, l..(nums)):
        __ j > i + 1 a.. nums[j] __ nums[j - 1]:
          _____
        start = j + 1
        end = l..(nums) - 1
        w.... start < end:
          s.. = nums[i] + nums[j] + nums[start] + nums[end]
          __ s.. < target:
            start += 1
          ____ s.. > target:
            end -= 1
          ____:
            res.a..((nums[i], nums[j], nums[start], nums[end]))
            start += 1
            end -= 1
            w.... start < end a.. nums[start] __ nums[start - 1]:
              start += 1
            w.... start < end a.. nums[end] __ nums[end + 1]:
              end -= 1
    r.. res
