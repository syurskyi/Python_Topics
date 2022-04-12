'''
Created on Mar 8, 2017

@author: MT
'''

_______ heapq
c_ MedianFinder(o..
    ___ -
        # minHeap save positive values: 7, 9
        minHeap    # list
        # maxHeap save negative values: -5, -3, -2
        maxHeap    # list

    ___ addNum  num
        __ (n.. minHeap a.. n.. maxHeap) o. num < -maxHeap[0]:
            heapq.heappush(maxHeap, -num)
            __ l..(maxHeap) > l..(minHeap) + 1:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap
        ____
            heapq.heappush(minHeap, num)
            __ l..(minHeap) > l..(maxHeap
                heapq.heappush(maxHeap, -heapq.heappop(minHeap
    
    ___ findMedian
        __ l..(minHeap) __ l..(maxHeap
            r.. (minHeap[0] - maxHeap 0/2.0
        ____
            r.. -maxHeap[0]
