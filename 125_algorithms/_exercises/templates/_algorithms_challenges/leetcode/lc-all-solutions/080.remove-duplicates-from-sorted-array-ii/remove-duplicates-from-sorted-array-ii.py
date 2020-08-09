class Solution(object
  ___ removeDuplicates(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ le.(nums) <= 2:
      r_ le.(nums)
    cnt = 0
    j = 1
    for i in range(1, le.(nums)):
      __ nums[i] __ nums[i - 1]:
        cnt += 1
        __ cnt < 2:
          nums[j] = nums[i]
          j += 1
      ____
        nums[j] = nums[i]
        j += 1
        cnt = 0
    r_ j
