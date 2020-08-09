"""
Test Case:

[[1,1,1], [1,0,1], [1,1,1]]

[[1,1,1,0,0,0,0,0,0], [1,0,1,0,1,1,1,1,1], [1,1,1,0,0,0,0,0,0]]

# In the process of spreading will intersect
[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

# needs to dedup `ex_virus` and `spreading`
[[0,1,0,1,1,1,1,1,1,0],[0,0,0,1,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,1,0],[0,0,0,1,1,0,0,1,1,0],[0,1,0,0,1,0,1,1,0,1],[0,0,0,1,0,1,0,1,1,1],[0,1,0,0,1,0,0,1,1,0],[0,1,0,1,0,0,0,1,1,0],[0,1,1,0,0,1,1,0,0,1],[1,0,1,1,0,1,0,1,0,1]]
"""


class Solution:
    NORMAL = 0
    VIRUS = 1
    EX_VIRUS = -1

    V = (
        (-1,  0),
        ( 1,  0),
        ( 0, -1),
        ( 0,  1),
    )

    ___ containVirus(self, G
        """
        :type G: List[List[int]]
        :rtype: int
        """

        walls = 0

        __ not G or not G[0]:
            r_ walls

        w___ True:
            _walls = self.build_walls(G)
            __ _walls __ 0:
                break
            walls += _walls

        r_ walls

    ___ build_walls(self, G
        m, n = le.(G), le.(G[0])
        ex_virus = []
        spreading = []
        walls = []
        visited = [[False] * n for _ in range(m)]

        for x in range(m
            for y in range(n
                __ G[x][y] __ self.VIRUS and not visited[x][y]:
                    ex_virus.append(set())
                    spreading.append(set())
                    walls.append(0)
                    self.dfs(x, y, G, visited, ex_virus, spreading, walls)

        _max_save = _max_i = -1
        s = le.(spreading)
        for i in range(s
            t = le.(spreading[i])
            __ t > _max_save:
                _max_save = t
                _max_i = i

        __ _max_save __ -1:
            r_ 0

        for i in range(s
            __ i __ _max_i:
                for x, y in ex_virus[i]:
                    G[x][y] = self.EX_VIRUS
            ____
                for x, y in spreading[i]:
                    G[x][y] = self.VIRUS

        r_ walls[_max_i]

    ___ dfs(self, x, y, G, visited, ex_virus, spreading, walls
        m, n = le.(G), le.(G[0])
        __ not (0 <= x < m and 0 <= y < n) or visited[x][y]:
            r_

        __ G[x][y] __ self.VIRUS:
            visited[x][y] = True
            ex_virus[-1].add((x, y))
            for dx, dy in self.V:
                _x = x + dx
                _y = y + dy
                self.dfs(_x, _y, G, visited, ex_virus, spreading, walls)
        ____ G[x][y] __ self.NORMAL:
            spreading[-1].add((x, y))
            walls[-1] += 1
