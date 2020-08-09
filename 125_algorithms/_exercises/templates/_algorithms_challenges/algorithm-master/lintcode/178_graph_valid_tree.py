class Solution:
    ___ validTree(self, n, edges
        """
        :type n: int
        :type edges: list[int]
        :rtype: bool
        """
        __ le.(edges) != n - 1:
            r_ False

        nodes = [i ___ i in range(n)]

        ___ a, b in edges:
            _a = self.find(nodes, a)
            _b = self.find(nodes, b)

            __ _a is _b:
                r_ False

            nodes[_a] = _b

        r_ True

    ___ find(self, nodes, a
        __ nodes[a] is a:
            r_ a

        nodes[a] = self.find(nodes, nodes[a])
        r_ nodes[a]
