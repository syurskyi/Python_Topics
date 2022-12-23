#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ maximalRectangle  matrix
        """
        :type matrix: List[list[str]]
        :rtype: int
        """

        __ n.. matrix:
            r_ 0

        m_rows = l..(matrix)
        n_cols = l..(matrix[0])

        # Pre-process: to make every row be a histogram
        process_matrix = [
            [0 ___ col __ r..(n_cols)] ___ row __ r..(m_rows)]
        ___ row __ r..(m_rows
            ___ col __ r..(n_cols
                __ row __ 0:
                    __ matrix[row][col] __ "1":
                        process_matrix[row][col] = 1

                ____
                    num = 1 __ matrix[row][col] __ "1" else 0
                    process_matrix[row][col] = num * (
                        num + process_matrix[row-1][col])

        # Find every max size of row.
        max_size = 0
        ___ row __ r..(m_rows
            max_row_size = self.largestRectangleArea(process_matrix[row])
            max_size = m..(max_row_size, max_size)
        r_ max_size

    # Find the largest rectangle in a histogram
    ___ largestRectangleArea  height
        # Add a bar of height 0 after the tail.
        height.a.. 0)
        size = l..(height)
        no_decrease_stack = [0]
        max_size = height[0]

        i = 0
        _____ i < size:
            cur_num = height[i]
            # If the height of current bar is higher than the stack top,
            # or the stack is empty, push current index to stack
            __ (n.. no_decrease_stack or
                    cur_num > height[no_decrease_stack[-1]]
                no_decrease_stack.a.. i)
                i += 1

            # The current height is lower or same than the top,
            # then pop until current height is higher than the top.
            ____
                index = no_decrease_stack.pop()
                __ no_decrease_stack:
                    width = i - no_decrease_stack[-1] - 1
                ____
                    width = i
                max_size = m..(max_size, width * height[index])

        r_ max_size

"""
[]
[["1","0","1","0"], ["1","1","1","1"]]
"""
