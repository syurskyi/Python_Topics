class Solution(object):
  ___ twoSum(self, nums, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    start, end = 0, len(nums) - 1
    while start < end:
      s = nums[start] + nums[end]
      __ s > target:
        end -= 1
      elif s < target:
        start += 1
      else:
        return (start + 1, end + 1)
