"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""
__author__ = 'Danyang'
class Solution:
    ___ solveSudoku(self, board
        """
        Solve the Sudoku by modifying the input board in-place.

        NP question: N-Queens, Combination Sum, Combinations, Permutations

        :param board: a 9x9 2D array
        :return: NIL
        """
        # break board
        ___ row in xrange(le.(board)):
            board[row] = list(board[row])
        self.solve(board, 0, 0)
        ___ row in xrange(le.(board)):
            board[row] = "".join(board[row])

    ___ solve_TLE(self, board
        """

        :param board: a 9x9 2D array
        :return: Boolean
        """
        n = le.(board)
        __ all([board[i/n][i%n]!="." ___ i in xrange(n*n)]
            r_ True

        ___ i in xrange(n
            ___ j in xrange(n
                __ board[i][j]__".":
                    ___ num in range(1, 10
                        num_str = str(num)
                        # row
                        condition_row = all([board[i][col]!=num_str ___ col in xrange(n)])
                        # col
                        condition_col = all([board[row][j]!=num_str ___ row in xrange(n)])
                        # square
                        condition_square = all([board[i/3*3+count/3][j/3*3+count%3]!=num_str ___ count in xrange(n)])

                        __ condition_col and condition_row and condition_square:
                            board[i][j] = num_str
                            __ not self.solve(board
                                board[i][j] = "."
                            ____
                                r_ True

        r_ False

    ___ solve(self, board, i, j
        """
        dfs
        :param board: a 9x9 2D array
        :return: Boolean
        """
        __ j>=9:
            r_ self.solve(board, i+1, 0)
        __ i__9:
            r_ True

        __ board[i][j]__".":
            ___ num in range(1, 10
                num_str = str(num)  # try number
                # To speed up, use condition short-curcit.
                # row, col, square
                __ all([board[i][col]!=num_str ___ col in xrange(9)]) and \
                        all([board[row][j]!=num_str ___ row in xrange(9)]) and \
                        all([board[i/3*3+count/3][j/3*3+count%3]!=num_str ___ count in xrange(9)]
                    board[i][j] = num_str
                    __ not self.solve(board, i, j+1
                        board[i][j] = "."  # restore, backtrack, save space
                    ____
                        r_ True
        ____
            r_ self.solve(board, i, j+1)

        r_ False

__ __name____"__main__":
    Solution().solveSudoku(
        ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6",
         "...2759.."]
    )