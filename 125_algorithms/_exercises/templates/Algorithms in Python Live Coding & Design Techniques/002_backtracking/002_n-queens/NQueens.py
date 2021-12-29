

___ save_queens(board, col, size

    __ col > size:
        r_ T..

    ___ i __ ra__(size
        __ is_safe(board, i, col, size
            board[i][col]  1

            __ save_queens(board, col+1,size
                r_ T..

            #backtrack
            board[i][col]  0

    r_ F..



___ is_safe(board, row, col, size
    # No queen horizontally..row is same
    ___ i __ ra__(col
        __ board[row][i] __ 1:
            r_ F..

    #upper half
    ___ i, j __ z..(ra__(row, -1, -1), ra__(col, -1, -1)):
        __ board[i][j] __ 1:
            r_ F..

    #lower half
    ___ i, j __ z..(ra__(row, size, 1), ra__(col, -1, -1)):
        __ board[i][j] __ 1:
            r_ F..

    r_ T..



board  [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]
         ]

