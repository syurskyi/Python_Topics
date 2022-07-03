#!/usr/bin/python3
"""
Given an integer array, find three numbers whose product is maximum and output
the maximum product.

Example 1:

Input: [1,2,3]
Output: 6


Example 2:

Input: [1,2,3,4]
Output: 24


Note:

The length of the given array will be in range [3,104] and all elements are in
the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of
32-bit signed integer.
"""
_______ h__

____ t___ _______ L..


c_ Solution:
    ___ maximumProduct  nums: L.. i.. __ i..
        """
        heapq nlargest nsmallest
        """
        mxes h__.n.. 3, nums)
        mns h__.nsmallest(3, nums)
        r.. m..(
            mxes[0] * mxes[1] * mxes[2],
            mns[0] * mns[1] * mxes[0],
        )
