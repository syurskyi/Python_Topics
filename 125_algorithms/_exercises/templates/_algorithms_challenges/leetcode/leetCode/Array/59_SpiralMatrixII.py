#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ generateMatrix  n
        """
        :type n: int
        :rtype: List[List[int]]
        """
        __ n.. n:
            r_ []

        matrix = [[-1 ___ row __ r..(n)] ___ col __ r..(n)]
        current_num = 1
        step = 0
        _____ step < n / 2:
            edge_len = n - 1 - 2 * step

            # Get number from left to right(up edge)
            ___ i __ r..(edge_len
                matrix[step][i + step] = current_num
                current_num += 1

            # Get number from up to down(right edge)
            ___ i __ r..(edge_len
                matrix[i + step][n - 1 - step] = current_num
                current_num += 1

            # Get number from right to left(down edge)
            ___ i __ r..(edge_len
                matrix[n - 1 - step][n - 1 - step - i] = current_num
                current_num += 1

            # Get number from down to up(left edge)
            ___ i __ r..(edge_len
                matrix[n - 1 - step - i][step] = current_num
                current_num += 1
            step += 1

        __ n % 2 __ 1:
            matrix[n/2][n/2] = current_num
        r_ matrix

"""
0
1
3
4
"""
