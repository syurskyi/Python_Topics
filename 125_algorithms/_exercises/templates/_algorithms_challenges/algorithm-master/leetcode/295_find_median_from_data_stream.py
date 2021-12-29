"""
Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(num)
param_2 = obj.findMedian()
"""
_______ heapq


class MedianFinder:
    ___ __init__(self):
        self.minheap    # list
        self.maxheap    # list

    ___ addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        __ self.minheap a.. num < self.minheap[0]:
            heapq.heappush(self.maxheap, -num)
        ____:
            heapq.heappush(self.minheap, num)

    ___ findMedian(self):
        """
        :rtype: float
        """
        __ n.. self.minheap:
            r.. 0.0

        # to handle odd case, it make sure `minheap` has one more child than `maxheap`
        w.... l..(self.minheap) > l..(self.maxheap) + 1:
            heapq.heappush(self.maxheap, - heapq.heappop(self.minheap))

        # to handle even case, it make sure `minheap` and `maxheap` are same size
        w.... l..(self.maxheap) > l..(self.minheap):
            heapq.heappush(self.minheap, - heapq.heappop(self.maxheap))

        __ l..(self.minheap) > l..(self.maxheap):
            r.. self.minheap[0] * 1.0

        # since the child in maxheap is negative
        r.. (self.minheap[0] - self.maxheap[0]) / 2.0
