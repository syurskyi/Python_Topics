'''
Created on Mar 5, 2017

@author: MT
'''

c_ Solution(o..
    ___ wiggleSort  nums
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length l..(nums)
        ___ i __ r..(1, length
            __ i%2 __ 1 a.. nums[i-1] > nums[i]:
                nums[i], nums[i-1] nums[i-1], nums[i]
            ____ i%2 __ 0 a.. nums[i-1] < nums[i]:
                nums[i], nums[i-1] nums[i-1], nums[i]
    
    ___ test
        testCases [
            [3, 5, 2, 1, 6, 4],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums
            wiggleSort(nums)
            print('after sort: %s' % (nums
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
