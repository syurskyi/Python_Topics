#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ largestRectangleArea  height
        """
        :type height: List[int]
        :rtype: int
        """
        # Add a bar of height 0 after the tail.
        height.append(0)
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
                no_decrease_stack.append(i)
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
[2,1,5,6,2,3]
[2,1,5,6,2,2,2,3,3]
[2,2,2,2]
"""
