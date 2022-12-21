#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ plusOne  digits
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        __ n.. digits:
            r_ [1]

        carry_in = (digits[-1] + 1)/10
        digits[-1] = (digits[-1] + 1) % 10

        index = l..(digits) - 2
        # Every position is the sum of post position and carry_in mod 10
        _____ index >= 0:
            __ digits[index] + carry_in __ 10:
                digits[index] = 0
                carry_in = 1
                index -= 1
            ____
                digits[index] += carry_in
                carry_in = 0
                ______

        # Add the pre carry in number.
        __ carry_in a.. index __ -1:
            digits.insert(0, 1)

        r_ digits

"""
[0]
[1,2,3,4,5,6]
[9,9,9,9,9,9]
"""
