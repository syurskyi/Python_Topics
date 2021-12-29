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
        res = []
        __ not nums: return res
        self.dfs(nums, [], res)
        return res
    
    ___ dfs(self, nums, curr, res):
        __ nums == []:
            res.append(list(curr))
            return
        for i, num in enumerate(nums):
            curr.append(num)
            self.dfs(nums[:i]+nums[i+1:], curr, res)
            curr.pop()
    
    ___ test(self):
        testCases = [
            [1, 2, 3]
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.permute(nums)
            print('result: %s' % result)
            print('-='*15+'-')

__ __name__ == '__main__':
    Solution().test()