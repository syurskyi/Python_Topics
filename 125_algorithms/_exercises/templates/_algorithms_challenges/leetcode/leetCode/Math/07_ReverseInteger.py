#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ reverse  x
        """
        :type x: int
        :rtype: int
        """
        negative = 1
        __ x < 0:
            negative = -1
            x = x * -1

        result = 0
        _____ x / 10 != 0:
            result = (result + x % 10) * 10
            x = x / 10
        result += x % 10

        __ abs(result) > 2 ** 31 - 1:
            r_ 0
        r_ result * negative
