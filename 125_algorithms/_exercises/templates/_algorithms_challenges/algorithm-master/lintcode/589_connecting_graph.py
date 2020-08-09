class ConnectingGraph:
    """
    @param: n: An integer
    """
    ___ __init__(self, n
        __ not n:
            r_

        self.N = {}
        for i in range(1, n + 1
            self.N[i] = i

    ___ find(self, a
        __ self.N[a] __ a:
            r_ a

        self.N[a] = self.find(self.N[a])
        r_ self.N[a]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    ___ connect(self, a, b
        _a = self.find(a)
        _b = self.find(b)
        __ _a != _b:
            self.N[_a] = _b

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    ___ query(self, a, b
        _a = self.find(a)
        _b = self.find(b)
        r_ _a __ _b
