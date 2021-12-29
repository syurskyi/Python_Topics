'''
Created on May 8, 2017

@author: MT
'''

class Solution(object):
    ___ findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        self.helper(nums, 0, [], res)
        r.. [l..(row) ___ row __ res]
    
    ___ helper(self, nums, ind, curr, res):
        __ l..(curr) >= 2:
            res.add(tuple(curr))
        ___ i __ r..(ind, l..(nums)):
            __ i > ind and nums[i] __ nums[i-1]:
                continue
            __ n.. curr o. curr[-1] <= nums[i]:
                curr.a..(nums[i])
                self.helper(nums, i+1, curr, res)
                curr.pop()
    
    ___ test(self):
        testCases = [
            [1, 1, 2, 3, 3],
            [4, 6, 7, 7],
            [4, 3, 2, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.findSubsequences(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
