'''
Created on May 8, 2017

@author: MT
'''

c_ Solution(object):
    ___ findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        helper(nums, 0, [], res)
        r.. [l..(row) ___ row __ res]
    
    ___ helper(self, nums, ind, curr, res):
        __ l..(curr) >= 2:
            res.add(t..(curr))
        ___ i __ r..(ind, l..(nums)):
            __ i > ind a.. nums[i] __ nums[i-1]:
                _____
            __ n.. curr o. curr[-1] <= nums[i]:
                curr.a..(nums[i])
                helper(nums, i+1, curr, res)
                curr.pop()
    
    ___ test
        testCases = [
            [1, 1, 2, 3, 3],
            [4, 6, 7, 7],
            [4, 3, 2, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = findSubsequences(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
