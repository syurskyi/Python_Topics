'''
Created on Mar 8, 2017

@author: MT
'''

______ heapq
class MedianFinder(object
    ___ __init__(self
        # minHeap save positive values: 7, 9
        self.minHeap = []
        # maxHeap save negative values: -5, -3, -2
        self.maxHeap = []

    ___ addNum(self, num
        __ (not self.minHeap and not self.maxHeap) or num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
            __ le.(self.maxHeap) > le.(self.minHeap) + 1:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        ____
            heapq.heappush(self.minHeap, num)
            __ le.(self.minHeap) > le.(self.maxHeap
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
    
    ___ findMedian(self
        __ le.(self.minHeap) __ le.(self.maxHeap
            r_ (self.minHeap[0] - self.maxHeap[0])/2.0
        ____
            r_ -self.maxHeap[0]
