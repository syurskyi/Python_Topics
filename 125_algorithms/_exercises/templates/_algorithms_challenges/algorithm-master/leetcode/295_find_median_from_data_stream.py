"""
Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(num)
param_2 = obj.findMedian()
"""
_______ heapq


c_ MedianFinder:
    ___ -
        minheap    # list
        maxheap    # list

    ___ addNum  num
        """
        :type num: int
        :rtype: void
        """
        __ minheap a.. num < minheap[0]:
            heapq.heappush(maxheap, -num)
        ____:
            heapq.heappush(minheap, num)

    ___ findMedian
        """
        :rtype: float
        """
        __ n.. minheap:
            r.. 0.0

        # to handle odd case, it make sure `minheap` has one more child than `maxheap`
        w.... l..(minheap) > l..(maxheap) + 1:
            heapq.heappush(maxheap, - heapq.heappop(minheap

        # to handle even case, it make sure `minheap` and `maxheap` are same size
        w.... l..(maxheap) > l..(minheap
            heapq.heappush(minheap, - heapq.heappop(maxheap

        __ l..(minheap) > l..(maxheap
            r.. minheap[0] * 1.0

        # since the child in maxheap is negative
        r.. (minheap[0] - maxheap[0]) / 2.0
