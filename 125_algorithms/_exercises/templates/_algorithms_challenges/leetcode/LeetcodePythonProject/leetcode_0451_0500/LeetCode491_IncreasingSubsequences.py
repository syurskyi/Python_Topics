'''
Created on May 8, 2017

@author: MT
'''

class Solution(object
    ___ findSubsequences(self, nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        self.helper(nums, 0, [], res)
        r_ [list(row) for row in res]
    
    ___ helper(self, nums, ind, curr, res
        __ le.(curr) >= 2:
            res.add(tuple(curr))
        for i in range(ind, le.(nums)):
            __ i > ind and nums[i] __ nums[i-1]:
                continue
            __ not curr or curr[-1] <= nums[i]:
                curr.append(nums[i])
                self.helper(nums, i+1, curr, res)
                curr.pop()
    
    ___ test(self
        testCases = [
            [1, 1, 2, 3, 3],
            [4, 6, 7, 7],
            [4, 3, 2, 1],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.findSubsequences(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
