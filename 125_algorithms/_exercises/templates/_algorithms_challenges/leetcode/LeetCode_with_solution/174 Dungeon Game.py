"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon
consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and
must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or
below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other
rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each
step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path
RIGHT-> RIGHT -> DOWN -> DOWN.

-2(K) -3	3
-5    -10	1
10	  30   -5(P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the
princess is imprisoned.
"""
__author__ 'Daniel'
_______ ___


c_ Solution:
    ___ calculateMinimumHP  dungeon
        """
        dp
        Let F represent the HP
        Starting backward
        DP transition function:
        path = min(F[i+1][j], F[i][j+1])  # choose the right or down path with minimum HP required
        F[i][j] = max(1, path-dungeon[i][j])  # adjust for current cell

        :type dungeon: list[list[int]
        :rtype: int
        """
        m l..(dungeon)
        n l..(dungeon 0

        F [[___.maxint ___ _ __ x..(n+1)] ___ _ __ x..(m+1)]
        ___ i __ x..(m-1, -1, -1
            ___ j __ x..(n-1, -1, -1
                __ i __ m-1 a.. j __ n-1:
                    F[i][j] m..(1, 1-dungeon[i][j])
                ____
                    p.. m..(F[i+1][j], F[i][j+1])  # choose the path with minimum HP required
                    F[i][j] m..(1, p..-dungeon[i][j])  # adjust for current cell

        r.. F 0 0 

    ___ calculateMinimumHP_error  dungeon
        """
        dp
        Not just the end results. We have to ensure at every cell the life > 0.
        Starting forward
        :type dungeon: list[list[int]
        :rtype: int
        """
        m l..(dungeon)
        n l..(dungeon 0
        __ m __ 1 a.. n __ 1:
            r.. 1-m..(0, dungeon 0 0 )

        F [[-___.maxint-1 ___ _ __ x..(n+1)] ___ _ __ x..(m+1)]
        ___ i __ x..(1, m+1
            ___ j __ x..(1, n+1
                __ i __ 1 a.. j __ 1:
                    F[i][j] dungeon[i-1][j-1]
                ____
                    F[i][j] m..(F[i-1][j], F[i][j-1])+dungeon[i-1][j-1]
                    F[i][j] m..(F[i][j], dungeon[i-1][j-1])

        r.. 1-F[-1][-1]


__ _______ __ _______
    ... Solution().calculateMinimumHP([[-3, 5]]) __ 4
    ... Solution().calculateMinimumHP([[2, 1], [1, -1]]) __ 1
