'''
Created on Jan 19, 2017

@author: MT
'''
c_ Solution(o..
    ___ permuteUnique  nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        __ n.. nums: r.. []
        __ nums __ []: r.. [[]]
        res    # list
        dfs(s..(nums), [], res)
        r.. res
    
    ___ dfs  nums, curr, res
        __ nums __ []:
            res.a..(l..(curr
            r..
        ___ i, num __ e..(nums
            __ i > 0 a.. nums[i] __ nums[i-1]:
                _____
            curr.a..(num)
            dfs(nums[:i]+nums[i+1:], curr, res)
            curr.p.. )
    
    ___ test
        testCases [
            [1,1,2],
            [3,3,0,3],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result permuteUnique(nums)
            print('result: %s' % result)
            print('-='*15+'-')

__ _____ __ _____
    Solution().test()