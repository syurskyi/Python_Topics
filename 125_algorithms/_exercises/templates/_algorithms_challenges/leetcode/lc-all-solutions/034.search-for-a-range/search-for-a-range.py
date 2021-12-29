class Solution(object):
  ___ searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    l, r = 0, len(nums) - 1
    found = 0
    start, end = 0, 0
    while l < r:
      m = l + (r - l) / 2
      __ target > nums[m]:
        l = m + 1
      else:
        __ target == nums[m]:
          found += 1
        r = m - 1

    __ nums[l] == target:
      found += 1

    start = r
    __ nums[r] != target or r < 0:
      start = r + 1

    l, r = 0, len(nums) - 1
    while l < r:
      m = l + (r - l) / 2
      __ target < nums[m]:
        r = m - 1
      else:
        __ target == nums[m]:
          found += 1
        l = m + 1
    end = l
    __ nums[l] != target:
      end = l - 1

    __ found == 0:
      return [-1, -1]
    return [start, end]
