____ heapq _______ heappush, heappop


c_ Solution:
    """
    @param A: the numbers
    @return: the minimum cost
    """
    ___ mergeNumber  A):
        ans = 0
        __ n.. A:
            r.. ans

        heap    # list

        ___ a __ A:
            heappush(heap, a)

        w.... l..(heap) > 1:
            _sum = heappop(heap) + heappop(heap)
            ans += _sum
            heappush(heap, _sum)

        r.. ans
