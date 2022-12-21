#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    # According to:
    # https://leetcode.com/discuss/38997/detailed-explained-8ms-c-solution
    # Key concept:
    # division simply requires us to find how many times we can subtract the
    # divisor from the the dividend without making the dividend negative.

    ___ divide  dividend, divisor
        __ divisor __ 0:
            r_ -1

        # Make sure it's positive or negative
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        answer = 0

        _____ dividend >= divisor:
            multiple, temp = 1, divisor
            _____ dividend >= (temp << 1
                multiple <<= 1
                temp <<= 1
            dividend -= temp
            answer += multiple

        __ n.. positive:
            answer = -answer

        __ (answer > 2147483647) or (answer < -2147483648
            r_ 2147483647
        r_ answer

"""
0
1
12
3
125
-4
1
-1
"""
