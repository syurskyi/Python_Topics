'''
Created on Feb 19, 2017

@author: MT
'''

c_ Solution(o..
    ___ rob  nums
        __ n.. nums: r.. 0
        __ l..(nums) __ 1: r.. nums[0]
        r.. m..(robHelper(nums, 0, l..(nums)-2),\
                   robHelper(nums, 1, l..(nums)-1
    
    ___ robHelper  nums, lo, hi
        include, exclude = 0, 0
        ___ i0 __ r..(lo, hi+1
            i, e = include, exclude
            include = e+nums[i0]
            exclude = m..(i, e)
        r.. m..(include, exclude)
    
    ___ robSpace  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums: r.. 0
        __ l..(nums) < 2: r.. nums[0]
        dp0 = [0]*l..(nums)
        dp1 = [0]*l..(nums)
        ___ i __ r..(l..(nums)-1
            __ i __ 0:
                dp0[i] = nums[0]
            ____ i __ 1:
                dp0[i] = m..(nums[i], nums[i-1])
            ____:
                dp0[i] = m..(dp0[i-1], dp0[i-2] + nums[i])
        ___ i __ r..(1, l..(nums:
            __ i __ 1:
                dp1[i] = nums[i]
            ____ i __ 2:
                dp1[i] = m..(nums[i], nums[i-1])
            ____:
                dp1[i] = m..(dp1[i-1], dp1[i-2] + nums[i])
        r.. m..(dp0[-2], dp1[-1])
    
    ___ test
        testCases = [
            [1, 1, 1],
#             [1, 1],
            [1, 2, 3, 9],
            [2, 1, 1, 2]
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums
            result = rob(nums)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
