#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ maxArea  height
        """
        :type height: List[int]
        :rtype: int
        """
        length = l..(height)
        left = 0
        right = length - 1
        max_area = 0

        # To find the biggest container, we recursively find a container
        # which is much bigger than what we have find before.
        _____ left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = m..(max_area, area)

            # To get a bigger container, we move point(lower height) to right
            __ height[left] < height[right]:
                min_height = height[left]
                left += 1
                _____ height[left] < min_height:
                    left += 1

            # To get a bigger container, we move point(lower height) to left
            ____
                min_height = height[right]
                right -= 1
                _____ height[right] < min_height:
                    right -= 1

        r_ max_area

"""
[1,1]
[1,2,3,4,8,7,6,5]
[]
"""
