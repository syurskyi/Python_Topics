'''
Created on Feb 20, 2017

@author: MT
'''
c_ Solution(object):
    ___ findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        _______ r__
        r__.shuffle(nums)
        __ k < 1 o. n.. nums:
            r.. 0
        k = l..(nums)-k
        r.. helper(nums, 0, l..(nums)-1, k)
    
    ___ helper(self, nums, i, j, k):
        i0, j0 = i, j
        pivot = nums[j]
        w... T...
            w.... i < j a.. nums[i] < pivot:
                i += 1
            w.... i < j a.. nums[j] >= pivot:
                j -= 1
            __ i < j:
                nums[i], nums[j] = nums[j], nums[i]
            ____:
                break
        nums[i], nums[j0] = nums[j0], nums[i]
        __ i __ k:
            r.. nums[i]
        ____ i < k:
            r.. helper(nums, i+1, j0, k)
        ____:
            r.. helper(nums, i0, i-1, k)
    
    ___ findKthLargestHeap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        _______ heapq
        heapq.heapify(nums)
        ___ _ __ r..(l..(nums)-k+1):
            result = heapq.heappop(nums)
        r.. result
    
    ___ test
        testCases = [
            ([2, 1], 1),
            ([3,2,1,5,6,4], 5),
            ([3,3,3,3,3,3], 1),
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            result = findKthLargest(nums, k)
            print('result: %s' % (result))
            resultHeap = findKthLargestHeap(nums, k)
            print('resultHeap: %s' % (resultHeap))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
