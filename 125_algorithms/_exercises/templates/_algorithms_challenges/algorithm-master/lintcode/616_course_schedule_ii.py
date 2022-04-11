c_ Solution:
    ___ findOrder  n, prerequisites
        """
        :type n: int
        :type prerequisites: list[list[int]]
        :rtype: list[int]
        """
        ans    # list

        __ n.. n:
            r.. ans

        indeg [0] * n
        edges [[] ___ _ __ r..(n)]

        ___ c, p __ prerequisites:
            indeg[c] += 1
            edges[p].a..(c)

        queue [c ___ c __ r..(n) __ indeg[c] __ 0]

        ___ p __ queue:
            ___ c __ edges[p]:
                indeg[c] -_ 1

                __ indeg[c] __ 0:
                    queue.a..(c)

        __ l..(queue) != n:
            r.. []

        r.. queue
