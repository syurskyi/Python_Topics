c_ Solution(object):
  ___ numberOfArithmeticSlices  nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    __ l..(nums) > 2:
      diff = [nums[i] - nums[i - 1] ___ i __ r..(1, l..(nums))]
      count = 1
      pre = diff[0]
      ___ i __ r..(1, l..(diff)):
        __ diff[i] __ pre:
          count += 1
        ____:
          ans += count * (count - 1) / 2
          count = 1
        pre = diff[i]
      ans += count * (count - 1) / 2
    r.. ans
