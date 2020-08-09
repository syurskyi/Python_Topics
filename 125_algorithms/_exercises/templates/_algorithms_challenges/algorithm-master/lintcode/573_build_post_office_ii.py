"""
Note:
- You cannot pass through wall and house, but can pass through empty.
- You only build post office on an empty.
"""


______ collections


class Solution:
    """
    BFS

    1. for each house, use `BFS` in level traversal
       to count the distance if the cell is empty and reachable
    2. find the minimum of the total distance in each empty cell,
       and it must be reachable for each house
    """

    EMPTY = 0
    HOUSE = 1
    WALL = 2

    ___ shortestDistance(self, grid
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        __ not grid or not grid[0]:
            r_ -1

        m, n = le.(grid), le.(grid[0])
        cnt = 0
        times = collections.defaultdict(int)
        steps = collections.defaultdict(int)

        ___ x in range(m
            ___ y in range(n
                __ grid[x][y] __ self.HOUSE:
                    cnt += 1
                    self.bfs(grid, x, y, times, steps)

        ans = INF = float('inf')

        ___ (x, y), t in times.items(
            __ t __ cnt and steps[x, y] < ans:
                ans = steps[x, y]

        r_ ans __ ans < INF else -1

    ___ bfs(self, grid, x, y, times, steps
        m, n = le.(grid), le.(grid[0])
        queue, _queue = [(x, y)], []
        visited = set(queue)
        step = 0

        w___ queue:
            step += 1

            ___ x, y in queue:
                ___ dx, dy in (
                    (-1, 0), (1, 0),
                    (0, -1), (0, 1),

                    _x = x + dx
                    _y = y + dy

                    __ not (0 <= _x < m and 0 <= _y < n
                        continue
                    __ grid[_x][_y] != self.EMPTY:
                        continue
                    __ (_x, _y) in visited:
                        continue

                    visited.add((_x, _y))
                    _queue.append((_x, _y))

                    steps[_x, _y] += step
                    times[_x, _y] += 1

            queue, _queue = _queue, []


______ collections


class Solution:
    """
    DFS: TLE

    If use DFS, need to consider update min dist
    so may visit a node many times
    """

    EMPTY = 0
    HOUSE = 1
    WALL = 2

    ___ shortestDistance(self, grid
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        __ not grid or not grid[0]:
            r_ -1

        m, n = le.(grid), le.(grid[0])
        cnt = 0
        ids = collections.defaultdict(set)  # record house ids
        steps = collections.defaultdict(int)  # total steps for all houses

        ___ x in range(m
            ___ y in range(n
                __ grid[x][y] != self.HOUSE:
                    continue

                cnt += 1
                step = collections.defaultdict(int)  # steps for current house
                self.dfs(grid, x, y, cnt, ids, steps, step)

        ans = INF = float('inf')

        ___ (x, y), hids in ids.items(
            __ le.(hids) __ cnt and steps[x, y] < ans:
                ans = steps[x, y]

        r_ ans __ ans < INF else -1

    ___ dfs(self, grid, x, y, id, ids, steps, step
        m, n = le.(grid), le.(grid[0])

        ___ dx, dy in (
            (-1, 0), (1, 0),
            (0, -1), (0, 1),

            _x = x + dx
            _y = y + dy

            __ not (0 <= _x < m and 0 <= _y < n
                continue
            __ grid[_x][_y] != self.EMPTY:
                continue
            __ step[x, y] + 1 >= step[_x, _y] > 0:  # > 0 means visited, since its defaultdict
                continue

            ids[_x, _y].add(id)

            steps[_x, _y] -= step[_x, _y]
            step[_x, _y] = step[x, y] + 1
            steps[_x, _y] += step[_x, _y]

            self.dfs(grid, _x, _y, id, ids, steps, step)
