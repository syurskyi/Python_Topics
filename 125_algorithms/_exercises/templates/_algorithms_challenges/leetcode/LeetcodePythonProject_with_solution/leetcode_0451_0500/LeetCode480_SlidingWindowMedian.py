'''
Created on Apr 27, 2017

@author: MT
'''
import heapq

class Solution(object):
    ___ medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        pass
    
    
    ___ medianSlidingWindow_another(self, nums, k):
        import bisect
        window = sorted(nums[:k])
        medians = []
        for a, b in zip(nums, nums[k:]+[0]):
            medians.append((window[k/2] + window[~(k/2)]/2.0))
            window.remove(a)
            bisect.insort(window, b)
        return medians
    
    
    ___ __init__(self):
        self.minHeap = []
        self.maxHeap = []
    
    ___ getMedian(self):
        __ not self.maxHeap and not self.minHeap:
            return 0
        __ len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0])/2.0
        else:
            return float(self.minHeap[0])
    
    ___ add(self, num):
        __ not self.maxHeap or num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        __ len(self.maxHeap) > len(self.minHeap):
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        __ len(self.minHeap) > len(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
    
    ___ remove(self, num):
        __ num >= self.getMedian():
            self.minHeap.remove(num)
            heapq.heapify(self.minHeap)
        else:
            self.maxHeap.remove(-num)
            heapq.heapify(self.maxHeap)
        __ len(self.maxHeap) > len(self.minHeap):
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        __ len(self.minHeap) > len(self.maxHeap)+1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
    
    ___ medianSlidingWindow_slow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        n = len(nums) - k + 1
        result = [0.0]*n
        for i in range(len(nums)+1):
            __ i >= k:
                result[i-k] = self.getMedian()
                self.remove(nums[i-k])
            __ i < len(nums):
                self.add(nums[i])
        return result
