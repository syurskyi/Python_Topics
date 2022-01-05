"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly
twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
__author__ = 'Daniel'


c_ Solution:
    ___ singleNumber  nums):
        """
        Constant space
        :type nums: list[int]
        :rtype: list[int]
        """
        bits = 0
        ___ elt __ nums:
            bits ^= elt

        rightmost_bit_set = bits & -bits
        a = 0
        b = 0
        ___ elt __ nums:
            __ elt & rightmost_bit_set:
                a ^= elt
            ____:
                b ^= elt

        r.. a, b