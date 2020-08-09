"""
Premium Question
Manhattan Distance
"""
__author__ = 'Daniel'


class Solution(object
    ___ minTotalDistance_3lines(self, grid
        x = sorted([i ___ i, row in enumerate(grid) ___ v in row __ v __ 1])
        y = sorted([j ___ row in grid ___ j, v in enumerate(row) __ v __ 1])
        r_ su.([abs(x[le.(x)/2]-i)+abs(y[le.(y)/2]-j) ___ i, row in enumerate(grid) ___ j, v in enumerate(row) __ v __ 1])

    ___ minTotalDistance(self, grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = []
        y = []

        m = le.(grid)
        n = le.(grid[0])
        ___ i in xrange(m
            ___ j in xrange(n
                __ grid[i][j] __ 1:
                    x.append(i)
                    y.append(j)

        x.sort()
        y.sort()
        cnt = le.(x)
        point = (x[cnt/2], y[cnt/2])
        ret = 0
        ___ i in xrange(m
            ___ j in xrange(n
                __ grid[i][j] __ 1:
                    ret += abs(point[0]-i)
                    ret += abs(point[1]-j)

        r_ ret


__ __name__ __ "__main__":
    assert Solution().minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]) __ 6