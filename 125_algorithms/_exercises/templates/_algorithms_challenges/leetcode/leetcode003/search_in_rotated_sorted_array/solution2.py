"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its
index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

c_ Solution(object):
    ___ s..  nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = l..(nums) - 1
        w.... left + 1 < right:
            mid = left + (right - left) / 2
            __ target __ nums[mid]:
                r.. mid
            # Right side is sorted
            ____ nums[mid] < nums[right]:
                __ nums[mid] <= target <= nums[right]:
                    left = mid
                ____:
                    right = mid
            # Left side is sorted
            ____:
                __ nums[left] <= target <= nums[mid]:
                    right = mid
                ____:
                    left = mid
        __ nums[left] __ target:
            r.. left
        ____ nums[right] __ target:
            r.. right
        r.. -1
