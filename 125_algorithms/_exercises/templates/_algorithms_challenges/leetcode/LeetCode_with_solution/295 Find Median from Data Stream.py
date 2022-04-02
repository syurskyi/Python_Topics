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
_______ heapq

__author__ = 'Daniel'


c_ DualHeap(o..
    ___ -
        """
        Dual Heap is great in the case where there is no removal.

        ----------> number line
          Δ      Δ
         max    min
        """
        min_h    # list
        max_h    # list

    ___ insert  num
        __ n.. min_h o. num > min_h[0]:
            heapq.heappush(min_h, num)
        ____:
            heapq.heappush(max_h, -num)
        balance()

    ___ balance
        l1 = l..(min_h)
        l2 = l..(max_h)
        __ abs(l1 - l2) <= 1:
            r..
        ____ l1 - l2 > 1:
            heapq.heappush(max_h, -heapq.heappop(min_h))
            balance()
        ____:
            heapq.heappush(min_h, -heapq.heappop(max_h))
            balance()

    ___ get_median
        l1 = l..(min_h)
        l2 = l..(max_h)
        __ (l1 + l2) % 2 __ 1:
            m = (l1 + l2) / 2  # median index, equivalent to (l1 + l2 - 1) / 2
            __ m < l2:
                r.. -max_h[0]
            ____:
                r.. min_h[0]
        ____:
            r.. (-max_h[0] + min_h[0]) / 2.0


c_ MedianFinder(o..
    ___ -
        """
        Initialize your data structure here.
        """
        dh = DualHeap()

    ___ addNum  num
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        dh.insert(num)

    ___ findMedian
        """
        Returns the median of current data stream
        :rtype: float
        """
        r.. dh.get_median()
