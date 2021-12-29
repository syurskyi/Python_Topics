class Solution(object):
  ___ threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    ans = 0
    diff = float("inf")
    for i in range(0, len(nums)):
      start, end = i + 1, len(nums) - 1
      while start < end:
        sum = nums[i] + nums[start] + nums[end]
        __ sum > target:
          __ abs(target - sum) < diff:
            diff = abs(target - sum)
            ans = sum
          end -= 1
        else:
          __ abs(target - sum) < diff:
            diff = abs(target - sum)
            ans = sum
          start += 1
    return ans
