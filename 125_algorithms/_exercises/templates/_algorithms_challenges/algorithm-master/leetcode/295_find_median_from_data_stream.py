"""
Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(num)
param_2 = obj.findMedian()
"""
_______ h__


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
            h__.heappush(maxheap, -num)
        ____
            h__.heappush(minheap, num)

    ___ findMedian
        """
        :rtype: float
        """
        __ n.. minheap:
            r.. 0.0

        # to handle odd case, it make sure `minheap` has one more child than `maxheap`
        w.... l..(minheap) > l..(maxheap) + 1:
            h__.heappush(maxheap, - h__.heappop(minheap

        # to handle even case, it make sure `minheap` and `maxheap` are same size
        w.... l..(maxheap) > l..(minheap
            h__.heappush(minheap, - h__.heappop(maxheap

        __ l..(minheap) > l..(maxheap
            r.. minheap[0] * 1.0

        # since the child in maxheap is negative
        r.. (minheap[0] - maxheap 0 / 2.0
