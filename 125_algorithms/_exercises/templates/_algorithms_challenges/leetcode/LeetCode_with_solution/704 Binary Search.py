#!/usr/bin/python3
"""
Given a sorted (in ascending order) integer array nums of n elements and a
target value, write a function to search target in nums. If target exists, then
return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
"""
____ t___ _______ L..


c_ Solution:
    ___ s..  nums: L..[i..], target: i..) __ i..:
        lo = 0
        hi = l..(nums)
        w.... lo < hi:
            mid = (lo + hi) // 2
            __ nums[mid] __ target:
                r.. mid
            ____ nums[mid] < target:
                lo = mid + 1
            ____:
                hi = mid

        r.. -1
