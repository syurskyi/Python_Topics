class Solution(object
  ___ searchRange(self, nums, target
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    l, r = 0, le.(nums) - 1
    found = 0
    start, end = 0, 0
    w___ l < r:
      m = l + (r - l) / 2
      __ target > nums[m]:
        l = m + 1
      ____
        __ target __ nums[m]:
          found += 1
        r = m - 1

    __ nums[l] __ target:
      found += 1

    start = r
    __ nums[r] != target or r < 0:
      start = r + 1

    l, r = 0, le.(nums) - 1
    w___ l < r:
      m = l + (r - l) / 2
      __ target < nums[m]:
        r = m - 1
      ____
        __ target __ nums[m]:
          found += 1
        l = m + 1
    end = l
    __ nums[l] != target:
      end = l - 1

    __ found __ 0:
      r_ [-1, -1]
    r_ [start, end]
