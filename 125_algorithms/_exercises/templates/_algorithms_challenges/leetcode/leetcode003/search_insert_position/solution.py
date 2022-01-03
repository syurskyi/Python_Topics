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

c_ Solution(object):
    ___ searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = l..(nums)
        __ n.. nums:
            r.. 0
        ____:
            left = 0
            right = n - 1
            w.... left <= right:
                mid = (left + right) / 2
                __ nums[mid] __ target:
                    r.. mid
                ____ (mid < n - 1 a.. nums[mid] < target
                        a.. nums[mid + 1] > target):
                    r.. mid + 1
                ____ target < nums[mid]:
                    right = mid - 1
                ____:
                    left = mid + 1
            __ left > n - 1:
                r.. n
            ____ right < 0:
                r.. 0


a = [1, 3, 5, 6]
s = Solution()
print(s.searchInsert(a, 5))
print(s.searchInsert(a, 2))
print(s.searchInsert(a, 7))
print(s.searchInsert(a, 0))
