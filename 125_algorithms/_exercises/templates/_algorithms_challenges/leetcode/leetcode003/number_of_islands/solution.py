class Solution:
    # @param {character[][]} grid
    # @return {integer}
    ___ numIslands(self, grid
        self.islands = set()  # coordinates of 1s (set of tuples)
        res = 0
        n = le.(grid)
        __ n __ 0:
            r_ 0
        m = le.(grid[0])
        __ m __ 0:
            r_ 0
        for y in range(n
            for x in range(m
                __ grid[y][x] __ '1' and (x, y) not in self.islands:
                    self.probe(grid, x, y, m, n)
                    res += 1
        r_ res

    ___ probe(self, grid, x, y, m, n
        """
        Probe right and down
        """
        __ x >= m or y >= n:
            r_
        ____ grid[y][x] __ '0':
            r_
        ____
            self.islands.add((x, y))
            self.probe(grid, x + 1, y, m, n)
            self.probe(grid, x, y + 1, m, n)


g1 = [
    list('11000'),
    list('11000'),
    list('00100'),
    list('00011')
]
for r in g1:
    print(r)
s = Solution()
print(s.numIslands(g1))
print(s.islands)
