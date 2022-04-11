'''
Created on Feb 16, 2017

@author: MT
'''

c_ Solution(o..
    ___ rotate  nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length l..(nums)
        k k % length
        __ k __ 0: r..
        arr    # list
        ___ i0 __ r..(length
            i length + i0 - k __ i0<k ____ i0-k
            arr.a..(nums[i])
        ___ i __ r..(length
            nums[i] arr[i]
    
    ___ test
        testCases [
            ([1,2,3,4,5,6,7], 3),
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % (nums
            print('k: %s' % (k
            rotate(nums, k)
            print('after: %s' % (nums
            print('-='*20+'-')
        
__ _____ __ _____
    Solution().test()