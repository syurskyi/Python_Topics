'''
Created on Jan 19, 2017

@author: MT
'''
c_ Solution(object):
    ___ permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        __ n.. nums: r.. []
        __ nums __ []: r.. [[]]
        res    # list
        dfs(s..(nums), [], res)
        r.. res
    
    ___ dfs(self, nums, curr, res):
        __ nums __ []:
            res.a..(l..(curr))
            r..
        ___ i, num __ e..(nums):
            __ i > 0 a.. nums[i] __ nums[i-1]:
                continue
            curr.a..(num)
            dfs(nums[:i]+nums[i+1:], curr, res)
            curr.pop()
    
    ___ test
        testCases = [
            [1,1,2],
            [3,3,0,3],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = permuteUnique(nums)
            print('result: %s' % result)
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()