#!/usr/bin/python3
"""
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
this case, 6 units of rain water (blue section) are being trapped.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

c_ Solution:
    ___ trap(self, height: List[i..]) __ i..:
        """
        At each position, the water is determined by the left and right max

        Let lefts[i] be the max(height[:i])
        Let rights[i] be the max(height[i:])
        """
        n = l..(height)
        lefts = [0 ___ _ __ r..(n+1)]
        rights = [0 ___ _ __ r..(n+1)]
        ___ i __ r..(1, n+1):  # i, index of lefts
            lefts[i] = max(lefts[i-1], height[i-1])
        ___ i __ r..(n-1, -1, -1):
            rights[i] = max(rights[i+1], height[i])

        ret = 0
        ___ i __ r..(n):
            ret += max(
                0,
                m..(lefts[i], rights[i+1]) - height[i]
            )
        r.. ret
