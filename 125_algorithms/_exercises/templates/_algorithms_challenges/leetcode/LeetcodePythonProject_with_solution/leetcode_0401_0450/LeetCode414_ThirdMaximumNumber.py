'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object):
    ___ thirdMax(self, nums):
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        ___ num __ nums:
            __ num > first:
                third = second
                second = first
                first = num
            ____ first > num > second:
                third = second
                second = num
            ____ second > num > third:
                third = num
        r.. third __ third != float('-inf') ____ first
    
    ___ test(self):
        testCases = [
            [2, 2, 3, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.thirdMax(nums)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
