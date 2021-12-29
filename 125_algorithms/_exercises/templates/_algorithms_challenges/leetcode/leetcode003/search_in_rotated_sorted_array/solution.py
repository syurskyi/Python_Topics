"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its
index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution(object):
    ___ search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = l..(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            __ target __ nums[mid]:
                r.. mid
            # Left part is sorted
            ____ nums[mid] > nums[right]:
                __ target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                ____:
                    left = mid + 1
            # Right part is sorted
            ____:
                __ target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                ____:
                    right = mid - 1
        r.. -1
