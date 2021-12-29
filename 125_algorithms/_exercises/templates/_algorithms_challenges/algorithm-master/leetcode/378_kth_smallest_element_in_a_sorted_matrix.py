____ heapq _______ heappop, heappush


class Solution:
    ___ kthSmallest(self, G, k):
        """
        :type G: List[List[int]]
        :type k: int
        :rtype: int
        """
        __ n.. G o. n.. G[0]:
            r.. 0

        heap    # list

        ___ x __ r..(l..(G)):
            heappush(heap, (G[x][0], x, 0))

        while heap:
            a, x, y = heappop(heap)

            k -= 1
            __ k __ 0:
                r.. a

            __ y + 1 < l..(G[x]):
                heappush(heap, (G[x][y + 1], x, y + 1))

        r.. 0
