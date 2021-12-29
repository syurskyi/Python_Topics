'''
Created on Feb 20, 2017

@author: MT
'''
class Solution(object):
    ___ findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        _______ random
        random.shuffle(nums)
        __ k < 1 o. n.. nums:
            r.. 0
        k = l..(nums)-k
        r.. self.helper(nums, 0, l..(nums)-1, k)
    
    ___ helper(self, nums, i, j, k):
        i0, j0 = i, j
        pivot = nums[j]
        while True:
            while i < j and nums[i] < pivot:
                i += 1
            while i < j and nums[j] >= pivot:
                j -= 1
            __ i < j:
                nums[i], nums[j] = nums[j], nums[i]
            ____:
                break
        nums[i], nums[j0] = nums[j0], nums[i]
        __ i __ k:
            r.. nums[i]
        ____ i < k:
            r.. self.helper(nums, i+1, j0, k)
        ____:
            r.. self.helper(nums, i0, i-1, k)
    
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
    
    ___ test(self):
        testCases = [
            ([2, 1], 1),
            ([3,2,1,5,6,4], 5),
            ([3,3,3,3,3,3], 1),
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            result = self.findKthLargest(nums, k)
            print('result: %s' % (result))
            resultHeap = self.findKthLargestHeap(nums, k)
            print('resultHeap: %s' % (resultHeap))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
