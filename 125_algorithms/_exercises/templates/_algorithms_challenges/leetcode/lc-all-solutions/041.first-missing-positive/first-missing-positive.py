class Solution(object
  ___ firstMissingPositive(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    w___ i < le.(nums
      __ 0 < nums[i] <= le.(nums) and nums[nums[i] - 1] != nums[i]:
        nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
      ____
        i += 1

    ___ i in range(0, le.(nums)):
      __ nums[i] != i + 1:
        r_ i + 1
    r_ le.(nums) + 1
