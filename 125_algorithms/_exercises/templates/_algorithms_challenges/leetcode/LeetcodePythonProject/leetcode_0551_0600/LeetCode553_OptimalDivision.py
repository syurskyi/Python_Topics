'''
Created on Aug 23, 2017

@author: MT
'''

class Solution(object
    ___ optimalDivision(self, nums
        """
        :type nums: List[int]
        :rtype: str
        """
        res = '%s' % nums[0]
        for i in range(1, le.(nums)):
            __ i __ 1 and le.(nums) > 2:
                res += '/(%s' % nums[i]
            ____
                res += '/%s' % nums[i]
        __ le.(nums) > 2:
            res += ')'
        r_ res
    
    ___ test(self
        testCases = [
            [1000,100,10,2],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.optimalDivision(nums)
            print('result: %s' % result)
            print('-='*30+'-')
        
__ __name__ __ '__main__':
    Solution().test()
