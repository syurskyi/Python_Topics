from heapq ______ heappop, heappush


class Solution:
    ___ findKthLargest(self, A, k
        """
        :type A: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        for a in A:
            heappush(heap, a)
            __ le.(heap) > k:
                heappop(heap)

        r_ heappop(heap)
