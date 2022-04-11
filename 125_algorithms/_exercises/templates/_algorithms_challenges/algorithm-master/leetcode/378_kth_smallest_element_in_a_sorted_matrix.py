____ heapq _______ heappop, heappush


c_ Solution:
    ___ kthSmallest  G, k
        """
        :type G: List[List[int]]
        :type k: int
        :rtype: int
        """
        __ n.. G o. n.. G[0]:
            r.. 0

        heap    # list

        ___ x __ r..(l..(G:
            heappush(heap, (G[x][0], x, 0

        w.... heap:
            a, x, y heappop(heap)

            k -_ 1
            __ k __ 0:
                r.. a

            __ y + 1 < l..(G[x]
                heappush(heap, (G[x][y + 1], x, y + 1

        r.. 0
