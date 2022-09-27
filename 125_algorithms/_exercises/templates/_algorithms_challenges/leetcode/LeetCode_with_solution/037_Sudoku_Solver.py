c_ Solution o..
    ___ solveSudoku  board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #https://leetcode.com/discuss/84831/java-backtracking-stack-20ms
        empty =    # list
        ___ i __ r.. 9):
            ___ j __ r.. 9):
                __ board[i][j] __ '.':
                    empty.append(9 * i + j)
        solve(board, empty)

    ___ solve  board, empty):
        __ l.. empty) __ 0:
            r_ T..
        first_value = empty[-1]
        row, col = first_value / 9, first_value % 9
        ___ k __ r.. 1, 10):
            __ is_safe(board, row, col, s..(k)):
                board[row][col] = s..(k)
                empty.pop()
                __ solve(board, empty):
                    r_ T..
                board[row][col] = '.'
                empty.append(first_value)
        r_ F..

    ___ is_safe  board, row, col, ch):
        ___ k __ r.. 9):
            __ board[k][col] __ ch:
                r_ F..
            __ board[row][k] __ ch:
                r_ F..
        start_row, start_col = 3 * (row / 3), 3 * (col / 3)
        ___ i __ r.. start_row, start_row + 3):
            ___ j __ r.. start_col, start_col + 3):
                __ board[i][j] __ ch:
                    r_ F..
        r_ T..


