'''
Created on Apr 11, 2017

@author: MT
'''

c_ Solution(o..
    ___ thirdMax  nums
        first, second, third = f__('-inf'), f__('-inf'), f__('-inf')
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
        r.. third __ third != f__('-inf') ____ first
    
    ___ test
        testCases = [
            [2, 2, 3, 1],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = thirdMax(nums)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
