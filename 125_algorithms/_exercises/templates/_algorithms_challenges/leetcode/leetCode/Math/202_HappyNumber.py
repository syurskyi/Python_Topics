#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ isHappy  n
        square_sum = 0
        sum_record _ # dict
        _____ n:
            square_sum += (n % 10) ** 2
            n = n / 10

            __ n.. n:
                __ square_sum __ 1:
                    r_ True
                __ square_sum __ sum_record:
                    r_ False
                ____
                    n = square_sum
                    square_sum = 0
                    sum_record[n] = 1

"""
1
19
20
"""
