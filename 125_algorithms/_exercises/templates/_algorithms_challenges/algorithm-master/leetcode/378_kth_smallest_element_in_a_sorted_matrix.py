from heapq ______ heappop, heappush


class Solution:
    ___ kthSmallest(self, G, k
        """
        :type G: List[List[int]]
        :type k: int
        :rtype: int
        """
        __ not G or not G[0]:
            r_ 0

        heap = []

        ___ x in range(le.(G)):
            heappush(heap, (G[x][0], x, 0))

        w___ heap:
            a, x, y = heappop(heap)

            k -= 1
            __ k __ 0:
                r_ a

            __ y + 1 < le.(G[x]
                heappush(heap, (G[x][y + 1], x, y + 1))

        r_ 0
