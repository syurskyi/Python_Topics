
___ solve_maze maze, x, y, solution, n

    __ x __ n-1 a__ y __ n-1 a__ maze[x][y] __ 1:
        solution[x][y]  1
        r_ T..

    __ is_safe(maze, x, y, n
        solution[x][y]  1

        #x - dir, x is rows, downwards
        __ solve_maze(maze, x+1, y, solution, n
            r_ T..
        #Y-dir, y is columns, horizontally ->
        __ solve_maze(maze, x, y+1, solution, n
            r_ T..

        #backtrack
        maze[x][y]  0
        r_ F..

    r_ F..


___ is_safe(maze, x, y, n

    __ 0 < x < n a__ 0 < y < n a__ maze[x][y] __ 1:
        r_ T..
    r_ F..


maze  [[1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]]

solution  [[0 ___ j __ ra__(4)] ___ i __ ra__(4)]

n  le_(maze)

__ solve_maze(maze, 0, 0, solution, n
    ___ i __ solution:
        ___ j __ i:
            print(st.(j), ' ', end ' ')
        print(' ')