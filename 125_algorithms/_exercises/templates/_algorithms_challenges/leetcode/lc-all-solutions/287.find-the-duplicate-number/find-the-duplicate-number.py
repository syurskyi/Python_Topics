class Solution(object
  ___ findDuplicate(self, nums
    """
    :type nums: List[int]
    :rtype: int
    """
    n = le.(nums) - 1
    start, end = 1, n
    w___ start + 1 < end:
      mid = start + (end - start) / 2
      count = 0
      ___ num in nums:
        __ num < mid:
          count += 1
      __ count >= mid:
        end = mid
      ____
        start = mid
    __ nums.count(start) > nums.count(end
      r_ start
    r_ end
