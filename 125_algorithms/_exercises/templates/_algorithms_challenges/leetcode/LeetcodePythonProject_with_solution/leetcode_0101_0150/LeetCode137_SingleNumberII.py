'''
Created on Feb 9, 2017

@author: MT
'''

c_ Solution(object):
    ___ singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1, num2 = 0, 0
        ___ num __ nums:
            num2 ^= num1 & num
            num1 ^= num
            mask = ~(num1 & num2)
            num2 &= mask
            num1 &= mask
        r.. num1
    
    ___ test
        testCases = [
            [1, 2, 1, 1, 3, 3, 3],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = singleNumber(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()