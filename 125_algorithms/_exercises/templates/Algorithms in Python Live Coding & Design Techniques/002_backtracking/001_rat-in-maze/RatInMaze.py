
___ solve_maze(maze, x, y, solution, n

    __ x == n-1 and y == n-1 and maze[x][y] == 1:
        solution[x][y] = 1
        r_ True

    __ is_safe(maze, x, y, n
        solution[x][y] = 1

        #x - dir, x is rows, downwards
        __ solve_maze(maze, x+1, y, solution, n
            r_ True
        #Y-dir, y is columns, horizontally ->
        __ solve_maze(maze, x, y+1, solution, n
            r_ True

        #backtrack
        maze[x][y] = 0
        r_ False

    r_ False


___ is_safe(maze, x, y, n

    __ 0 <= x < n and 0 <= y < n and maze[x][y] == 1:
        r_ True
    r_ False


maze = [[1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]]

solution = [[0 ___ j __ range(4)] ___ i __ range(4)]

n = le_(maze)

__ solve_maze(maze, 0, 0, solution, n
    ___ i __ solution:
        ___ j __ i:
            print(str(j), ' ', end= ' ')
        print(' ')