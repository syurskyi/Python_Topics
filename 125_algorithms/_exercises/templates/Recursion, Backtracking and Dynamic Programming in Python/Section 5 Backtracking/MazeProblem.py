c_ MazeProblem:

    ___  -   maze_matrix
        maze_matrix = maze_matrix
        maze_size = le_(maze_matrix)
        solution_matrix = [[' - ' ___ _ __ range(maze_size)] ___ _ __ range(maze_size)]
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    ___ solve_problem(self

        # we start with (0,0)
        solution_matrix[0][0] = ' S '

        __ solve(0, 0
            show_result()
        ____
            print('There is no feasible solution...')

    ___ solve  x, y

        __ is_finished(x, y
            r_ T..

        ___ move __ moves:

            next_x = x + move[0]
            next_y = y + move[1]

            __ is_valid(next_x, next_y
                solution_matrix[next_x][next_y] = ' S '

                __ solve(next_x, next_y
                    r_ T..

                # BACKTRACK
                solution_matrix[next_x][next_y] = ' '

        r_ F..

    ___ is_valid  x, y

        # we do not step out of the board
        # horizontally and then vertically
        __ x < 0 or x >= maze_size:
            r_ F..

        __ y < 0 or y >= maze_size:
            r_ F..

        # there may be obstacles (we are not able to use cells that are obstacles)
        # 0 represents obstacles !!!
        __ maze_matrix[x][y] __ 0:
            r_ F..

        # let's check whether we have already included that cell in the solution
        __ solution_matrix[x][y] __ ' S ':
            r_ F..

        r_ T..

    ___ is_finished  x, y
        __ x __ maze_size - 1 and y __ maze_size - 1:
            r_ T..

    ___ show_result(self
        ___ x __ range(maze_size
            ___ y __ range(maze_size
                print(solution_matrix[x][y], end=' ')
            print('\n')


__ ___ __ '__main__':

    # 1: valid cells 0: walls or obstacles
    maze = [[1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1]]

    maze = MazeProblem(maze)
    maze.solve_problem()
