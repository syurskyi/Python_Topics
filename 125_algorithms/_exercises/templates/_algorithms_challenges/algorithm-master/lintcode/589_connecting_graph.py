c_ ConnectingGraph:
    """
    @param: n: An integer
    """
    ___ - , n):
        __ n.. n:
            r..

        N    # dict
        ___ i __ r..(1, n + 1):
            N[i] = i

    ___ find  a):
        __ N[a] __ a:
            r.. a

        N[a] = find(N[a])
        r.. N[a]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    ___ connect  a, b):
        _a = find(a)
        _b = find(b)
        __ _a != _b:
            N[_a] = _b

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    ___ query  a, b):
        _a = find(a)
        _b = find(b)
        r.. _a __ _b
