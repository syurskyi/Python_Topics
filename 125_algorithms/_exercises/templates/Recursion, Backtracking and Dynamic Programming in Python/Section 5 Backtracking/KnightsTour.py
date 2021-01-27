
class KnightsTour:

    ___ __init__(self, board_size
        self.board_size = board_size
        # possible horizontal components of the moves
        self.x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
        self.solution_matrix = [[-1 ___ _ __ range(self.board_size)] ___ _ __ range(self.board_size)]

    ___ solve_problem(self

        # we start with the top left cell
        self.solution_matrix[0][0] = 0

        # first parameter is the counter
        # the second and third parameter is the location (0, 0)
        __ self.solve(1, 0, 0
            self.print_solution()
        ____
            print('There is no feasible solution...')

    ___ solve(self, step_counter, x, y

        # base case
        __ step_counter == self.board_size * self.board_size:
            r_ True

        # we have to consider all the possible moves and find the valid one
        ___ move_index __ range(le_(self.x_moves)):

            next_x = x + self.x_moves[move_index]
            next_y = y + self.y_moves[move_index]

            __ self.is_valid_move(next_x, next_y
                # it is a valid step so we can update the solution_matrix
                self.solution_matrix[next_x][next_y] = step_counter

                __ self.solve(step_counter+1, next_x, next_y
                    r_ True

                # BACKTRACK AS USUAL - we have to remove the step and
                # reinitialize the solution_matrix with -1
                self.solution_matrix[next_x][next_y] = -1

        r_ False

    ___ is_valid_move(self, x, y

        # that the knight will not step outside the chessboard
        # the knight leaves the board horizontally
        __ x < 0 or x >= self.board_size:
            r_ False

        # the knight leaves the board vertically
        __ y < 0 or y >= self.board_size:
            r_ False

        # maybe we have already visited that given cell
        # which means that the value is not -1
        __ self.solution_matrix[x][y] > -1:
            r_ False

        r_ True

    ___ print_solution(self
        ___ i __ range(self.board_size
            ___ j __ range(self.board_size
                print(self.solution_matrix[i][j], end=' ')
            print('\n')


__ __name__ == '__main__':

    # for small values backtracking is fast
    tour = KnightsTour(8)
    tour.solve_problem()
