class Solution(object):
  ___ removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ len(nums) <= 2:
      return len(nums)
    cnt = 0
    j = 1
    for i in range(1, len(nums)):
      __ nums[i] == nums[i - 1]:
        cnt += 1
        __ cnt < 2:
          nums[j] = nums[i]
          j += 1
      else:
        nums[j] = nums[i]
        j += 1
        cnt = 0
    return j
