____ heapq _______ heappush, heappop


class Solution:
    """
    @param A: the numbers
    @return: the minimum cost
    """
    ___ mergeNumber(self, A):
        ans = 0
        __ n.. A:
            r.. ans

        heap    # list

        ___ a __ A:
            heappush(heap, a)

        while l..(heap) > 1:
            _sum = heappop(heap) + heappop(heap)
            ans += _sum
            heappush(heap, _sum)

        r.. ans
