#!/usr/bin/python3
"""
Given an array of integers A with even length, return true if and only if it is
possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every
0 <= i < len(A) / 2.



Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false
Example 3:

Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or
[2,4,-2,-4].
Example 4:

Input: [1,2,4,16,8,4]
Output: false


Note:

0 <= A.length <= 30000
A.length is even
-100000 <= A[i] <= 100000
"""
____ t___ _______ L..
____ c.. _______ C..


c_ Solution:
    ___ canReorderDoubled  A: L..[i..]) __ b..:
        A.s..(key=a..)
        counter C..(A)
        ___ a __ A:
            __ counter[a] __ 0:
                _____
            __ counter[2*a] __ 0:
                r.. F..

            counter[a] -_ 1
            counter[2*a] -_ 1

        r.. T..

    ___ canReorderDoubled_positive_negative  A: L..[i..]) __ b..:
        """
        sort + counter to form the doubled pairs
        """
        A.s..()
        counter C..(A)
        ___ a __ A:
            __ counter[a] __ 0:
                _____
            counter[a] -_ 1
            __ a > 0
                target 2 * a
            ____ a % 2 !_ 0:
                r.. F..
            ____
                target a // 2

            __ counter[target] > 0
                counter[target] -_ 1
            ____
                r.. F..

        r.. T..


__ _______ __ _______
    ... Solution().canReorderDoubled([4,-2,2,-4]) __ T..
