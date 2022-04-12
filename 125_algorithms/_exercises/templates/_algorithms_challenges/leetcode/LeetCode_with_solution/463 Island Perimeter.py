#!/usr/bin/python3
"""
You are given a map in form of a two-dimensional integer grid where 1 represents
land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is
completely surrounded by water, and there is exactly one island (i.e., one or
more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water
around the island). One cell is a square with side length 1. The grid is
rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""
c_ Solution:
    dirs [(0, -1), (-1, 0), (0, 1), (1, 0)]

    ___ islandPerimeter  grid
        """
        There is constraint that one concrete island

        check surrounding: O(4) * O(n) = O(n)
        count side for land
        :type grid: List[List[int]]
        :rtype: int
        """
        ret 0
        __ n.. grid:
            r.. ret
        R l..(grid)
        C l..(grid 0
        ___ r0 __ r..(R
            ___ c0 __ r..(C
                __ grid[r0][c0] __ 1:
                    ___ dr, dc __ dirs:
                        r r0 + dr
                        c c0 + dc
                        __ r < 0 o. r >_ R o. c < 0 o. c >_ C:
                            ret += 1
                        ____ grid[r][c] __ 0:
                            ret += 1

        r.. ret


__ _______ __ _______
    grid [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0],
    ]
    ... Solution().islandPerimeter(grid) __ 16
