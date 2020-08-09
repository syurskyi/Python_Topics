class Solution:
    ___ solveNQueens(self, n
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        __ not n:
            r_ ans

        G = [['.'] * n ___ _ in range(n)]
        self.dfs(G, 0, ans)
        r_ ans

    ___ dfs(self, G, y, ans
        __ y __ le.(G
            ans.append(self.clone_board(G))
            r_

        ___ x in range(le.(G)):
            __ self.is_valid(G, x, y
                G[x][y] = 'Q'
                self.dfs(G, y + 1, ans)
                G[x][y] = '.'

    ___ is_valid(self, G, x, y
        """
        traverse left half => i in [0, n], j in [0, y - 1] to
        1. avoid `j == y` and speed up
        and return False if
        2. `x == i` => at same row
        3. `x - i = y - j` => `x + j = y + i` => left diagonal line
        4. `x - i = -(y - j)` => `x + y = i + j` => right diagonal line
        """
        ___ i in range(le.(G)):
            ___ j in range(y
                __ G[i][j] != 'Q':
                    continue
                __ (x + j __ y + i or
                    x + y __ i + j or
                    x __ i
                    r_ False
        r_ True

    ___ clone_board(self, G
        res = []
        ___ R in G:
            res.append(''.join(R))
        r_ res
