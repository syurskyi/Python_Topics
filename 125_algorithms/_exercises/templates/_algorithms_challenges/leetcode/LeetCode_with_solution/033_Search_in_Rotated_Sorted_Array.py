c_ Solution:
    ___ search  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # binary search
        # if start < mid, then left part is sorted
        # if mid < end, then right part is sorted
        ___ get(start, end
          __ start > end:
            r_ -1
          mid = (start + end) / 2
          __ nums[mid] __ target:
            r_ mid
          ____ nums[mid] >= nums[start]: # First half is sorted
            __ target >= nums[start] a.. target < nums[mid]:
              r_ get(start, mid - 1)
            ____
              r_ get(mid + 1, end)
          ____ nums[mid] <= nums[end]: # Second half is sorted
            __ target > nums[mid] a.. target <= nums[end]:
              r_ get(mid + 1, end)
            ____
              r_ get(start, mid - 1)
        r_ get(0, l.. nums) - 1)