'''
Created on Mar 9, 2017

@author: MT
'''

class Solution(object):
    ___ lengthOfLIS(self, nums):
        _______ bisect
        dp = [0]*l..(nums)
        length = 0
        ___ num __ nums:
            i = bisect.bisect_left(dp, num, 0, length)
            dp[i] = num
            __ i __ length:
                length+=1
        print('dp: %s' % dp)
        r.. length
    
    ___ test(self):
        testCases = [
            [10, 9, 2, 5, 3, 7, 101, 18],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = self.lengthOfLIS(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
