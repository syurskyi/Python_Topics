'''
Created on Jan 19, 2017

@author: MT
'''
c_ Solution(object):
    ___ permute  nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res    # list
        __ n.. nums: r.. res
        dfs(nums, [], res)
        r.. res
    
    ___ dfs  nums, curr, res):
        __ nums __ []:
            res.a..(l..(curr))
            r..
        ___ i, num __ e..(nums):
            curr.a..(num)
            dfs(nums[:i]+nums[i+1:], curr, res)
            curr.pop()
    
    ___ test
        testCases = [
            [1, 2, 3]
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = permute(nums)
            print('result: %s' % result)
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()