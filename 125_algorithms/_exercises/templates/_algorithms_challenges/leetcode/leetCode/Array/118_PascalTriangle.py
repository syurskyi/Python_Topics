#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ generate  numRows
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        __ n.. numRows:
            r_ []
        triangle = [[0 ___ j __ r..(i+1)] ___ i __ r..(numRows)]
        triangle[0] = [1]

        ___ i __ r..(1, numRows
            one_row   # list
            ___ j __ r..(i+1
                num = 0
                __ j < i:
                    num = triangle[i-1][j]
                __ i > j-1 >= 0:
                    num += triangle[i-1][j-1]
                one_row.a.. num)

            triangle[i] = one_row

        r_ triangle

"""
0
10
"""
