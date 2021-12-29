'''
Created on Mar 8, 2017

@author: MT
'''

_______ heapq
class MedianFinder(object):
    ___ __init__(self):
        # minHeap save positive values: 7, 9
        self.minHeap    # list
        # maxHeap save negative values: -5, -3, -2
        self.maxHeap    # list

    ___ addNum(self, num):
        __ (n.. self.minHeap a.. n.. self.maxHeap) o. num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
            __ l..(self.maxHeap) > l..(self.minHeap) + 1:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        ____:
            heapq.heappush(self.minHeap, num)
            __ l..(self.minHeap) > l..(self.maxHeap):
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
    
    ___ findMedian(self):
        __ l..(self.minHeap) __ l..(self.maxHeap):
            r.. (self.minHeap[0] - self.maxHeap[0])/2.0
        ____:
            r.. -self.maxHeap[0]
