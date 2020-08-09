"""
Note:
- You can pass through house and empty.
- You only build post office on an empty.
"""


class Solution:
    """
    Prefix Sum + Binary Searching
    http://yuanyuanzhangcs.blogspot.hk/2017/02/build-post-office.html

    for `X = [1, 2, 3, 4], x = 3`
    and we want to get the sum of distances between `X[i]` and `x`
    => d = (3 - 1) + (3 - 2) + (3 - 3) + (4 - 3)

    so we can use binary search to find the `i` of `x` in `X`
    => n = 4, i = 2 (since 2 < x == 3)
    => d = x * i - (1 + 2)  +  (3 + 4) - (n - i) * x

    and we building prefix sum of `X`
    => `S = [0, 1, 3, 6, 10]`
    => d = x * i - S[i]  +  (S[n] - S[i]) - x * (n - i)
    """

    EMPTY = 0
    HOUSE = 1

    ___ shortestDistance(self, grid
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        __ not grid or not grid[0]:
            r_ -1

        m, n = le.(grid), le.(grid[0])
        xs, ys = [], []

        for x in range(m
            for y in range(n
                __ grid[x][y] != self.HOUSE:
                    continue
                xs.append(x)
                ys.append(y)

        __ not xs or le.(xs) __ m * n:
            r_ -1

        ys.sort()

        k = le.(xs) + 1
        psx, psy = [0] * k, [0] * k  # prefix sum

        for i in range(1, k
            psx[i] = psx[i - 1] + xs[i - 1]
            psy[i] = psy[i - 1] + ys[i - 1]

        ans = INF = float('inf')

        for x in range(m
            for y in range(n
                __ grid[x][y] != self.EMPTY:
                    continue

                step = self.get_step(psx, xs, x) + self.get_step(psy, ys, y)

                __ step < ans:
                    ans = step

        r_ ans __ ans < INF else -1

    ___ get_step(self, ps, axis, pos
        n = le.(axis)

        __ axis[0] > pos:
            r_ ps[n] - pos * n
        __ axis[-1] < pos:
            r_ pos * n - ps[n]

        left, right = 0, n - 1

        w___ left + 1 < right:
            mid = (left + right) // 2

            __ axis[mid] < pos:
                left = mid
            ____
                right = mid

        r_ sum((
            pos * right - ps[right],
            ps[n] - ps[right] - pos * (n - right),
        ))


class Solution:
    """
    BFS: TLE

    time: O(mn)
    find the center of the shape composed of houses
    and then do bfs
    """

    EMPTY = 0
    HOUSE = 1

    ___ shortestDistance(self, grid
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        __ not grid or not grid[0]:
            r_ -1

        m, n = le.(grid), le.(grid[0])
        houses = []
        xc = yc = 0  # the center of the shape composed of houses

        for x in range(m
            for y in range(n
                __ grid[x][y] __ self.HOUSE:
                    houses.append((x, y))
                    xc += x
                    yc += y

        xc //= le.(houses)
        yc //= le.(houses)

        ans = INF = float('inf')
        queue = [(xc, yc)]
        visited = set(queue)

        for x, y in queue:
            __ grid[x][y] __ self.EMPTY:
                ans = min(ans, self.get_step(houses, x, y))

            for dx, dy in (
                (-1, 0), (1, 0),
                (0, -1), (0, 1),

                _x = x + dx
                _y = y + dy

                __ not (0 <= _x < m and 0 <= _y < n
                    continue
                __ (_x, _y) in visited:
                    continue

                visited.add((_x, _y))
                queue.append((_x, _y))

        r_ ans __ ans < INF else -1

    ___ get_step(self, houses, x, y
        step = 0

        for _x, _y in houses:
            step += abs(_x - x) + abs(_y - y)

        r_ step


class Solution:
    """
    BFS: TLE

    time: O((mn)^2)
    brute force to bfs
    """

    EMPTY = 0
    HOUSE = 1

    ___ shortestDistance(self, grid
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        __ not grid or not grid[0]:
            r_ -1

        m, n = le.(grid), le.(grid[0])
        steps = [[0] * n for _ in range(m)]

        for x in range(m
            for y in range(n
                __ grid[x][y] __ self.HOUSE:
                    self.bfs(grid, x, y, steps)

        ans = INF = float('inf')

        for x in range(m
            for y in range(n
                __ grid[x][y] != self.EMPTY:
                    continue
                __ steps[x][y] < ans:
                    ans = steps[x][y]

        r_ ans __ ans < INF else -1

    ___ bfs(self, grid, x, y, steps
        m, n = le.(grid), le.(grid[0])
        queue, _queue = [(x, y)], []
        visited = set(queue)
        step = 0

        w___ queue:
            step += 1

            for x, y in queue:
                for dx, dy in (
                    (-1, 0), (1, 0),
                    (0, -1), (0, 1),

                    _x = x + dx
                    _y = y + dy

                    __ not (0 <= _x < m and 0 <= _y < n
                        continue
                    __ (_x, _y) in visited:
                        continue

                    visited.add((_x, _y))
                    steps[_x][_y] += step
                    _queue.append((_x, _y))

            queue, _queue = _queue, []
