#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-04 14:00:57


c.. Solution o..
    ___ reverseString  s
        r_ s[::-1]


c.. Solution_2 o..
    ___ reverseString  s
        left, right = 0, l..(s) - 1
        s = list(s)
        _____ left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        r_ "".join(s)


"""
""
"hello"
"  HELLO "
"""
