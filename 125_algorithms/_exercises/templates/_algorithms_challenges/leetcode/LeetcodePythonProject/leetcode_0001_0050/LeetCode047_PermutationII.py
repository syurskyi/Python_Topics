'''
Created on Jan 19, 2017

@author: MT
'''
class Solution(object
    ___ permuteUnique(self, nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        __ not nums: r_ []
        __ nums __ []: r_ [[]]
        res = []
        self.dfs(sorted(nums), [], res)
        r_ res
    
    ___ dfs(self, nums, curr, res
        __ nums __ []:
            res.append(list(curr))
            r_
        for i, num in enumerate(nums
            __ i > 0 and nums[i] __ nums[i-1]:
                continue
            curr.append(num)
            self.dfs(nums[:i]+nums[i+1:], curr, res)
            curr.pop()
    
    ___ test(self
        testCases = [
            [1,1,2],
            [3,3,0,3],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.permuteUnique(nums)
            print('result: %s' % result)
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()