'''
Created on Apr 4, 2017

@author: MT
'''

c_ Solution(o..):
    ___ maxRotateFunction  A):
        nums = A
        sumVal = 0
        sample = 0
        ___ i, num __ e..(nums):
            sample += i*num
            sumVal += num
        maxVal = sample
        ___ i __ r..(l..(nums)-1, 0, -1):
            sample = sample+sumVal-l..(nums)*nums[i]
            maxVal = m..(maxVal, sample)
        r.. maxVal

    ___ test
        testCases = [
            [4, 3, 2, 6],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = maxRotateFunction(nums)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
