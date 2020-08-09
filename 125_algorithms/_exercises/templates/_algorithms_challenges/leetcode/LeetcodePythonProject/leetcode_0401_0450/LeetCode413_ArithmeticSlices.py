'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object
    ___ numberOfArithmeticSlices(self, A
        """
        :type A: List[int]
        :rtype: int
        """
        nums = A
        __ not nums or le.(nums) < 3: r_ 0
        res = 0
        curr = 0
        for i in range(2, le.(nums)):
            __ nums[i]-nums[i-1] __ nums[i-1]-nums[i-2]:
                curr += 1
            ____
                curr = 0
            res += curr
        r_ res
    
    ___ test(self
        testCases = [
            [1, 2, 3, 4],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.numberOfArithmeticSlices(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
