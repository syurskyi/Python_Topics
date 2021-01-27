class QueensProblem:

    ___ __init__(self, n
        self.n = n
        self.chess_table = [[0 ___ i __ range(n)] ___ j __ range(n)]

    ___ solve_n_queens(self

        # we start with the first queen (with index 0)
        __ self.solve(0
            self.print_queens()
        ____
            # when we have considered all the possible configurations without a success
            # then it means there is no solution (3x3 with 3 queens)
            print('There is no solution to the problem...')

    # col_index is the same as the index of the queen
    ___ solve(self, col_index

        # we have solved the problem - base case
        __ col_index == self.n:
            r_ True

        # let's try to find a position for queen (col_index) within a given column
        ___ row_index __ range(self.n
            __ self.is_place_valid(row_index, col_index
                # 1 means that there is a queen at the given location
                self.chess_table[row_index][col_index] = 1

                # we call the same function with col_index+1
                # we try to find the location of the next queen in the next column
                __ self.solve(col_index+1
                    r_ True

                # BACKTRACK
                print('BACKTRACKING ...')
                self.chess_table[row_index][col_index] = 0

        # when we have considered all the rows in a col without
        # finding a valid cell for the queen
        r_ False

    ___ is_place_valid(self, row_index, col_index

        # check the rows (whether given queens can attack each other horizontally)
        # it means that there is already at least 1 queen in that given row
        ___ i __ range(self.n
            __ self.chess_table[row_index][i] == 1:
                r_ False

        # we do not have to check the same column because we implement the problem
        # such that we assign 1 queen to every single column

        # we have to check the diagonals
        # from top left to bottom right
        j = col_index
        ___ i __ range(row_index, -1, -1

            __ i < 0:
                break

            __ self.chess_table[i][j] == 1:
                r_ False

            j = j - 1

        # we have to check the diagonals
        # from top right to bottom left
        j = col_index
        ___ i __ range(row_index, self.n

            __ j < 0:
                break

            __ self.chess_table[i][j] == 1:
                r_ False

            j = j - 1

        r_ True

    ___ print_queens(self
        ___ i __ range(self.n
            ___ j __ range(self.n
                __ self.chess_table[i][j] == 1:
                    print(' Q ', end='')
                ____
                    print(' - ', end='')
            print('\n')


__ __name__ == '__main__':
    queens = QueensProblem(100)
    queens.solve_n_queens()
