class Solution(object):
  ___ findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    for i in range(0, len(nums)):
      idx = abs(nums[i]) - 1
      nums[idx] = -nums[idx] __ nums[idx] > 0 else nums[idx]

    for i in range(0, len(nums)):
      __ nums[i] > 0:
        ans.append(i + 1)

    for i in range(0, len(nums)):
      nums[idx] = -nums[idx] __ nums[idx] < 0 else nums[idx]
    return ans
