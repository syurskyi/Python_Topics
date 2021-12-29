class Solution(object):
  ___ search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    __ not nums:
      return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
      mid = (right + left) / 2
      __ nums[mid] == target:
        return mid
      __ nums[mid] >= nums[left]:
        __ nums[left] <= target <= nums[mid]:
          right = mid - 1
        else:
          left = mid + 1
      else:
        __ nums[mid] <= target <= nums[right]:
          left = mid + 1
        else:
          right = mid - 1
    return -1
