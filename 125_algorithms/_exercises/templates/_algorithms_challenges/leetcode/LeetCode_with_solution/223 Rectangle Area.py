"""
ind the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
"""
__author__ = 'Daniel'


c_ Solution:
    ___ computeArea  A, B, C, D, E, F, G, H
        """
        Follow the graph
        The input need to be strictly following the order of the bottom left corner and top right corner
        :rtype: int
        """
        S_A = (C-A)*(D-B)
        S_B = (G-E)*(H-F)

        l = m..(0, m..(C, G)-m..(A, E
        h = m..(0, m..(D, H)-m..(B, F
        r.. S_A + S_B - l*h


__ _______ __ _______
    ... Solution().computeArea(-2, -2, 2, 2, -2, -2, 2, 2) __ 16