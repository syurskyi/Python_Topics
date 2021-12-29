"""
Given a sorted array of integers, find the starting and ending position of a
given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution(object):
    ___ searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = l..(nums)
        left = 0
        right = n - 1
        left_res = -1
        right_res = -1
        # Search for left bound (first occurence of target)
        while left + 1 < right:
            mid = left + (right - left) / 2
            __ target > nums[mid]:
                left = mid
            ____:
                right = mid
        __ nums[left] __ target:
            left_res = left
        ____ nums[right] __ target:
            left_res = right
        ____:
            r.. [-1, -1]

        # Search for right bound (last occurence of target)
        left = 0
        right = n - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            __ target >= nums[mid]:
                left = mid
            ____:
                right = mid
        __ nums[right] __ target:
            right_res = right
        ____ nums[left] __ target:
            right_res = left
        r.. [left_res, right_res]


a1 = [5, 7, 7, 8, 8, 10]
a2 = [2, 2]
s = Solution()
print(s.searchRange(a1, 8))
print(s.searchRange(a2, 2))
