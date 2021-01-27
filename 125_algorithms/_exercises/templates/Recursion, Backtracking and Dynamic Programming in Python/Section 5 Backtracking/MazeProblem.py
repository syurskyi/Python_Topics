class MazeProblem:

    ___ __init__(self, maze_matrix
        self.maze_matrix = maze_matrix
        self.maze_size = le_(maze_matrix)
        self.solution_matrix = [[' - ' ___ _ __ range(self.maze_size)] ___ _ __ range(self.maze_size)]
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    ___ solve_problem(self

        # we start with (0,0)
        self.solution_matrix[0][0] = ' S '

        __ self.solve(0, 0
            self.show_result()
        ____
            print('There is no feasible solution...')

    ___ solve(self, x, y

        __ self.is_finished(x, y
            r_ True

        ___ move __ self.moves:

            next_x = x + move[0]
            next_y = y + move[1]

            __ self.is_valid(next_x, next_y
                self.solution_matrix[next_x][next_y] = ' S '

                __ self.solve(next_x, next_y
                    r_ True

                # BACKTRACK
                self.solution_matrix[next_x][next_y] = ' '

        r_ False

    ___ is_valid(self, x, y

        # we do not step out of the board
        # horizontally and then vertically
        __ x < 0 or x >= self.maze_size:
            r_ False

        __ y < 0 or y >= self.maze_size:
            r_ False

        # there may be obstacles (we are not able to use cells that are obstacles)
        # 0 represents obstacles !!!
        __ self.maze_matrix[x][y] == 0:
            r_ False

        # let's check whether we have already included that cell in the solution
        __ self.solution_matrix[x][y] == ' S ':
            r_ False

        r_ True

    ___ is_finished(self, x, y
        __ x == self.maze_size - 1 and y == self.maze_size - 1:
            r_ True

    ___ show_result(self
        ___ x __ range(self.maze_size
            ___ y __ range(self.maze_size
                print(self.solution_matrix[x][y], end=' ')
            print('\n')


__ __name__ == '__main__':

    # 1: valid cells 0: walls or obstacles
    maze = [[1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1]]

    maze = MazeProblem(maze)
    maze.solve_problem()
