'''
Created on Apr 4, 2017

@author: MT
'''

class Solution(object):
    ___ maxRotateFunction(self, A):
        nums = A
        sumVal = 0
        sample = 0
        ___ i, num __ enumerate(nums):
            sample += i*num
            sumVal += num
        maxVal = sample
        ___ i __ r..(l..(nums)-1, 0, -1):
            sample = sample+sumVal-l..(nums)*nums[i]
            maxVal = max(maxVal, sample)
        r.. maxVal

    ___ test(self):
        testCases = [
            [4, 3, 2, 6],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = self.maxRotateFunction(nums)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
