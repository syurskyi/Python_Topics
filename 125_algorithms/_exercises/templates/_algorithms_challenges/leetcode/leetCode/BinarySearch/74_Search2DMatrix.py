#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    # Don't treat it as a 2D matrix, just treat it as a sorted list
    ___ searchMatrix  matrix, target
        __ n.. matrix:
            r_ False

        # Classic binary search: O(logmn)
        m_rows, n_cols = l..(matrix), l..(matrix[0])
        left, right = 0, m_rows * n_cols - 1

        _____ left <= right:
            mid = (left+right) / 2
            num = matrix[mid / n_cols][mid % n_cols]
            __ num > target:
                right = mid - 1
            ____ num < target:
                left = mid + 1
            ____
                r_ True

        r_ False

"""
[[]]
0
[[1]]
0
[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
34
[[1, 3, 5], [10, 11, 16], [23, 30, 34]]
46
"""
