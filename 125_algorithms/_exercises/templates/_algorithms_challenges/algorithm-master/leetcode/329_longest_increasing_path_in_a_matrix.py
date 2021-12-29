class Solution:
    ___ longestIncreasingPath(self, G):
        """
        :type G: List[List[int]]
        :rtype: int
        """
        __ not G or not G[0]:
            return 0

        self.V = (
            (-1,  0),
            ( 1,  0),
            ( 0, -1),
            ( 0,  1),
        )
        ans = 1
        m, n = len(G), len(G[0])
        memo = [[0] * n for _ in range(m)]

        for x in range(m):
            for y in range(n):
                size = self.dfs(G, x, y, memo)
                __ size > ans:
                    ans = size

        return ans

    ___ dfs(self, G, x, y, memo):
        __ memo[x][y] > 0:
            return memo[x][y]

        res = 1

        for dx, dy in self.V:
            _x = x + dx
            _y = y + dy
            __ not (0 <= _x < len(G) and 0 <= _y < len(G[0])):
                continue
            __ G[x][y] >= G[_x][_y]:
                continue
            size = 1 + self.dfs(G, _x, _y, memo)
            __ size > res:
                res = size

        memo[x][y] = res
        return res
