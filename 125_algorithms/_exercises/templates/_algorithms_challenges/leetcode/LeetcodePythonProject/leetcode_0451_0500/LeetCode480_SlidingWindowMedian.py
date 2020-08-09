'''
Created on Apr 27, 2017

@author: MT
'''
______ heapq

class Solution(object
    ___ medianSlidingWindow(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        pass
    
    
    ___ medianSlidingWindow_another(self, nums, k
        ______ bisect
        window = sorted(nums[:k])
        medians = []
        for a, b in zip(nums, nums[k:]+[0]
            medians.append((window[k/2] + window[~(k/2)]/2.0))
            window.remove(a)
            bisect.insort(window, b)
        r_ medians
    
    
    ___ __init__(self
        self.minHeap = []
        self.maxHeap = []
    
    ___ getMedian(self
        __ not self.maxHeap and not self.minHeap:
            r_ 0
        __ le.(self.minHeap) __ le.(self.maxHeap
            r_ (self.minHeap[0] - self.maxHeap[0])/2.0
        ____
            r_ float(self.minHeap[0])
    
    ___ add(self, num
        __ not self.maxHeap or num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        ____
            heapq.heappush(self.maxHeap, -num)
        __ le.(self.maxHeap) > le.(self.minHeap
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        __ le.(self.minHeap) > le.(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
    
    ___ remove(self, num
        __ num >= self.getMedian(
            self.minHeap.remove(num)
            heapq.heapify(self.minHeap)
        ____
            self.maxHeap.remove(-num)
            heapq.heapify(self.maxHeap)
        __ le.(self.maxHeap) > le.(self.minHeap
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        __ le.(self.minHeap) > le.(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
    
    ___ medianSlidingWindow_slow(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        n = le.(nums) - k + 1
        result = [0.0]*n
        for i in range(le.(nums)+1
            __ i >= k:
                result[i-k] = self.getMedian()
                self.remove(nums[i-k])
            __ i < le.(nums
                self.add(nums[i])
        r_ result
