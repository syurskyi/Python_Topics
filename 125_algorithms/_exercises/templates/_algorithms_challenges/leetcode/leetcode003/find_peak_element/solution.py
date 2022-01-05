# -*- coding: utf-8 -*-
"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return
its index.

The array may contain multiple peaks, in that case return the index to any one
of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function
should return the index number 2.

Note:
Your solution should be in logarithmic complexity.
"""

c_ Solution(object):
    ___ findPeakElement  nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = l..(nums)
        left = 0
        right = n - 1
        __ n __ 1:
            r.. 0
        w.... left <= right:
            mid = left + (right - left) / 2
            __ mid __ 0 a.. nums[mid] > nums[mid + 1]:
                r.. mid
            ____ mid __ n - 1 a.. nums[mid] > nums[mid - 1]:
                r.. mid
            ____ nums[mid - 1] < nums[mid] > nums[mid + 1]:
                r.. mid
            ____ mid > 0 a.. nums[mid - 1] > nums[mid]:
                right = mid - 1
            ____:
                left = mid + 1
        r.. mid

a1 = [1, 2]
a2 = [1, 2, 1]
s = Solution()
print(s.findPeakElement(a1))
print(s.findPeakElement(a2))
