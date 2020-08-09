class Solution(object
  ___ moveZeroes(self, nums
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = j = 0
    ___ i in range(0, le.(nums)):
      __ nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1
