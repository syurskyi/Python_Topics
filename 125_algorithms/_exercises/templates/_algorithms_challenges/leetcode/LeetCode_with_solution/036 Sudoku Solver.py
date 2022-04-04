"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""
__author__ = 'Danyang'
c_ Solution:
    ___ solveSudoku  board
        """
        Solve the Sudoku by modifying the input board in-place.

        NP question: N-Queens, Combination Sum, Combinations, Permutations

        :param board: a 9x9 2D array
        :return: NIL
        """
        # break board
        ___ row __ x..(l..(board:
            board[row] = l..(board[row])
        solve(board, 0, 0)
        ___ row __ x..(l..(board:
            board[row] = "".j..(board[row])

    ___ solve_TLE  board
        """

        :param board: a 9x9 2D array
        :return: Boolean
        """
        n = l..(board)
        __ a..([board[i/n][i%n]!="." ___ i __ x..(n*n)]
            r.. T..

        ___ i __ x..(n
            ___ j __ x..(n
                __ board[i][j]__".":
                    ___ num __ r..(1, 10
                        num_str = s..(num)
                        # row
                        condition_row = a..([board[i][col]!=num_str ___ col __ x..(n)])
                        # col
                        condition_col = a..([board[row][j]!=num_str ___ row __ x..(n)])
                        # square
                        condition_square = a..([board[i/3*3+count/3][j/3*3+count%3]!=num_str ___ count __ x..(n)])

                        __ condition_col a.. condition_row a.. condition_square:
                            board[i][j] = num_str
                            __ n.. solve(board
                                board[i][j] = "."
                            ____:
                                r.. T..

        r.. F..

    ___ solve  board, i, j
        """
        dfs
        :param board: a 9x9 2D array
        :return: Boolean
        """
        __ j>=9:
            r.. solve(board, i+1, 0)
        __ i__9:
            r.. T..

        __ board[i][j]__".":
            ___ num __ r..(1, 10
                num_str = s..(num)  # try number
                # To speed up, use condition short-curcit.
                # row, col, square
                __ a..([board[i][col]!=num_str ___ col __ x..(9)]) a.. \
                        a..([board[row][j]!=num_str ___ row __ x..(9)]) a.. \
                        a..([board[i/3*3+count/3][j/3*3+count%3]!=num_str ___ count __ x..(9)]
                    board[i][j] = num_str
                    __ n.. solve(board, i, j+1
                        board[i][j] = "."  # restore, backtrack, save space
                    ____:
                        r.. T..
        ____:
            r.. solve(board, i, j+1)

        r.. F..

__ _____ __ ____
    Solution().solveSudoku(
        ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6",
         "...2759.."]
    )