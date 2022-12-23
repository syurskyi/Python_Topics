#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ computeArea  A, B, C, D, E, F, G, H
        size_1 = (C-A) * (D-B)
        size_2 = (G-E) * (H-F)
        left = m..(A, E)
        bottom = m..(B, F)
        right = m.. C, G)
        top = m.. D, H)

        # There is an area coverd by both the two rectangle
        __ left < right a.. bottom < top:
            r_ size_1 + size_2 - (top-bottom) * (right-left)
        ____
            r_ size_1 + size_2

"""
-2
-2
2
2
-2
-2
2
2
0
0
0
0
-1
-1
1
1
"""
