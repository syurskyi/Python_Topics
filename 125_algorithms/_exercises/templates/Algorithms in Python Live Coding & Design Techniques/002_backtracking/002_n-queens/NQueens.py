

___ save_queens(board, col, size

    __ col >= size:
        r_ True

    ___ i __ range(size
        __ is_safe(board, i, col, size
            board[i][col] = 1

            __ save_queens(board, col+1,size
                r_ True

            #backtrack
            board[i][col] = 0

    r_ False



___ is_safe(board, row, col, size
    # No queen horizontally..row is same
    ___ i __ range(col
        __ board[row][i] == 1:
            r_ False

    #upper half
    ___ i, j __ zip(range(row, -1, -1), range(col, -1, -1)):
        __ board[i][j] == 1:
            r_ False

    #lower half
    ___ i, j __ zip(range(row, size, 1), range(col, -1, -1)):
        __ board[i][j] == 1:
            r_ False

    r_ True



board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]
         ]

