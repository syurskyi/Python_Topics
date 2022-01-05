'''
Created on Apr 27, 2017

@author: MT
'''

c_ Solution(o..):
    ___ totalHammingDistance  nums):
        res = 0
        ___ i __ r..(32):
            cnt = 0
            ___ num __ nums:
                __ num & (1 << i):
                    cnt += 1
            res += cnt*(l..(nums)-cnt)
        r.. res
    
    ___ test
        testCases = [
            [4, 14, 2],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = totalHammingDistance(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
