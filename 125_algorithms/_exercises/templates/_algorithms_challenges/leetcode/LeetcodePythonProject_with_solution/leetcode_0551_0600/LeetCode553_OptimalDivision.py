'''
Created on Aug 23, 2017

@author: MT
'''

class Solution(object):
    ___ optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = '%s' % nums[0]
        for i in range(1, len(nums)):
            __ i == 1 and len(nums) > 2:
                res += '/(%s' % nums[i]
            else:
                res += '/%s' % nums[i]
        __ len(nums) > 2:
            res += ')'
        return res
    
    ___ test(self):
        testCases = [
            [1000,100,10,2],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.optimalDivision(nums)
            print('result: %s' % result)
            print('-='*30+'-')
        
__ __name__ == '__main__':
    Solution().test()
