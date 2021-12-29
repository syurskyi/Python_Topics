____ heapq _______ heappop, heappush


class Solution:
    ___ findKthLargest(self, A, k):
        """
        :type A: List[int]
        :type k: int
        :rtype: int
        """
        heap    # list

        ___ a __ A:
            heappush(heap, a)
            __ l..(heap) > k:
                heappop(heap)

        r.. heappop(heap)
