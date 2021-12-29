class Solution(object):
  ___ findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums) - 1
    start, end = 1, n
    while start + 1 < end:
      mid = start + (end - start) / 2
      count = 0
      for num in nums:
        __ num < mid:
          count += 1
      __ count >= mid:
        end = mid
      else:
        start = mid
    __ nums.count(start) > nums.count(end):
      return start
    return end
