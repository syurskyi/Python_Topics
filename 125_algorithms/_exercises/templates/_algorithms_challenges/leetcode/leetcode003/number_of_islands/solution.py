c_ Solution:
    # @param {character[][]} grid
    # @return {integer}
    ___ numIslands  grid
        islands = s..()  # coordinates of 1s (set of tuples)
        res = 0
        n = l..(grid)
        __ n __ 0:
            r.. 0
        m = l..(grid[0])
        __ m __ 0:
            r.. 0
        ___ y __ r..(n
            ___ x __ r..(m
                __ grid[y][x] __ '1' a.. (x, y) n.. __ islands:
                    probe(grid, x, y, m, n)
                    res += 1
        r.. res

    ___ probe  grid, x, y, m, n
        """
        Probe right and down
        """
        __ x >_ m o. y >_ n:
            r..
        ____ grid[y][x] __ '0':
            r..
        ____
            islands.add((x, y
            probe(grid, x + 1, y, m, n)
            probe(grid, x, y + 1, m, n)


g1 = [
    l..('11000'),
    l..('11000'),
    l..('00100'),
    l..('00011')
]
___ r __ g1:
    print(r)
s = Solution()
print(s.numIslands(g1
print(s.islands)
