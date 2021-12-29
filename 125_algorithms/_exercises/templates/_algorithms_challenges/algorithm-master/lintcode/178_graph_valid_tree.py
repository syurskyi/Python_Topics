class Solution:
    ___ validTree(self, n, edges):
        """
        :type n: int
        :type edges: list[int]
        :rtype: bool
        """
        __ len(edges) != n - 1:
            return False

        nodes = [i for i in range(n)]

        for a, b in edges:
            _a = self.find(nodes, a)
            _b = self.find(nodes, b)

            __ _a is _b:
                return False

            nodes[_a] = _b

        return True

    ___ find(self, nodes, a):
        __ nodes[a] is a:
            return a

        nodes[a] = self.find(nodes, nodes[a])
        return nodes[a]
