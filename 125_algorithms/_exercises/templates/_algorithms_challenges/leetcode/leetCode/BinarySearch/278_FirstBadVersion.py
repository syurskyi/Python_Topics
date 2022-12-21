#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


c.. Solution o..
    # Attention: the latest version of your product fails the quality check
    # That's saying, given n versions must have at least one bad version.
    ___ firstBadVersion  n
        __ n <= 0:
            r_ 0
        left, right = 1, n
        _____ left < right:
            mid = (left + right) / 2
            __ isBadVersion(mid
                right = mid
            ____
                left = mid + 1
        r_ right
