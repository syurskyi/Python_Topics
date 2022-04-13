c_ Solution:
    ___ validTree  n, edges
        """
        :type n: int
        :type edges: list[int]
        :rtype: bool
        """
        __ l..(edges) !_ n - 1:
            r.. F..

        nodes [i ___ i __ r..(n)]

        ___ a, b __ edges:
            _a f.. nodes, a)
            _b f.. nodes, b)

            __ _a __ _b:
                r.. F..

            nodes[_a] _b

        r.. T..

    ___ find  nodes, a
        __ nodes[a] __ a:
            r.. a

        nodes[a] f.. nodes, nodes[a])
        r.. nodes[a]
