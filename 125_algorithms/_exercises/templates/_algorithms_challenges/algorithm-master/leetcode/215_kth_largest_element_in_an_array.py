from heapq import heappop, heappush


class Solution:
    ___ findKthLargest(self, A, k):
        """
        :type A: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        for a in A:
            heappush(heap, a)
            __ len(heap) > k:
                heappop(heap)

        return heappop(heap)
