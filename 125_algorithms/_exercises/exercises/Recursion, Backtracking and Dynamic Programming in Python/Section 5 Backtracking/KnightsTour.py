
c_ KnightsTour:

    ___  -   board_size
        board_size = board_size
        # possible horizontal components of the moves
        x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
        solution_matrix = [[-1 ___ _ __ ra__(board_size)] ___ _ __ ra__(board_size)]

    ___ solve_problem(self

        # we start with the top left cell
        solution_matrix[0][0] = 0

        # first parameter is the counter
        # the second and third parameter is the location (0, 0)
        __ solve(1, 0, 0
            print_solution()
        ____
            print('There is no feasible solution...')

    ___ solve  step_counter, x, y

        # base case
        __ step_counter __ board_size * board_size:
            r_ T..

        # we have to consider all the possible moves and find the valid one
        ___ move_index __ ra__(le_(x_moves)):

            next_x = x + x_moves[move_index]
            next_y = y + y_moves[move_index]

            __ is_valid_move(next_x, next_y
                # it is a valid step so we can update the solution_matrix
                solution_matrix[next_x][next_y] = step_counter

                __ solve(step_counter+1, next_x, next_y
                    r_ T..

                # BACKTRACK AS USUAL - we have to remove the step and
                # reinitialize the solution_matrix with -1
                solution_matrix[next_x][next_y] = -1

        r_ F..

    ___ is_valid_move  x, y

        # that the knight will not step outside the chessboard
        # the knight leaves the board horizontally
        __ x < 0 or x >= board_size:
            r_ F..

        # the knight leaves the board vertically
        __ y < 0 or y >= board_size:
            r_ F..

        # maybe we have already visited that given cell
        # which means that the value is not -1
        __ solution_matrix[x][y] > -1:
            r_ F..

        r_ T..

    ___ print_solution(self
        ___ i __ ra__(board_size
            ___ j __ ra__(board_size
                print(solution_matrix[i][j], end=' ')
            print('\n')


__ ___ __ '__main__':

    # for small values backtracking is fast
    tour = KnightsTour(8)
    tour.solve_problem()
