#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
from heapq import *


c.. MedianFinder:
    """According to
    https://leetcode.com/discuss/64850/short-simple-java-c-python-o-log-n-o-1

    keep two heaps (or priority queues):
        1. Max-heap small has the smaller half of the numbers.
        2. Min-heap large has the larger half of the numbers.

    This gives me direct access to the one
    or two middle values (they're the tops of the heaps)
    """
    ___ __init__(self
        self.small, self.large   # list, []
        self.c.. = 0

    ___ addNum  num
        self.c.. += 1
        # Python has no max-heap, so we do some trick here by keep the -num in
        # smaller half, then the max num will be at the top of the heap.
        heappush(self.small, -heappushpop(self.large, num))
        __ self.c.. & 1:
            heappush(self.large, -heappop(self.small))

    ___ findMedian(self
        __ self.c.. & 1:
            r_ float(self.large[0])
        ____
            r_ (self.large[0] - self.small[0]) / 2.0

"""
if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(6)
    print mf.findMedian()
    mf.addNum(10)
    print mf.findMedian()
    mf.addNum(2)
    mf.addNum(6)
    mf.addNum(5)
    print mf.findMedian()
"""
