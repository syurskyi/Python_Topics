class Solution(object
  ___ removeDuplicates(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ le.(nums) <= 1:
      r_ le.(nums)
    slow = 0
    for i in range(1, le.(nums)):
      __ nums[i] != nums[slow]:
        slow += 1
        nums[slow] = nums[i]
    r_ slow + 1
