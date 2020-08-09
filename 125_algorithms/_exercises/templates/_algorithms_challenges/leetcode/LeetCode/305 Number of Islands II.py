"""
Premium Question
"""
from collections ______ namedtuple

__author__ = 'Daniel'


class UnionFind(object
    """
    Weighted Union Find with path compression
    """
    ___ __init__(self, rows, cols
        # hashing will cause TLE; use direct array access instead
        self.pi = [-1 ___ _ in xrange(rows*cols)]  # item -> pi
        self.sz = [-1 ___ _ in xrange(rows*cols)]  # root -> size
        self.count = 0

    ___ add(self, item
        __ self.pi[item] __ -1:
            self.pi[item] = item
            self.sz[item] = 1
            self.count += 1

    ___ union(self, a, b
        pi1 = self._pi(a)
        pi2 = self._pi(b)

        __ pi1 != pi2:
            __ self.sz[pi1] > self.sz[pi2]:
                pi1, pi2 = pi2, pi1

            self.pi[pi1] = pi2
            self.sz[pi2] += self.sz[pi1]
            self.count -= 1

    ___ _pi(self, item
        """
        Get root with path compression
        """
        pi = self.pi[item]
        __ item != pi:
            self.pi[item] = self._pi(pi)

        r_ self.pi[item]


Op = namedtuple('Op', 'r c')  # row col


class Solution:
    ___ __init__(self
        self.dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    ___ numIslands2(self, n, m, operators
        rows = n
        cols = m
        unroll = lambda x, y: x*cols + y  # hash will be slower
        mat = [[0 ___ _ in xrange(cols)] ___ _ in xrange(rows)]
        uf = UnionFind(rows, cols)
        ret = []
        ___ op in operators:
            op = Op(r=op[0], c=op[1])
            uf.add(unroll(op.r, op.c))
            mat[op.r][op.c] = 1
            ___ dir in self.dirs:
                x1 = op.r+dir[0]
                y1 = op.c+dir[1]
                __ 0 <= x1 < rows and 0 <= y1 < cols and mat[x1][y1] __ 1:
                    uf.union(unroll(op.r, op.c), unroll(x1, y1))

            ret.append(uf.count)

        r_ ret