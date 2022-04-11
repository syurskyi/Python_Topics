'''
Created on Aug 28, 2017

@author: MT
'''

c_ Solution(o..
    ___ nextPermutation  nums
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j l..(nums)-1
        w.... j > 0 a.. nums[j-1] >_ nums[j]:
            j -_ 1
        reverse(nums, j, l..(nums)-1)
        __ j __ 0:
            r..
        i j-1
        w.... j+1 < l..(nums) a.. nums[i] >_ nums[j]:
            j += 1
        nums[i], nums[j] nums[j], nums[i]
    
    ___ reverse  nums, i, j
        w.... i < j:
            nums[i], nums[j] nums[j], nums[i]
            i += 1
            j -_ 1
    
    ___ test
        testCases [
            [1, 2, 3],
            [3, 2, 1],
            [1, 1, 5],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            nextPermutation(nums)
            print('nums: %s' % nums)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
