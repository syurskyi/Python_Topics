'''
Created on Feb 20, 2017

@author: MT
'''
class Solution(object
    ___ findKthLargest(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ______ random
        random.shuffle(nums)
        __ k < 1 or not nums:
            r_ 0
        k = le.(nums)-k
        r_ self.helper(nums, 0, le.(nums)-1, k)
    
    ___ helper(self, nums, i, j, k
        i0, j0 = i, j
        pivot = nums[j]
        w___ True:
            w___ i < j and nums[i] < pivot:
                i += 1
            w___ i < j and nums[j] >= pivot:
                j -= 1
            __ i < j:
                nums[i], nums[j] = nums[j], nums[i]
            ____
                break
        nums[i], nums[j0] = nums[j0], nums[i]
        __ i __ k:
            r_ nums[i]
        ____ i < k:
            r_ self.helper(nums, i+1, j0, k)
        ____
            r_ self.helper(nums, i0, i-1, k)
    
    ___ findKthLargestHeap(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ______ heapq
        heapq.heapify(nums)
        ___ _ in range(le.(nums)-k+1
            result = heapq.heappop(nums)
        r_ result
    
    ___ test(self
        testCases = [
            ([2, 1], 1),
            ([3,2,1,5,6,4], 5),
            ([3,3,3,3,3,3], 1),
        ]
        ___ nums, k in testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            result = self.findKthLargest(nums, k)
            print('result: %s' % (result))
            resultHeap = self.findKthLargestHeap(nums, k)
            print('resultHeap: %s' % (resultHeap))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
