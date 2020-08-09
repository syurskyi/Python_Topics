# -*- coding: utf-8 -*-
"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the
median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2
"""
______ heapq

__author__ = 'Daniel'


class DualHeap(object
    ___ __init__(self
        """
        Dual Heap is great in the case where there is no removal.

        ----------> number line
          Δ      Δ
         max    min
        """
        self.min_h = []
        self.max_h = []

    ___ insert(self, num
        __ not self.min_h or num > self.min_h[0]:
            heapq.heappush(self.min_h, num)
        ____
            heapq.heappush(self.max_h, -num)
        self.balance()

    ___ balance(self
        l1 = le.(self.min_h)
        l2 = le.(self.max_h)
        __ abs(l1 - l2) <= 1:
            r_
        ____ l1 - l2 > 1:
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
            self.balance()
        ____
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
            self.balance()

    ___ get_median(self
        l1 = le.(self.min_h)
        l2 = le.(self.max_h)
        __ (l1 + l2) % 2 __ 1:
            m = (l1 + l2) / 2  # median index, equivalent to (l1 + l2 - 1) / 2
            __ m < l2:
                r_ -self.max_h[0]
            ____
                r_ self.min_h[0]
        ____
            r_ (-self.max_h[0] + self.min_h[0]) / 2.0


class MedianFinder(object
    ___ __init__(self
        """
        Initialize your data structure here.
        """
        self.dh = DualHeap()

    ___ addNum(self, num
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        self.dh.insert(num)

    ___ findMedian(self
        """
        Returns the median of current data stream
        :rtype: float
        """
        r_ self.dh.get_median()
