class Solution(object):
  ___ sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    x = y = z = -1
    for i in range(0, len(nums)):
      __ nums[i] == 0:
        x += 1
        y += 1
        z += 1
        __ z != -1:
          nums[z] = 2
        __ y != -1:
          nums[y] = 1
        nums[x] = 0
      elif nums[i] == 1:
        y += 1
        z += 1
        nums[z] = 2
        __ x != -1:
          nums[x] = 0
        __ y != -1:
          nums[y] = 1
      elif nums[i] == 2:
        z += 1
        __ y != -1:
          nums[y] = 1
        __ x != -1:
          nums[x] = 0
        nums[z] = 2
