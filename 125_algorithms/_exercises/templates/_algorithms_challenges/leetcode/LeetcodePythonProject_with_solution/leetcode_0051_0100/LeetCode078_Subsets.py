'''
Created on Jan 24, 2017

@author: MT
'''

c_ Solution(o..
    ___ subsets  nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        __ n.. nums:
            r.. []
        result    # list
        elem    # list
        helper(nums, elem, 0, result)
        r.. result
    
    ___ helper  nums, elem, start, result
        result.a..(l..(elem
        ___ i __ r..(start, l..(nums:
            elem.a..(nums[i])
            helper(nums, elem, i+1, result)
            elem.pop()
    
    ___ test
        testCases = [
            [1, 2, 3],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums
            result = subsets(nums)
            print('result: %s' % (result
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()
