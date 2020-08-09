class Solution(object
  ___ fourSum(self, nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    res = []
    for i in range(0, le.(nums)):
      __ i > 0 and nums[i] __ nums[i - 1]:
        continue
      for j in range(i + 1, le.(nums)):
        __ j > i + 1 and nums[j] __ nums[j - 1]:
          continue
        start = j + 1
        end = le.(nums) - 1
        w___ start < end:
          sum = nums[i] + nums[j] + nums[start] + nums[end]
          __ sum < target:
            start += 1
          ____ sum > target:
            end -= 1
          ____
            res.append((nums[i], nums[j], nums[start], nums[end]))
            start += 1
            end -= 1
            w___ start < end and nums[start] __ nums[start - 1]:
              start += 1
            w___ start < end and nums[end] __ nums[end + 1]:
              end -= 1
    r_ res
