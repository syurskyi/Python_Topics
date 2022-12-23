#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ trap  height
        """ For each bar, calculate its left and right highest elevation.

        Then calculating total area by sum of each bar's height*width.

        There is a brilliant solution in discuss:
        https://discuss.leetcode.com/topic/5125/sharing-my-simple-c-code-o-n-time-o-1-space
        """

        # Get the left highest elevation of each bar
        left_side   # list
        max_high = 0
        ___ high __ height:
            __ high > max_high:
                max_high = high
            left_side.a.. max_high)

        # Get the right highest elevation of each bar
        right_side   # list
        max_high = 0
        ___ high __ height[::-1]:
            __ high > max_high:
                max_high = high
            right_side.a.. max_high)

        # Scan each bar and get the water
        water = 0
        length = l..(height)
        ___ i __ r..(length
            min_side = m.. left_side[i], right_side[length - i - 1])
            __ min_side > height[i]:
                water += min_side - height[i]

        r_ water

"""
[]
[3,0,0,3]
[1,1,1,2,2,1,1]
[0,1,0,2,1,0,1,3,2,1,2,1]
"""
