c_ Solution:
    ___ longestIncreasingPath  G):
        """
        :type G: List[List[int]]
        :rtype: int
        """
        __ n.. G o. n.. G[0]:
            r.. 0

        V = (
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
                size = dfs(G, x, y, memo)
                __ size > ans:
                    ans = size

        r.. ans

    ___ dfs  G, x, y, memo):
        __ memo[x][y] > 0:
            r.. memo[x][y]

        res = 1

        ___ dx, dy __ V:
            _x = x + dx
            _y = y + dy
            __ n.. (0 <= _x < l..(G) a.. 0 <= _y < l..(G[0])):
                _____
            __ G[x][y] >= G[_x][_y]:
                _____
            size = 1 + dfs(G, _x, _y, memo)
            __ size > res:
                res = size

        memo[x][y] = res
        r.. res
