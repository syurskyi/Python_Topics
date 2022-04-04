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

c_ Solution(o..
    ___ searchInsert  nums, target
        n = l..(nums)
        left = 0
        right = n - 1
        w.... left + 1 < right:
            mid = left + (right - left) / 2
            __ mid > 0 a.. nums[mid - 1] < target < nums[mid]:
                r.. mid
            ____ target <_ nums[mid]:
                right = mid
            ____
                left = mid
        __ nums[left] < target < nums[right]:
            r.. left + 1
        ____ nums[left] __ target:
            r.. left
        ____ nums[right] __ target:
            r.. right
        ____ nums[left] > target:
            r.. m..(0, left)
        ____ nums[right] < target:
            r.. m..(n, right)


a1 = [1, 3]
s = Solution()
print s.searchInsert(a1, 2)
