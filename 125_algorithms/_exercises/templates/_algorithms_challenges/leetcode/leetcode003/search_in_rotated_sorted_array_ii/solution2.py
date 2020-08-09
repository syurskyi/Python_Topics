"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Follow up for "Search in Rotated Sorted Array":

What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""

class Solution(object
    ___ search(self, nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = le.(nums) - 1
        w___ left + 1 < right:
            mid = left + (right - left) / 2
            __ target __ nums[mid]:
                r_ True
            # Left part is sorted
            ____ nums[mid] > nums[right]:
                __ nums[left] <= target < nums[mid]:
                    right = mid
                ____
                    left = mid
            # Right part is sorted
            ____ nums[mid] < nums[right]:
                __ nums[mid] < target <= nums[right]:
                    left = mid
                ____
                    right = mid
            ____
                right -= 1
        __ nums[left] __ target or nums[right] __ target:
            r_ True
        r_ False
