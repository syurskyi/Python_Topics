#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ calculateMinimumHP  dungeon
        """  Dynamic Programming
        dp[i][j]: the leatest health point must remain before enter room [i, j]
        Initinal: After enter the princess's room,
                  knight's health point should at least be 1.
                  that's say, dp[m_rows-1][n_cols-1] = 1 or 1-demon's hurt
        Then assume the knight go from princess's room(right_down) to up_left.

        DP process: There are two ways to enter to room [i, j], dp[i][j] =
                    1. right to left: dp[i][j+1] - dungeon[i][j] or 1
                    2. down to up: dp[i+1][j] - dungeon[i][j] or 1
        """
        m_rows = l..(dungeon)
        n_cols = l..(dungeon[0])
        dp = [[1 ___ i __ r..(n_cols)] ___ j __ r..(m_rows)]
        __ dungeon[-1][-1] > 0:
            dp[-1][-1] = 1
        ____
            dp[-1][-1] = 1 - dungeon[-1][-1]

        ___ i __ r..(m_rows-1, -1, -1
            ___ j __ r..(n_cols-1, -1, -1
                down_up = None
                right_left = None
                __ i+1 < m_rows:
                    __ dungeon[i][j] >= dp[i+1][j]:
                        down_up = 1
                    ____
                        down_up = dp[i+1][j] - dungeon[i][j]
                __ j+1 < n_cols:
                    __ dungeon[i][j] >= dp[i][j+1]:
                        right_left = 1
                    ____
                        right_left = dp[i][j+1] - dungeon[i][j]
                __ right_left a.. down_up:
                    dp[i][j] = min(down_up, right_left)
                ____ right_left or down_up:
                    dp[i][j] = down_up or right_left
                ____
                    pass

        r_ dp[0][0]
"""
[[0]]
[[-1]]
[[0,-3]]
[[-2,-3,-3], [-5,-10,1], [10,30,-5]]
"""
