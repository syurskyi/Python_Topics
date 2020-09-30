class ConnectingGraph3:
    """
    @param: n: An integer
    """
    ___ __init__(self, n
        __ n < 1:
            r_
        self.nodes = {}
        self.count = n
        ___ i __ range(n
            self.nodes[i + 1] = i + 1

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
            self.nodes[root_a] = root_b
            self.count -= 1

    """
    @return: An integer
    """
    ___ query(self
        r_ self.count
