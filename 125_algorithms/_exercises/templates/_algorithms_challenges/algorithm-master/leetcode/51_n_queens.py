class Solution:
    ___ solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        __ not n:
            return ans

        G = [['.'] * n for _ in range(n)]
        self.dfs(G, 0, ans)
        return ans

    ___ dfs(self, G, y, ans):
        __ y == len(G):
            ans.append(self.clone_board(G))
            return

        for x in range(len(G)):
            __ self.is_valid(G, x, y):
                G[x][y] = 'Q'
                self.dfs(G, y + 1, ans)
                G[x][y] = '.'

    ___ is_valid(self, G, x, y):
        """
        traverse left half => i in [0, n], j in [0, y - 1] to
        1. avoid `j == y` and speed up
        and return False if
        2. `x == i` => at same row
        3. `x - i = y - j` => `x + j = y + i` => left diagonal line
        4. `x - i = -(y - j)` => `x + y = i + j` => right diagonal line
        """
        for i in range(len(G)):
            for j in range(y):
                __ G[i][j] != 'Q':
                    continue
                __ (x + j == y + i or
                    x + y == i + j or
                    x == i):
                    return False
        return True

    ___ clone_board(self, G):
        res = []
        for R in G:
            res.append(''.join(R))
        return res
