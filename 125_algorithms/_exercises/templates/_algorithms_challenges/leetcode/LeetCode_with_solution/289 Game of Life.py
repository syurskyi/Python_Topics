"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by
the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight
neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells
first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause
problems when the active area encroaches the border of the array. How would you address these problems?
"""


__author__ = 'Daniel'


class Solution(object):
    ___ __init__(self):
        self.dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

    ___ gameOfLife(self, board):
        """
        B3/S23, born 3 stays 2 or 3

        In-place solution
        Similar to dp space optimization.
        1. Line buffer, directional, main the entires for previous state.
        2. higher bit, since you got 32-bit int


        new new new
        new cur pre
        pre pre pre

        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = l..(board)
        n = l..(board[0])
        lines = [[0 ___ _ __ xrange(n)] ___ _ __ xrange(2)]
        ___ i __ xrange(m):
            ___ j __ xrange(n):
                lines[(i+1)%2][j] = board[i][j]

                cnt = 0
                ___ d __ self.dirs:
                    I = i+d[0]
                    J = j+d[1]
                    __ 0 <= I < m and 0 <= J < n:
                        __ I < i:
                            cnt += lines[i%2][J]
                        ____ I __ i and J < j:
                            cnt += lines[(i+1)%2][J]
                        ____:
                            cnt += board[I][J]

                __ cnt __ 3:
                    board[i][j] = 1
                ____ cnt __ 2:
                    board[i][j] &= 1
                ____:
                    board[i][j] = 0
