class Solution(object):
  ___ search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    start, end = 0, len(nums) - 1
    while start + 1 < end:
      mid = start + (end - start) / 2
      __ nums[mid] == target:
        return True
      __ nums[start] < nums[mid]:
        __ nums[start] <= target <= nums[mid]:
          end = mid
        else:
          start = mid
      elif nums[start] > nums[mid]:
        __ nums[mid] <= target <= nums[end]:
          start = mid
        else:
          end = mid
      else:
        start += 1

    __ nums[start] == target:
      return True
    __ nums[end] == target:
      return True
    return False
