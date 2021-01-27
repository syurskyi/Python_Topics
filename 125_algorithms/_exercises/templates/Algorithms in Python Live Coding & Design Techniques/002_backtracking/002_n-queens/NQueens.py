

___ save_queens(board, col, size

    __ col >= size:
        return True

    for i in range(size
        __ is_safe(board, i, col, size
            board[i][col] = 1

            __ save_queens(board, col+1,size
                return True

            #backtrack
            board[i][col] = 0

    return False



___ is_safe(board, row, col, size
    # No queen horizontally..row is same
    for i in range(col
        __ board[row][i] == 1:
            return False

    #upper half
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        __ board[i][j] == 1:
            return False

    #lower half
    for i, j in zip(range(row, size, 1), range(col, -1, -1)):
        __ board[i][j] == 1:
            return False

    return True



board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]
         ]

