#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ candy  ratings
        candies = [0 ___ i __ ratings]
        candies[0] = 1
        children_nums = l..(ratings)

        # Scan from left to right
        ___ i __ r..(children_nums - 1
            __ ratings[i + 1] > ratings[i]:
                candies[i + 1] = candies[i] + 1
            ____
                candies[i + 1] = 1

        minimum_candies = 0
        # Scan from right to left
        ___ i __ r..(children_nums - 1, 0, -1
            __ ratings[i - 1] > ratings[i]:
                candies[i - 1] = m..(candies[i] + 1, candies[i - 1])
            ____
                candies[i - 1] = m..(1, candies[i - 1])
            minimum_candies += candies[i]

        r_ minimum_candies + candies[0]


"""
[0]
[2,2,1]
[3,4,8,6,7]
[4,3,8,6,7]
[1,2,4,4,3]
[1,2,4,4,5]
[4,4,4,4,4]
"""
