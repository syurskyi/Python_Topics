class Solution(object):
  ___ firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i < len(nums):
      __ 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
        nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
      else:
        i += 1

    for i in range(0, len(nums)):
      __ nums[i] != i + 1:
        return i + 1
    return len(nums) + 1
