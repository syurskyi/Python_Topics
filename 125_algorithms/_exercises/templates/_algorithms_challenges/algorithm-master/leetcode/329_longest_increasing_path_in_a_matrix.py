class Solution:
    ___ longestIncreasingPath(self, G):
        """
        :type G: List[List[int]]
        :rtype: int
        """
        __ n.. G o. n.. G[0]:
            r.. 0

        self.V = (
            (-1,  0),
            ( 1,  0),
            ( 0, -1),
            ( 0,  1),
        )
        ans = 1
        m, n = l..(G), l..(G[0])
        memo = [[0] * n ___ _ __ r..(m)]

        ___ x __ r..(m):
            ___ y __ r..(n):
                size = self.dfs(G, x, y, memo)
                __ size > ans:
                    ans = size

        r.. ans

    ___ dfs(self, G, x, y, memo):
        __ memo[x][y] > 0:
            r.. memo[x][y]

        res = 1

        ___ dx, dy __ self.V:
            _x = x + dx
            _y = y + dy
            __ n.. (0 <= _x < l..(G) and 0 <= _y < l..(G[0])):
                continue
            __ G[x][y] >= G[_x][_y]:
                continue
            size = 1 + self.dfs(G, _x, _y, memo)
            __ size > res:
                res = size

        memo[x][y] = res
        r.. res
