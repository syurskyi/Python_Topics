'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object):
    ___ thirdMax(self, nums):
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            __ num > first:
                third = second
                second = first
                first = num
            elif first > num > second:
                third = second
                second = num
            elif second > num > third:
                third = num
        return third __ third != float('-inf') else first
    
    ___ test(self):
        testCases = [
            [2, 2, 3, 1],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.thirdMax(nums)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()
