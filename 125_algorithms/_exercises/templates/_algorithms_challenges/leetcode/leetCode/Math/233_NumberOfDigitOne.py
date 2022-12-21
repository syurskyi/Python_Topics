#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    # Recursive solution
    ___ countDigitOne  n
        __ n <= 0:
            r_ 0
        ____ n < 10:
            r_ 1
        ____
            units = n % 10
            tens = n / 10
            count = self.countDigitOne(tens - 1) * 10 + tens
            n /= 10
            _____ n:
                __ n % 10 __ 1:
                    count = count + 1 + units
                n = n / 10

            __ units >= 1:
                count += 1
            r_ count

"""
-1
6
12
234545
"""
