class Solution(object
  ___ threeSum(self, nums
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    ___ i in range(0, le.(nums)):
      __ i > 0 and nums[i] __ nums[i - 1]:
        continue
      target = 0 - nums[i]
      start, end = i + 1, le.(nums) - 1
      w___ start < end:
        __ nums[start] + nums[end] > target:
          end -= 1
        ____ nums[start] + nums[end] < target:
          start += 1
        ____
          res.append((nums[i], nums[start], nums[end]))
          end -= 1
          start += 1
          w___ start < end and nums[end] __ nums[end + 1]:
            end -= 1
          w___ start < end and nums[start] __ nums[start - 1]:
            start += 1
    r_ res
