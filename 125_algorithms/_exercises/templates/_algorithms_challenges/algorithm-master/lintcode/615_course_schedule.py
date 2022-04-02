c_ Solution:
    ___ canFinish  n, P
        """
        :type n: int
        :type P: List[List[int]]
        :rtype: bool
        """
        indeg = [0] * n
        edges = [[] ___ _ __ r..(n)]

        ___ c, p __ P:
            indeg[c] += 1
            edges[p].a..(c)

        queue = [i ___ i __ r..(n) __ indeg[i] __ 0]
        ___ p __ queue:
            ___ c __ edges[p]:
                indeg[c] -= 1
                __ indeg[c] __ 0:
                    queue.a..(c)

        r.. l..(queue) __ n
