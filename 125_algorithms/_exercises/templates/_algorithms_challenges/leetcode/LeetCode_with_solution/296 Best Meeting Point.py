"""
Premium Question
Manhattan Distance
"""
__author__ = 'Daniel'


c_ Solution(o..):
    ___ minTotalDistance_3lines  grid):
        x = s..([i ___ i, row __ e..(grid) ___ v __ row __ v __ 1])
        y = s..([j ___ row __ grid ___ j, v __ e..(row) __ v __ 1])
        r.. s..([abs(x[l..(x)/2]-i)+abs(y[l..(y)/2]-j) ___ i, row __ e..(grid) ___ j, v __ e..(row) __ v __ 1])

    ___ minTotalDistance  grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x    # list
        y    # list

        m = l..(grid)
        n = l..(grid[0])
        ___ i __ x..(m):
            ___ j __ x..(n):
                __ grid[i][j] __ 1:
                    x.a..(i)
                    y.a..(j)

        x.s..()
        y.s..()
        cnt = l..(x)
        point = (x[cnt/2], y[cnt/2])
        ret = 0
        ___ i __ x..(m):
            ___ j __ x..(n):
                __ grid[i][j] __ 1:
                    ret += abs(point[0]-i)
                    ret += abs(point[1]-j)

        r.. ret


__ _______ __ _______
    ... Solution().minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]) __ 6