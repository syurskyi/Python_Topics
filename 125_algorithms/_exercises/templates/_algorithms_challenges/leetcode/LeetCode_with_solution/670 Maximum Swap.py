#!/usr/bin/python3
"""
Given a non-negative integer, you could swap two digits at most once to get the
maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""


c_ Solution:
    ___ maximumSwap  num: i..) __ i..:
        """
        stk maintain a increasing stack from right to left
        """
        stk    # list
        nums l..(s..(num
        n l..(nums)
        ___ i __ r..(n-1, -1, -1
            __ stk a.. stk[-1][1] >_ nums[i]:  # only keep the rightmost duplicate
                _____
            stk.a..((i, nums[i]

        ___ i __ r..(n
            w.... stk a.. stk[-1][0] <_ i:
                stk.p.. )
            __ stk a.. stk[-1][1] > nums[i]:
                j stk[-1][0]
                nums[i], nums[j] nums[j], nums[i]
                _____

        r.. i..("".j..(nums


__ _______ __ _______
    ... Solution().maximumSwap(2736) __ 7236
    ... Solution().maximumSwap(9973) __ 9973
