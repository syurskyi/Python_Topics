"""
Test Case:

[[1,1,1], [1,0,1], [1,1,1]]

[[1,1,1,0,0,0,0,0,0], [1,0,1,0,1,1,1,1,1], [1,1,1,0,0,0,0,0,0]]

# In the process of spreading will intersect
[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

# needs to dedup `ex_virus` and `spreading`
[[0,1,0,1,1,1,1,1,1,0],[0,0,0,1,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,1,0],[0,0,0,1,1,0,0,1,1,0],[0,1,0,0,1,0,1,1,0,1],[0,0,0,1,0,1,0,1,1,1],[0,1,0,0,1,0,0,1,1,0],[0,1,0,1,0,0,0,1,1,0],[0,1,1,0,0,1,1,0,0,1],[1,0,1,1,0,1,0,1,0,1]]
"""


c_ Solution:
    NORMAL = 0
    VIRUS = 1
    EX_VIRUS = -1

    V = (
        (-1,  0),
        ( 1,  0),
        ( 0, -1),
        ( 0,  1),
    )

    ___ containVirus  G):
        """
        :type G: List[List[int]]
        :rtype: int
        """

        walls = 0

        __ n.. G o. n.. G[0]:
            r.. walls

        w... T...
            _walls = build_walls(G)
            __ _walls __ 0:
                _____
            walls += _walls

        r.. walls

    ___ build_walls  G):
        m, n = l..(G), l..(G[0])
        ex_virus    # list
        spreading    # list
        walls    # list
        visited = [[F..] * n ___ _ __ r..(m)]

        ___ x __ r..(m):
            ___ y __ r..(n):
                __ G[x][y] __ VIRUS a.. n.. visited[x][y]:
                    ex_virus.a..(s..())
                    spreading.a..(s..())
                    walls.a..(0)
                    dfs(x, y, G, visited, ex_virus, spreading, walls)

        _max_save = _max_i = -1
        s = l..(spreading)
        ___ i __ r..(s):
            t = l..(spreading[i])
            __ t > _max_save:
                _max_save = t
                _max_i = i

        __ _max_save __ -1:
            r.. 0

        ___ i __ r..(s):
            __ i __ _max_i:
                ___ x, y __ ex_virus[i]:
                    G[x][y] = EX_VIRUS
            ____:
                ___ x, y __ spreading[i]:
                    G[x][y] = VIRUS

        r.. walls[_max_i]

    ___ dfs  x, y, G, visited, ex_virus, spreading, walls):
        m, n = l..(G), l..(G[0])
        __ n.. (0 <= x < m a.. 0 <= y < n) o. visited[x][y]:
            r..

        __ G[x][y] __ VIRUS:
            visited[x][y] = T..
            ex_virus[-1].add((x, y))
            ___ dx, dy __ V:
                _x = x + dx
                _y = y + dy
                dfs(_x, _y, G, visited, ex_virus, spreading, walls)
        ____ G[x][y] __ NORMAL:
            spreading[-1].add((x, y))
            walls[-1] += 1
