'''
Created on Apr 27, 2017

@author: MT
'''
_______ heapq

class Solution(object):
    ___ medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        pass
    
    
    ___ medianSlidingWindow_another(self, nums, k):
        _______ bisect
        window = s..(nums[:k])
        medians    # list
        ___ a, b __ z..(nums, nums[k:]+[0]):
            medians.a..((window[k/2] + window[~(k/2)]/2.0))
            window.remove(a)
            bisect.insort(window, b)
        r.. medians
    
    
    ___ __init__(self):
        self.minHeap    # list
        self.maxHeap    # list
    
    ___ getMedian(self):
        __ n.. self.maxHeap a.. n.. self.minHeap:
            r.. 0
        __ l..(self.minHeap) __ l..(self.maxHeap):
            r.. (self.minHeap[0] - self.maxHeap[0])/2.0
        ____:
            r.. float(self.minHeap[0])
    
    ___ add(self, num):
        __ n.. self.maxHeap o. num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        ____:
            heapq.heappush(self.maxHeap, -num)
        __ l..(self.maxHeap) > l..(self.minHeap):
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        __ l..(self.minHeap) > l..(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
    
    ___ remove(self, num):
        __ num >= self.getMedian():
            self.minHeap.remove(num)
            heapq.heapify(self.minHeap)
        ____:
            self.maxHeap.remove(-num)
            heapq.heapify(self.maxHeap)
        __ l..(self.maxHeap) > l..(self.minHeap):
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        __ l..(self.minHeap) > l..(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
    
    ___ medianSlidingWindow_slow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        n = l..(nums) - k + 1
        result = [0.0]*n
        ___ i __ r..(l..(nums)+1):
            __ i >= k:
                result[i-k] = self.getMedian()
                self.remove(nums[i-k])
            __ i < l..(nums):
                self.add(nums[i])
        r.. result
