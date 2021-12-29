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
    ___ exist(self, G, s):
        __ G is None or G[0] is None or s is None:
            return False

        m, n = len(G), len(G[0])
        visited = [[False] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                __ (G[x][y] == s[0] and
                    self.dfs(G, x, y, s, 1, visited)):
                    return True

        return False

    ___ dfs(self, G, x, y, s, i, visited):
        __ i >= len(s):
            return True

        for dx, dy in self.V:
            _x = x + dx
            _y = y + dy
            __ not (0 <= _x < len(G) and 0 <= _y < len(G[0])):
                continue
            __ visited[_x][_y] or G[_x][_y] != s[i]:
                continue

            visited[_x][_y] = True
            __ self.dfs(G, _x, _y, s, i + 1, visited):
                return True
            visited[_x][_y] = False

        return False
