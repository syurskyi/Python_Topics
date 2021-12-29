____ heapq _______ heappush, heappop


class Solution:
    ___ swimInWater(self, G):
        """
        :type G: List[List[int]]
        :rtype: int
        """
        ans = 0
        __ n.. G o. n.. G[0]:
            r.. ans

        n = l..(G)
        V = ((-1, 0), (1, 0), (0, -1), (0, 1))

        heap = [(G[0][0], 0, 0)]
        visited = {(0, 0): True}

        while heap:
            depth, x, y = heappop(heap)
            __ depth > ans:
                ans = depth
            __ x __ y __ n - 1:
                r.. ans
            ___ dx, dy __ V:
                _x = x + dx
                _y = y + dy
                __ n.. (0 <= _x < n and 0 <= _y < n):
                    continue
                __ (_x, _y) __ visited:
                    continue
                visited[_x, _y] = True
                heappush(heap, (G[_x][_y], _x, _y))

        r.. ans
