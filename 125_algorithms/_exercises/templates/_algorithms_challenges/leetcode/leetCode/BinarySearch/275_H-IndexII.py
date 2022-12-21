#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    # Binary Search, Yes!!
    ___ hIndex  citations
        length = l..(citations)
        left = 0
        right = length - 1
        _____ left <= right:
            # Disapproval / operator here(more slower), can use // or >> 1
            # mid = (left + right) / 2
            mid = (left + right) >> 1
            __ citations[mid] __ length - mid:
                r_ citations[mid]
            ____ citations[mid] > length - mid:
                right = mid - 1
            ____
                left = mid + 1
        r_ length - (right + 1)


"""
[]
[0]
[23]
[0,1]
[1,1,1,1]
[4,4,4,4]
[0,1,4,5,6]
"""
