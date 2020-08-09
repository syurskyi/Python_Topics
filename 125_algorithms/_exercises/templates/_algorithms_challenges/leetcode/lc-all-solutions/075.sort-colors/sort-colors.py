class Solution(object
  ___ sortColors(self, nums
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    x = y = z = -1
    ___ i in range(0, le.(nums)):
      __ nums[i] __ 0:
        x += 1
        y += 1
        z += 1
        __ z != -1:
          nums[z] = 2
        __ y != -1:
          nums[y] = 1
        nums[x] = 0
      ____ nums[i] __ 1:
        y += 1
        z += 1
        nums[z] = 2
        __ x != -1:
          nums[x] = 0
        __ y != -1:
          nums[y] = 1
      ____ nums[i] __ 2:
        z += 1
        __ y != -1:
          nums[y] = 1
        __ x != -1:
          nums[x] = 0
        nums[z] = 2
