____ heapq _______ heappop, heappush


c_ Solution:
    ___ findKthLargest  A, k):
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
