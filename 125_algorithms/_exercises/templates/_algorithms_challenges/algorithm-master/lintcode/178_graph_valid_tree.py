class Solution:
    ___ validTree(self, n, edges):
        """
        :type n: int
        :type edges: list[int]
        :rtype: bool
        """
        __ l..(edges) != n - 1:
            r.. False

        nodes = [i ___ i __ r..(n)]

        ___ a, b __ edges:
            _a = self.find(nodes, a)
            _b = self.find(nodes, b)

            __ _a __ _b:
                r.. False

            nodes[_a] = _b

        r.. True

    ___ find(self, nodes, a):
        __ nodes[a] __ a:
            r.. a

        nodes[a] = self.find(nodes, nodes[a])
        r.. nodes[a]
