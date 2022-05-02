'''
Created on May 8, 2017

@author: MT
'''

c_ Solution(o..
    ___ findSubsequences  nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res s..()
        helper(nums, 0,    # list, res)
        r.. [l..(row) ___ row __ res]
    
    ___ helper  nums, ind, curr, res
        __ l..(curr) >_ 2:
            res.add(t..(curr
        ___ i __ r..(ind, l..(nums:
            __ i > ind a.. nums[i] __ nums[i-1]:
                _____
            __ n.. curr o. curr[-1] <_ nums[i]:
                curr.a..(nums[i])
                helper(nums, i+1, curr, res)
                curr.p.. )
    
    ___ test
        testCases [
            [1, 1, 2, 3, 3],
            [4, 6, 7, 7],
            [4, 3, 2, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result findSubsequences(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
