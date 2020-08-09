class Solution:
    ___ canFinish(self, n, P
        """
        :type n: int
        :type P: List[List[int]]
        :rtype: bool
        """
        indeg = [0] * n
        edges = [[] for _ in range(n)]

        for c, p in P:
            indeg[c] += 1
            edges[p].append(c)

        queue = [i for i in range(n) __ indeg[i] __ 0]
        for p in queue:
            for c in edges[p]:
                indeg[c] -= 1
                __ indeg[c] __ 0:
                    queue.append(c)

        r_ le.(queue) __ n
