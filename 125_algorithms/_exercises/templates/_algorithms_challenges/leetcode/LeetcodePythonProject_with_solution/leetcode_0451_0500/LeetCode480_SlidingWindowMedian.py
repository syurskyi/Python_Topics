'''
Created on Apr 27, 2017

@author: MT
'''
_______ heapq

c_ Solution(object):
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
    
    
    ___ - ):
        minHeap    # list
        maxHeap    # list
    
    ___ getMedian
        __ n.. maxHeap a.. n.. minHeap:
            r.. 0
        __ l..(minHeap) __ l..(maxHeap):
            r.. (minHeap[0] - maxHeap[0])/2.0
        ____:
            r.. float(minHeap[0])
    
    ___ add(self, num):
        __ n.. maxHeap o. num > -maxHeap[0]:
            heapq.heappush(minHeap, num)
        ____:
            heapq.heappush(maxHeap, -num)
        __ l..(maxHeap) > l..(minHeap):
            val = heapq.heappop(maxHeap)
            heapq.heappush(minHeap, -val)
        __ l..(minHeap) > l..(maxHeap)+1:
            val = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -val)
    
    ___ remove(self, num):
        __ num >= getMedian():
            minHeap.remove(num)
            heapq.heapify(minHeap)
        ____:
            maxHeap.remove(-num)
            heapq.heapify(maxHeap)
        __ l..(maxHeap) > l..(minHeap):
            val = heapq.heappop(maxHeap)
            heapq.heappush(minHeap, -val)
        __ l..(minHeap) > l..(maxHeap)+1:
            val = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -val)
    
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
                result[i-k] = getMedian()
                remove(nums[i-k])
            __ i < l..(nums):
                add(nums[i])
        r.. result
