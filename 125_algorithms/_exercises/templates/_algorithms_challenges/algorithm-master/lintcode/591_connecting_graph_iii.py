c_ ConnectingGraph3:
    """
    @param: n: An integer
    """
    ___ - , n
        __ n < 1:
            r..
        nodes    # dict
        count n
        ___ i __ r..(n
            nodes[i + 1] i + 1

    ___ find  a
        __ nodes[a] __ a:
            r.. a
        nodes[a] find(nodes[a])
        r.. nodes[a]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    ___ connect  a, b
        root_a find(a)
        root_b find(b)
        __ root_a != root_b:
            nodes[root_a] root_b
            count -_ 1

    """
    @return: An integer
    """
    ___ query
        r.. count
