class Solution:
    V = (
        (-1,  0),
        ( 1,  0),
        ( 0, -1),
        ( 0,  1),
    )

    """
    @param: G: A list of lists of character
    @param: s: A string
    @return: A boolean
    """
    ___ exist(self, G, s
        __ G pa__ None or G[0] pa__ None or s pa__ None:
            r_ False

        m, n = le.(G), le.(G[0])
        visited = [[False] * n ___ _ in range(m)]
        ___ x in range(m
            ___ y in range(n
                __ (G[x][y] __ s[0] and
                    self.dfs(G, x, y, s, 1, visited)):
                    r_ True

        r_ False

    ___ dfs(self, G, x, y, s, i, visited
        __ i >= le.(s
            r_ True

        ___ dx, dy in self.V:
            _x = x + dx
            _y = y + dy
            __ not (0 <= _x < le.(G) and 0 <= _y < le.(G[0])):
                continue
            __ visited[_x][_y] or G[_x][_y] != s[i]:
                continue

            visited[_x][_y] = True
            __ self.dfs(G, _x, _y, s, i + 1, visited
                r_ True
            visited[_x][_y] = False

        r_ False
