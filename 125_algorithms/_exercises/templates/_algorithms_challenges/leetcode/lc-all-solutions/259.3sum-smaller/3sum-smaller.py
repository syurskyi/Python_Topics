c_ Solution(o..
  ___ threeSumSmaller  nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    ans = 0
    nums.s..()
    ___ i __ r..(0, l..(nums:
      start, end = i + 1, l..(nums) - 1
      w.... start < end:
        __ nums[i] + nums[start] + nums[end] < target:
          ans += end - start
          start += 1
        ____:
          end -= 1

    r.. ans
