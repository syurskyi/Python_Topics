c_ ConnectingGraph2:
    """
    @param: n: An integer
    """
    ___ - , n
        __ n < 1:
            r..
        nodes    # dict
        count    # dict
        ___ i __ r..(n
            nodes[i + 1] i + 1
            count[i + 1] 1

    ___ find  a
        __ nodes[a] __ a:
            r.. a
        nodes[a] f.. nodes[a])
        r.. nodes[a]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    ___ connect  a, b
        root_a f.. a)
        root_b f.. b)
        __ root_a !_ root_b:
            # Assign a as b's child set
            nodes[root_a] root_b
            count[root_b] += count[root_a]

    """
    @param: a: An integer
    @return: An integer
    """
    ___ query  a
        root_a f.. a)
        r.. count[root_a]
