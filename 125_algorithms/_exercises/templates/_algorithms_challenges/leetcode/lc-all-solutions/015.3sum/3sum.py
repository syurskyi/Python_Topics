class Solution(object):
  ___ threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res    # list
    nums.sort()
    ___ i __ r..(0, l..(nums)):
      __ i > 0 and nums[i] __ nums[i - 1]:
        continue
      target = 0 - nums[i]
      start, end = i + 1, l..(nums) - 1
      while start < end:
        __ nums[start] + nums[end] > target:
          end -= 1
        ____ nums[start] + nums[end] < target:
          start += 1
        ____:
          res.a..((nums[i], nums[start], nums[end]))
          end -= 1
          start += 1
          while start < end and nums[end] __ nums[end + 1]:
            end -= 1
          while start < end and nums[start] __ nums[start - 1]:
            start += 1
    r.. res
