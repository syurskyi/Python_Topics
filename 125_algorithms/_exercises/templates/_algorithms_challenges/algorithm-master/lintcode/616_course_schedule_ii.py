class Solution:
    ___ findOrder(self, n, prerequisites
        """
        :type n: int
        :type prerequisites: list[list[int]]
        :rtype: list[int]
        """
        ans = []

        __ not n:
            r_ ans

        indeg = [0] * n
        edges = [[] ___ _ in range(n)]

        ___ c, p in prerequisites:
            indeg[c] += 1
            edges[p].append(c)

        queue = [c ___ c in range(n) __ indeg[c] __ 0]

        ___ p in queue:
            ___ c in edges[p]:
                indeg[c] -= 1

                __ indeg[c] __ 0:
                    queue.append(c)

        __ le.(queue) != n:
            r_ []

        r_ queue
