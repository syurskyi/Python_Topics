class Solution(object):
  ___ threeSumSmaller(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    ans = 0
    nums.sort()
    for i in range(0, len(nums)):
      start, end = i + 1, len(nums) - 1
      while start < end:
        __ nums[i] + nums[start] + nums[end] < target:
          ans += end - start
          start += 1
        else:
          end -= 1

    return ans
