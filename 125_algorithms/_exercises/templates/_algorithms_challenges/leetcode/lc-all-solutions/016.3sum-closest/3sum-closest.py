class Solution(object):
  ___ threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    ans = 0
    diff = float("inf")
    ___ i __ r..(0, l..(nums)):
      start, end = i + 1, l..(nums) - 1
      while start < end:
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
