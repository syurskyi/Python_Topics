'''
Created on Feb 16, 2017

@author: MT
'''

class Solution(object
    ___ rotate(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = le.(nums)
        k = k % length
        __ k __ 0: r_
        arr = []
        for i0 in range(length
            i = length + i0 - k __ i0<k else i0-k
            arr.append(nums[i])
        for i in range(length
            nums[i] = arr[i]
    
    ___ test(self
        testCases = [
            ([1,2,3,4,5,6,7], 3),
        ]
        for nums, k in testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            self.rotate(nums, k)
            print('after: %s' % (nums))
            print('-='*20+'-')
        
__ __name__ __ '__main__':
    Solution().test()