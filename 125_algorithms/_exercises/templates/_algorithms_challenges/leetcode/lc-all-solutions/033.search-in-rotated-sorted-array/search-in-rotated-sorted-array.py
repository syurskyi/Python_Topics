c_ Solution(object):
  ___ s..  nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    __ n.. nums:
      r.. -1
    left = 0
    right = l..(nums) - 1
    w.... left <= right:
      mid = (right + left) / 2
      __ nums[mid] __ target:
        r.. mid
      __ nums[mid] >= nums[left]:
        __ nums[left] <= target <= nums[mid]:
          right = mid - 1
        ____:
          left = mid + 1
      ____:
        __ nums[mid] <= target <= nums[right]:
          left = mid + 1
        ____:
          right = mid - 1
    r.. -1
