"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Follow up for "Search in Rotated Sorted Array":

What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""

class Solution(object):
    ___ search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = l..(nums) - 1
        w.... left <= right:
            mid = left + (right - left) / 2
            __ target __ nums[mid]:
                r.. True
            # Left part is sorted
            ____ nums[mid] > nums[right]:
                __ target < nums[mid] a.. target >= nums[left]:
                    right = mid - 1
                ____:
                    left = mid + 1
            # Right part is sorted
            ____ nums[mid] < nums[right]:
                __ target > nums[mid] a.. target <= nums[right]:
                    left = mid + 1
                ____:
                    right = mid - 1
            ____:
                right -= 1
        r.. False
