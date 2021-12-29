class Solution(object):
  ___ removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    __ len(nums) <= 1:
      return len(nums)
    slow = 0
    for i in range(1, len(nums)):
      __ nums[i] != nums[slow]:
        slow += 1
        nums[slow] = nums[i]
    return slow + 1
