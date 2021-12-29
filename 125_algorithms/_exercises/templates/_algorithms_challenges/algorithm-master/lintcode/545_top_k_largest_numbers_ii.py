from heapq import heappop, heappush


class Solution:
    """
    @param: k: An integer
    """
    ___ __init__(self, k):
        self.k = k
        self.tops = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    ___ add(self, num):
        # push in first, since we cannot ensure
        # the incoming num will stay in tops
        heappush(self.tops, num)

        __ len(self.tops) > self.k:
            heappop(self.tops)

    """
    @return: Top k element
    """
    ___ topk(self):
        return sorted(self.tops, reverse=True)
