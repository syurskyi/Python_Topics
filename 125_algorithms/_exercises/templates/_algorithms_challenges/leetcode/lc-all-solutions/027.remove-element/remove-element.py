class Solution(object
  ___ removeElement(self, nums, val
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    slow = -1
    ___ i in range(0, le.(nums)):
      __ nums[i] != val:
        slow += 1
        nums[slow] = nums[i]
    r_ slow + 1
