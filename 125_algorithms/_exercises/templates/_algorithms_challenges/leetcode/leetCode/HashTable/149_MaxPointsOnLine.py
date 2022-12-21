#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

c.. Solution o..
    ___ maxPoints  points
        __ n.. points:
            r_ 0
        # Record all the duplicate points
        replicate _ # dict
        ___ point __ points:
            replicate[(point.x, point.y)] = replicate.get(
                (point.x, point.y), 0) + 1

        # Get all the different nodes
        diff_points = replicate.keys()
        diff_count = l..(diff_points)
        __ diff_count __ 1:
            r_ replicate[diff_points[0]]

        maxPoints = 0
        # Get all the different slope's point numbers.
        ___ i __ xrange(diff_count-1
            slopes _ # dict
            slope = 0
            ___ j __ r..(i+1, diff_count
                dx = diff_points[i][0] - diff_points[j][0]
                dy = diff_points[i][1] - diff_points[j][1]
                __ dx __ 0:
                    slope = "#"
                ____ dy __ 0:
                    slope = 0
                ____
                    slope = float(dy) / dx
                slopes[slope] = (slopes.get(slope, 0) +
                                 replicate[diff_points[j]])

            maxPoints = m..(maxPoints,
                            m..(slopes.values())+replicate[diff_points[i]])

        r_ maxPoints

"""
[]
[[1,1]]
[[1,1],[2,2],[1,1],[1,1],[2,2],[2,3]]
"""
