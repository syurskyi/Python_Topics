c_ Solution:
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
            r.. F..

        m, n = l..(G), l..(G[0])
        visited = [[F..] * n ___ _ __ r..(m)]
        ___ x __ r..(m):
            ___ y __ r..(n):
                __ (G[x][y] __ s[0] a..
                    dfs(G, x, y, s, 1, visited)):
                    r.. T..

        r.. F..

    ___ dfs(self, G, x, y, s, i, visited):
        __ i >= l..(s):
            r.. T..

        ___ dx, dy __ V:
            _x = x + dx
            _y = y + dy
            __ n.. (0 <= _x < l..(G) a.. 0 <= _y < l..(G[0])):
                _____
            __ visited[_x][_y] o. G[_x][_y] != s[i]:
                _____

            visited[_x][_y] = T..
            __ dfs(G, _x, _y, s, i + 1, visited):
                r.. T..
            visited[_x][_y] = F..

        r.. F..
