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
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            __ target == nums[mid]:
                return mid
            # Right side is sorted
            elif nums[mid] < nums[right]:
                __ nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
            # Left side is sorted
            else:
                __ nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
        __ nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        return -1
