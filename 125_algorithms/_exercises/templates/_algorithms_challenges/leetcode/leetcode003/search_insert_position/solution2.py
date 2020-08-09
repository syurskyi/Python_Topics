# -*- coding: utf-8 -*-
"""
Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in
order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

"""

class Solution(object
    ___ searchInsert(self, nums, target
        n = le.(nums)
        left = 0
        right = n - 1
        w___ left + 1 < right:
            mid = left + (right - left) / 2
            __ mid > 0 and nums[mid - 1] < target < nums[mid]:
                r_ mid
            ____ target <= nums[mid]:
                right = mid
            ____
                left = mid
        __ nums[left] < target < nums[right]:
            r_ left + 1
        ____ nums[left] __ target:
            r_ left
        ____ nums[right] __ target:
            r_ right
        ____ nums[left] > target:
            r_ min(0, left)
        ____ nums[right] < target:
            r_ max(n, right)


a1 = [1, 3]
s = Solution()
print s.searchInsert(a1, 2)
