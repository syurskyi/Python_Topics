"""
The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a
queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
__author__ = 'Danyang'
INVALID = -1
QUEEN = 1
DEFAULT = 0
directions = [(+1, +1), (-1, -1), (-1, +1), (+1, -1)]
c_ Solution:
    ___ solveNQueens  n):
        """
        backtracking
        :param n: integer
        :return: a list of lists of string
        """
        result    # list
        current = [[0 ___ _ __ x..(n)] ___ _ __ x..(n)]
        backtrack(0, current, result)
        r.. transform2string(result)

    ___ backtrack  queen_index, current, result):
        """
        Search problem: dfs, backtracking

        Python:
        notice, the bound should be checked using "if condition" rather than "try-catch" since negative index is acceptable in python

        :param queen_index:
        :param current: 2D matrix
        :param result: list of 2D matrix
        :return: Nothing
        """
        n = l..(current)
        __ queen_index__n:
            result.a..(current)
            r..

        ___ i __ x..(n):
            __ current[queen_index][i]__INVALID:
                _____

            # place the queen
            new_config = [l..(element) ___ element __ current]  # new copy
            new_config[queen_index][i] = QUEEN

            # update invalid position in the new config
            ___ m __ x..(n):
                # col
                __ new_config[m][i]__DEFAULT:
                    new_config[m][i] = INVALID
                # row
                __ new_config[queen_index][m]__DEFAULT:
                    new_config[queen_index][m] = INVALID

                # diagonal - not optimized
                # row = queen_index+m
                # col = i+m
                # if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT: new_config[row][col] = INVALID
                #
                # row = queen_index-m
                # col = i-m
                # if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT: new_config[row][col] = INVALID
                #
                # row = queen_index-m
                # col = i+m
                # if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT: new_config[row][col] = INVALID
                #
                # row = queen_index+m
                # col = i-m
                # if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT: new_config[row][col] = INVALID

                # diagonal - optimized
                ___ direction __ directions:
                    row = queen_index+direction[0]*m
                    col = i+direction[1]*m
                    __ 0<=row<n a.. 0<=col<n a.. new_config[row][col]__DEFAULT:
                        new_config[row][col] = INVALID

            # dfs
            # backtrack by using clone of the board configuration
            backtrack(queen_index+1, new_config, result)


    ___ transform2string  result):
        string_result    # list
        ___ configuration __ result:
            current    # list
            ___ row __ configuration:
                row = map(l.... x: "." __ x__-1 ____ "Q", row)
                row = "".j..(row)
                current.a..(row)
            string_result.a..(current)
        r.. string_result


__ _____ __ ____
    ... Solution().solveNQueens(4)__[['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]