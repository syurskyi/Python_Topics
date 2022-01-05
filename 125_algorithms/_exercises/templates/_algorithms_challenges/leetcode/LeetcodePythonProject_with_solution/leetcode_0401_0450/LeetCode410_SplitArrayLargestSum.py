'''
Created on Apr 10, 2017

@author: MT
'''

c_ Solution(object):
    ___ splitArray  nums, m):
        left, right = 0, 0
        ___ num __ nums:
            left = m..(left, num)
            right += num
        w.... left < right:
            mid = (left+right)//2
            __ doable(nums, m-1, mid):
                right = mid
            ____:
                left = mid+1
        r.. left
    
    ___ doable  nums, cuts, maxVal):
        acc = 0
        ___ num __ nums:
            __ num > maxVal:
                r.. F..
            ____ acc+num <= maxVal:
                acc += num
            ____:
                cuts -= 1
                acc = num
                __ cuts < 0:
                    r.. F..
        r.. T..
    
    ___ test
        testCases = [
            [
                [7,2,5,10,8],
                2,
            ],
        ]
        ___ nums, m __ testCases:
            print('nums: %s' % nums)
            print('m: %s' % m)
            result = splitArray(nums, m)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
