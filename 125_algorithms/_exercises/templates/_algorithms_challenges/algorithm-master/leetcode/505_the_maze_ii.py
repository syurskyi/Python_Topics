class Solution:
    """
    BFS
    """
    ___ shortestDistance(self, maze, start, destination
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int

        >>> s = Solution()
        >>> maze = [[0, 0, 1, 0, 0],
        ...         [0, 0, 0, 0, 0],
        ...         [0, 0, 0, 1, 0],
        ...         [1, 1, 0, 1, 1],
        ...         [0, 0, 0, 0, 0]]

        >>> s.shortestDistance(maze, [0, 4], [4, 4])
        12

        >>> s.shortestDistance(maze, [0, 4], [3, 2])
        -1
        """
        __ not maze or not maze[0]:
            r_ -1

        m, n = le.(maze), le.(maze[0])
        sx, sy = start
        tx, ty = destination
        queue = [(sx, sy)]
        distance = {(sx, sy 0}

        for x, y in queue:
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _x = x + dx
                _y = y + dy
                _step = 0

                w___ 0 <= _x < m and 0 <= _y < n and maze[_x][_y] __ 0:
                    _x += dx
                    _y += dy
                    _step += 1

                _x -= dx
                _y -= dy

                __ ((_x, _y) in distance and
                    distance[x, y] + _step >= distance[_x, _y]
                    continue

                distance[_x, _y] = distance[x, y] + _step

                __ _x __ tx and _y __ ty:
                    r_ distance[_x, _y]

                queue.append((_x, _y))

        r_ -1




______ heapq


class Solution2:
    """
    Dijkstra
    """
    ___ shortestDistance(self, maze, start, destination
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int

        >>> s = Solution2()
        >>> maze = [[0, 0, 1, 0, 0],
        ...         [0, 0, 0, 0, 0],
        ...         [0, 0, 0, 1, 0],
        ...         [1, 1, 0, 1, 1],
        ...         [0, 0, 0, 0, 0]]

        >>> s.shortestDistance(maze, [0, 4], [4, 4])
        12

        >>> s.shortestDistance(maze, [0, 4], [3, 2])
        -1
        """
        __ not maze or not maze[0]:
            r_ -1

        m, n = le.(maze), le.(maze[0])
        sx, sy = start
        tx, ty = destination
        heap = [(sx, sy)]
        distance = {(sx, sy 0}

        w___ heap:
            x, y = heapq.heappop(heap)

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _x = x + dx
                _y = y + dy

                w___ 0 <= _x < m and 0 <= _y < n and maze[_x][_y] __ 0:
                    _x += dx
                    _y += dy

                _x -= dx
                _y -= dy

                _step = distance[x, y] + abs(_x - x) + abs(_y - y)

                __ (_x, _y) in distance and _step >= distance[_x, _y]:
                    continue

                __ _x __ tx and _y __ ty:
                    r_ _step

                distance[_x, _y] = _step
                heapq.heappush(heap, (_x, _y))

        r_ -1
