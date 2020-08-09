class Solution:
    ___ canFinish(self, n, P
        """
        :type n: int
        :type P: List[List[int]]
        :rtype: bool
        """
        indeg = [0] * n
        edges = [[] ___ _ in range(n)]

        ___ c, p in P:
            indeg[c] += 1
            edges[p].append(c)

        queue = [i ___ i in range(n) __ indeg[i] __ 0]
        ___ p in queue:
            ___ c in edges[p]:
                indeg[c] -= 1
                __ indeg[c] __ 0:
                    queue.append(c)

        r_ le.(queue) __ n
