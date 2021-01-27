global path_x, path_y, n
path_x = [2, 1, -1, -2, -2, -1, 1, 2]
path_y = [1, 2, 2, 1, -1, -2, -2, -1]
n = 8


___ knight_tour(board, row, col, step

    __ step == n**2:
        return True

    for index in range(n

        row_new = row + path_x[index]
        col_new = col + path_y[index]

        __ move_is_valid(board, row_new, col_new
            board[row_new][col_new] = step
            __ knight_tour(board, row_new, col_new, step+1
                return True
            board[row_new][col_new] = -1
    return False


___ move_is_valid(board, row, col
    __ 0 <= row < n and 0 <= col < n and board[row][col] == -1:
        return True
    return False


board = [[-1 for i in range(n)] for i in range(n)]
board[0][0] = 0
step = 1

__ knight_tour(board, 0, 0, step
    for i in range(n
        for j in range(n
            print(board[i][j], ' ', end= ' ')
        print(' ')
____
    print('Solution does not exist!')

