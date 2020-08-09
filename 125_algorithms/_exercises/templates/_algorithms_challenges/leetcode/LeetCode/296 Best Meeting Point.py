"""
Premium Question
Manhattan Distance
"""
__author__ = 'Daniel'


class Solution(object
    ___ minTotalDistance_3lines(self, grid
        x = sorted([i for i, row in enumerate(grid) for v in row __ v __ 1])
        y = sorted([j for row in grid for j, v in enumerate(row) __ v __ 1])
        r_ sum([abs(x[le.(x)/2]-i)+abs(y[le.(y)/2]-j) for i, row in enumerate(grid) for j, v in enumerate(row) __ v __ 1])

    ___ minTotalDistance(self, grid
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = []
        y = []

        m = le.(grid)
        n = le.(grid[0])
        for i in xrange(m
            for j in xrange(n
                __ grid[i][j] __ 1:
                    x.append(i)
                    y.append(j)

        x.sort()
        y.sort()
        cnt = le.(x)
        point = (x[cnt/2], y[cnt/2])
        ret = 0
        for i in xrange(m
            for j in xrange(n
                __ grid[i][j] __ 1:
                    ret += abs(point[0]-i)
                    ret += abs(point[1]-j)

        r_ ret


__ __name__ __ "__main__":
    assert Solution().minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]) __ 6