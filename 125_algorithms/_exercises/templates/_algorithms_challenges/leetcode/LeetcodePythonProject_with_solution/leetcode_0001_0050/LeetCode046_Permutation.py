'''
Created on Jan 19, 2017

@author: MT
'''
class Solution(object):
    ___ permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res    # list
        __ n.. nums: r.. res
        self.dfs(nums, [], res)
        r.. res
    
    ___ dfs(self, nums, curr, res):
        __ nums __ []:
            res.a..(l..(curr))
            r..
        ___ i, num __ enumerate(nums):
            curr.a..(num)
            self.dfs(nums[:i]+nums[i+1:], curr, res)
            curr.pop()
    
    ___ test(self):
        testCases = [
            [1, 2, 3]
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.permute(nums)
            print('result: %s' % result)
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()