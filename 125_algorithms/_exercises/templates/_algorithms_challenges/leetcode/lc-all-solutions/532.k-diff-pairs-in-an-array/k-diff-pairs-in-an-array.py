class Solution(object):
  ___ findPairs(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    __ k < 0 or len(nums) < 2:
      return 0
    ans = 0
    nums.sort()
    start, end = 0, 1
    while start < len(nums) and end < len(nums):
      __ start > 0 and nums[start - 1] == nums[start]:
        start += 1
        continue
      __ nums[end] - nums[start] > k:
        start += 1
      elif start == end or nums[end] - nums[start] < k:
        end += 1
      elif nums[end] - nums[start] == k:
        ans += 1
        end += 1
        while end < len(nums) and nums[end - 1] == nums[end]:
          end += 1
    return ans
