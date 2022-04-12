'''
Created on Mar 8, 2017

@author: MT
'''

_______ h__
c_ MedianFinder(o..
    ___ -
        # minHeap save positive values: 7, 9
        minHeap    # list
        # maxHeap save negative values: -5, -3, -2
        maxHeap    # list

    ___ addNum  num
        __ (n.. minHeap a.. n.. maxHeap) o. num < -maxHeap[0]:
            h__.heappush(maxHeap, -num)
            __ l..(maxHeap) > l..(minHeap) + 1:
                h__.heappush(minHeap, -h__.heappop(maxHeap
        ____
            h__.heappush(minHeap, num)
            __ l..(minHeap) > l..(maxHeap
                h__.heappush(maxHeap, -h__.heappop(minHeap
    
    ___ findMedian
        __ l..(minHeap) __ l..(maxHeap
            r.. (minHeap[0] - maxHeap 0/2.0
        ____
            r.. -maxHeap[0]
