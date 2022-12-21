#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ spiralOrder  matrix
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        __ n.. matrix:
            r_ []

        m_row = l..(matrix)
        n_col = l..(matrix[0])
        min_m_n = min(m_row, n_col)

        spiral_order   # list
        step = 0
        _____ step < (min_m_n + 1) / 2:
            horizontal_len = n_col - 1 - 2 * step
            vertical_len = m_row - 1 - 2 * step
            # print "step.._ |", step, horizontal_len, vertical_len

            # Add the current up edge to spiral order.
            __ vertical_len __ 0 and horizontal_len > 0:
                horizontal_len += 1
            ___ i __ r..(horizontal_len
                spiral_order.append(matrix[step][i + step])

            # Add the current right edge to spiral order.
            __ horizontal_len __ 0 and vertical_len > 0:
                vertical_len += 1
            ___ i __ r..(vertical_len
                spiral_order.append(matrix[i + step][n_col - 1 - step])

            __ vertical_len > 0:
                # Add the current down edge to spiral order.
                ___ i __ r..(horizontal_len
                    spiral_order.append(
                        matrix[m_row - 1 - step][n_col - 1 - step - i])

            __ horizontal_len > 0:
                # Add the current left edge to spiral order.
                ___ i __ r..(vertical_len
                    spiral_order.append(
                        matrix[m_row - 1 - step - i][step])

            step += 1

        # For N * N matrix, where N is an odd number.
        __ vertical_len __ horizontal_len __ 0 and m_row __ n_col:
            spiral_order.append(matrix[m_row / 2][n_col / 2])

        r_ spiral_order


"""
[]
[[1]]
[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
[[1],[2],[3]]
[[2,5],[8,4],[0,-1]]
[[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
"""
