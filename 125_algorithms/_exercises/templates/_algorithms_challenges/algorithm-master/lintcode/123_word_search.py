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
        __ G __ N.. o. G[0] __ N.. o. s __ N..
            r.. False

        m, n = l..(G), l..(G[0])
        visited = [[False] * n ___ _ __ r..(m)]
        ___ x __ r..(m):
            ___ y __ r..(n):
                __ (G[x][y] __ s[0] and
                    self.dfs(G, x, y, s, 1, visited)):
                    r.. True

        r.. False

    ___ dfs(self, G, x, y, s, i, visited):
        __ i >= l..(s):
            r.. True

        ___ dx, dy __ self.V:
            _x = x + dx
            _y = y + dy
            __ n.. (0 <= _x < l..(G) and 0 <= _y < l..(G[0])):
                continue
            __ visited[_x][_y] o. G[_x][_y] != s[i]:
                continue

            visited[_x][_y] = True
            __ self.dfs(G, _x, _y, s, i + 1, visited):
                r.. True
            visited[_x][_y] = False

        r.. False
