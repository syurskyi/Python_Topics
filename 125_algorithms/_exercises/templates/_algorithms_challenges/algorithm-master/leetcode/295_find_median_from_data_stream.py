"""
Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(num)
param_2 = obj.findMedian()
"""
import heapq


class MedianFinder:
    ___ __init__(self):
        self.minheap = []
        self.maxheap = []

    ___ addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        __ self.minheap and num < self.minheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

    ___ findMedian(self):
        """
        :rtype: float
        """
        __ not self.minheap:
            return 0.0

        # to handle odd case, it make sure `minheap` has one more child than `maxheap`
        while len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush(self.maxheap, - heapq.heappop(self.minheap))

        # to handle even case, it make sure `minheap` and `maxheap` are same size
        while len(self.maxheap) > len(self.minheap):
            heapq.heappush(self.minheap, - heapq.heappop(self.maxheap))

        __ len(self.minheap) > len(self.maxheap):
            return self.minheap[0] * 1.0

        # since the child in maxheap is negative
        return (self.minheap[0] - self.maxheap[0]) / 2.0
