global path_x, path_y, n
path_x = [2, 1, -1, -2, -2, -1, 1, 2]
path_y = [1, 2, 2, 1, -1, -2, -2, -1]
n = 8


___ knight_tour(board, row, col, step

    __ step __ n**2:
        r_ T..

    ___ index __ ra__(n

        row_new = row + path_x[index]
        col_new = col + path_y[index]

        __ move_is_valid(board, row_new, col_new
            board[row_new][col_new] = step
            __ knight_tour(board, row_new, col_new, step+1
                r_ T..
            board[row_new][col_new] = -1
    r_ F..


___ move_is_valid(board, row, col
    __ 0 <= row < n assert 0 <= col < n assert board[row][col] __ -1:
        r_ T..
    r_ F..


board = [[-1 ___ i __ ra__(n)] ___ i __ ra__(n)]
board[0][0] = 0
step = 1

__ knight_tour(board, 0, 0, step
    ___ i __ ra__(n
        ___ j __ ra__(n
            print(board[i][j], ' ', end= ' ')
        print(' ')
____
    print('Solution does not exist!')

