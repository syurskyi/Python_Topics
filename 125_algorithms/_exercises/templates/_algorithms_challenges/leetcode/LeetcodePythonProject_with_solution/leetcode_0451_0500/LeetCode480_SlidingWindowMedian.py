'''
Created on Apr 27, 2017

@author: MT
'''
_______ heapq

c_ Solution(o..
    ___ medianSlidingWindow  nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        p..
    
    
    ___ medianSlidingWindow_another  nums, k
        _______ b__
        window s..(nums[:k])
        medians    # list
        ___ a, b __ z..(nums, nums[k:]+[0]
            medians.a..((window[k/2] + window[~(k/2)]/2.0
            window.remove(a)
            b__.i.. (window, b)
        r.. medians
    
    
    ___ -
        minHeap    # list
        maxHeap    # list
    
    ___ getMedian
        __ n.. maxHeap a.. n.. minHeap:
            r.. 0
        __ l..(minHeap) __ l..(maxHeap
            r.. (minHeap[0] - maxHeap 0/2.0
        ____
            r.. f__(minHeap 0
    
    ___ add  num
        __ n.. maxHeap o. num > -maxHeap[0]:
            heapq.heappush(minHeap, num)
        ____
            heapq.heappush(maxHeap, -num)
        __ l..(maxHeap) > l..(minHeap
            val heapq.heappop(maxHeap)
            heapq.heappush(minHeap, -val)
        __ l..(minHeap) > l..(maxHeap)+1:
            val heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -val)
    
    ___ remove  num
        __ num >_ getMedian
            minHeap.remove(num)
            heapq.heapify(minHeap)
        ____
            maxHeap.remove(-num)
            heapq.heapify(maxHeap)
        __ l..(maxHeap) > l..(minHeap
            val heapq.heappop(maxHeap)
            heapq.heappush(minHeap, -val)
        __ l..(minHeap) > l..(maxHeap)+1:
            val heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -val)
    
    ___ medianSlidingWindow_slow  nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        n l..(nums) - k + 1
        result [0.0]*n
        ___ i __ r..(l..(nums)+1
            __ i >_ k:
                result[i-k] getMedian()
                remove(nums[i-k])
            __ i < l..(nums
                add(nums[i])
        r.. result
