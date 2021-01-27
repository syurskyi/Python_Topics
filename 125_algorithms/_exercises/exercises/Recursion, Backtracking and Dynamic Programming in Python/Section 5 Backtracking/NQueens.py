c_ QueensProblem:

    ___  -   n
        n = n
        chess_table = [[0 ___ i __ ra__(n)] ___ j __ ra__(n)]

    ___ solve_n_queens(self

        # we start with the first queen (with index 0)
        __ solve(0
            print_queens()
        ____
            # when we have considered all the possible configurations without a success
            # then it means there is no solution (3x3 with 3 queens)
            print('There is no solution to the problem...')

    # col_index is the same as the index of the queen
    ___ solve  col_index

        # we have solved the problem - base case
        __ col_index __ n:
            r_ T..

        # let's try to find a position for queen (col_index) within a given column
        ___ row_index __ ra__(n
            __ is_place_valid(row_index, col_index
                # 1 means that there is a queen at the given location
                chess_table[row_index][col_index] = 1

                # we call the same function with col_index+1
                # we try to find the location of the next queen in the next column
                __ solve(col_index+1
                    r_ T..

                # BACKTRACK
                print('BACKTRACKING ...')
                chess_table[row_index][col_index] = 0

        # when we have considered all the rows in a col without
        # finding a valid cell for the queen
        r_ F..

    ___ is_place_valid  row_index, col_index

        # check the rows (whether given queens can attack each other horizontally)
        # it means that there is already at least 1 queen in that given row
        ___ i __ ra__(n
            __ chess_table[row_index][i] __ 1:
                r_ F..

        # we do not have to check the same column because we implement the problem
        # such that we assign 1 queen to every single column

        # we have to check the diagonals
        # from top left to bottom right
        j = col_index
        ___ i __ ra__(row_index, -1, -1

            __ i < 0:
                break

            __ chess_table[i][j] __ 1:
                r_ F..

            j = j - 1

        # we have to check the diagonals
        # from top right to bottom left
        j = col_index
        ___ i __ ra__(row_index, n

            __ j < 0:
                break

            __ chess_table[i][j] __ 1:
                r_ F..

            j = j - 1

        r_ T..

    ___ print_queens(self
        ___ i __ ra__(n
            ___ j __ ra__(n
                __ chess_table[i][j] __ 1:
                    print(' Q ', end='')
                ____
                    print(' - ', end='')
            print('\n')


__ ___ __ '__main__':
    queens = QueensProblem(100)
    queens.solve_n_queens()
