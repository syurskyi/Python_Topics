"""
Premium Question
"""
____ c.. _______ n..

__author__ 'Daniel'


c_ UnionFind(o..
    """
    Weighted Union Find with path compression
    """
    ___ - , rows, cols
        # hashing will cause TLE; use direct array access instead
        pi [-1 ___ _ __ x..(rows*cols)]  # item -> pi
        sz [-1 ___ _ __ x..(rows*cols)]  # root -> size
        count 0

    ___ add  item
        __ pi[item] __ -1:
            pi[item] item
            sz[item] 1
            count += 1

    ___ union  a, b
        pi1 _pi(a)
        pi2 _pi(b)

        __ pi1 != pi2:
            __ sz[pi1] > sz[pi2]:
                pi1, pi2 pi2, pi1

            pi[pi1] pi2
            sz[pi2] += sz[pi1]
            count -_ 1

    ___ _pi  item
        """
        Get root with path compression
        """
        pi pi[item]
        __ item != pi:
            pi[item] _pi(pi)

        r.. pi[item]


Op n..('Op', 'r c')  # row col


c_ Solution:
    ___ -
        dirs ((-1, 0), (1, 0), (0, -1), (0, 1

    ___ numIslands2  n, m, operators
        rows n
        cols m
        unroll l.... x, y: x*cols + y  # hash will be slower
        mat [[0 ___ _ __ x..(cols)] ___ _ __ x..(rows)]
        uf UnionFind(rows, cols)
        ret    # list
        ___ op __ operators:
            op Op(r=op[0], c=op[1])
            uf.add(unroll(op.r, op.c
            mat[op.r][op.c] 1
            ___ dir __ dirs:
                x1 op.r+dir[0]
                y1 op.c+dir[1]
                __ 0 <_ x1 < rows a.. 0 <_ y1 < cols a.. mat[x1][y1] __ 1:
                    uf.union(unroll(op.r, op.c), unroll(x1, y1

            ret.a..(uf.count)

        r.. ret