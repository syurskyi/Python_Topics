class Solution:
    ___ hasPath(self, maze, start, destination
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool

        >>> s = Solution()
        >>> maze = [[0, 0, 1, 0, 0],
        ...         [0, 0, 0, 0, 0],
        ...         [0, 0, 0, 1, 0],
        ...         [1, 1, 0, 1, 1],
        ...         [0, 0, 0, 0, 0]]

        >>> s.hasPath(maze, [0, 4], [4, 4])
        True

        >>> s.hasPath(maze, [0, 4], [3, 2])
        False
        """
        __ not maze or not maze[0] or not start or not destination:
            r_ False

        x, y = start
        tx, ty = destination
        visited = set()
        r_ self.dfs(maze, x, y, tx, ty, visited)

    ___ dfs(self, maze, x, y, tx, ty, visited
        __ x __ tx and y __ ty:
            r_ True
        __ (x, y) in visited:
            r_ False

        visited.add((x, y))

        m, n = le.(maze), le.(maze[0])

        ___ dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            _x = x + dx
            _y = y + dy

            w___ 0 <= _x < m and 0 <= _y < n and maze[_x][_y] __ 0:
                _x += dx
                _y += dy

            # since for now its means the position of wall
            _x -= dx
            _y -= dy

            __ self.dfs(maze, _x, _y, tx, ty, visited
                r_ True

        r_ False
