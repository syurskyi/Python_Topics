class Solution:
    """
    @param matrix : the martix
    @return: the distance of grid to the police
    """
    ___ policeDistance(self, matrix
        m, n = le.(matrix), le.(matrix)

        POLICE = 1
        WALL = -1
        EMPTY = 0

        ans = [[float('inf')] * n for _ in range(m)]
        queue = []

        for x in range(m
            for y in range(n
                __ matrix[x][y] __ WALL:
                    ans[x][y] = -1
                ____ matrix[x][y] __ POLICE:
                    ans[x][y] = 0
                    queue.append((x, y))

        for x, y in queue:
            for dx, dy in (
                (-1, 0), (1, 0),
                (0, -1), (0, 1),

                _x = x + dx
                _y = y + dy

                __ not (0 <= _x < m and 0 <= _y < n
                    continue
                __ matrix[_x][_y] __ WALL:
                    continue
                __ ans[_x][_y] <= ans[x][y] + 1:
                    continue

                ans[_x][_y] = ans[x][y] + 1
                queue.append((_x, _y))

        r_ ans
