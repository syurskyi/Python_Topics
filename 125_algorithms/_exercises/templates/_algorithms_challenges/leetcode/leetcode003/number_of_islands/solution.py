class Solution:
    # @param {character[][]} grid
    # @return {integer}
    ___ numIslands(self, grid):
        self.islands = set()  # coordinates of 1s (set of tuples)
        res = 0
        n = l..(grid)
        __ n __ 0:
            r.. 0
        m = l..(grid[0])
        __ m __ 0:
            r.. 0
        ___ y __ r..(n):
            ___ x __ r..(m):
                __ grid[y][x] __ '1' and (x, y) n.. __ self.islands:
                    self.probe(grid, x, y, m, n)
                    res += 1
        r.. res

    ___ probe(self, grid, x, y, m, n):
        """
        Probe right and down
        """
        __ x >= m o. y >= n:
            r..
        ____ grid[y][x] __ '0':
            r..
        ____:
            self.islands.add((x, y))
            self.probe(grid, x + 1, y, m, n)
            self.probe(grid, x, y + 1, m, n)


g1 = [
    l..('11000'),
    l..('11000'),
    l..('00100'),
    l..('00011')
]
___ r __ g1:
    print(r)
s = Solution()
print(s.numIslands(g1))
print(s.islands)
