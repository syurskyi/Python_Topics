class ConnectingGraph2:
    """
    @param: n: An integer
    """
    ___ __init__(self, n
        __ n < 1:
            r_
        self.nodes = {}
        self.count = {}
        ___ i in range(n
            self.nodes[i + 1] = i + 1
            self.count[i + 1] = 1

    ___ find(self, a
        __ self.nodes[a] __ a:
            r_ a
        self.nodes[a] = self.find(self.nodes[a])
        r_ self.nodes[a]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    ___ connect(self, a, b
        root_a = self.find(a)
        root_b = self.find(b)
        __ root_a != root_b:
            # Assign a as b's child set
            self.nodes[root_a] = root_b
            self.count[root_b] += self.count[root_a]

    """
    @param: a: An integer
    @return: An integer
    """
    ___ query(self, a
        root_a = self.find(a)
        r_ self.count[root_a]
