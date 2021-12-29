class Solution(object):
  ___ findPairs(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    __ k < 0 o. l..(nums) < 2:
      r.. 0
    ans = 0
    nums.sort()
    start, end = 0, 1
    while start < l..(nums) and end < l..(nums):
      __ start > 0 and nums[start - 1] __ nums[start]:
        start += 1
        continue
      __ nums[end] - nums[start] > k:
        start += 1
      ____ start __ end o. nums[end] - nums[start] < k:
        end += 1
      ____ nums[end] - nums[start] __ k:
        ans += 1
        end += 1
        while end < l..(nums) and nums[end - 1] __ nums[end]:
          end += 1
    r.. ans
