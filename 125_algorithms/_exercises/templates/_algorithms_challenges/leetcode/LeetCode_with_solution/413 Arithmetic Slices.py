#!/usr/bin/python3
"""
A sequence of number is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the same.

The function should return the number of arithmetic slices in the array A.
"""

c_ Solution:
    ___ c.. self, l
        r.. (l-1) * l // 2

    ___ numberOfArithmeticSlices  A
        """
        Diff the array, find the pattern.
        Find that it is a function of length of the sequence
        With 3 consecutive sequence (l - 1) * l / 2

        :type A: List[int]
        :rtype: int
        """
        ret = 0
        __ l..(A) < 3:
            r.. ret

        delta    # list
        ___ i __ r..(1, l..(A:
            delta.a..(A[i] - A[i-1])

        s = 0
        e = 0
        w.... s < l..(delta
            w.... e < l..(delta) a.. delta[s] __ delta[e]:
                e += 1

            l = e - s
            ret += c.. l)

            s = e

        r.. ret


__ _______ __ _______
    ... Solution().numberOfArithmeticSlices([1, 2, 3, 4]) __ 3
