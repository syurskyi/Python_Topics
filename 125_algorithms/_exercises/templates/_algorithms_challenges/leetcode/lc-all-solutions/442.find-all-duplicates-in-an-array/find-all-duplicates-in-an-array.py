class Solution(object):
  ___ findDuplicates(self, nums):
    ans = []
    for i in range(0, len(nums)):
      while nums[nums[i] - 1] != nums[i]:
        tmp = nums[nums[i] - 1]
        nums[nums[i] - 1] = nums[i]
        nums[i] = tmp
    for i in range(0, len(nums)):
      __ i + 1 != nums[i]:
        ans.append(nums[i])
    return ans
