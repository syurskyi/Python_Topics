c_ Solution(o..
  ___ threeSumClosest  nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.s..()
    ans = 0
    diff = f__("inf")
    ___ i __ r..(0, l..(nums:
      start, end = i + 1, l..(nums) - 1
      w.... start < end:
        s.. = nums[i] + nums[start] + nums[end]
        __ s.. > target:
          __ abs(target - s..) < diff:
            diff = abs(target - s..)
            ans = s..
          end -= 1
        ____:
          __ abs(target - s..) < diff:
            diff = abs(target - s..)
            ans = s..
          start += 1
    r.. ans
