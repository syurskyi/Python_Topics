'''
Created on Apr 1, 2017

@author: MT
'''

class Solution(object
    ___ combinationSum4(self, nums, target
        __ not nums: r_ 0
        dp = [0]*(target+1)
        dp[0] = 1
        ___ i __ range(target+1
            ___ num __ nums:
                __ i+num <= target:
                    dp[i+num] += dp[i]
        r_ dp[-1]
    
    ___ test(self
        testCases = [
            ([1, 2, 3], 4),
        ]
        ___ nums, target __ testCases:
            print('nums: %s' % (nums))
            print('target: %s' % target)
            result = self.combinationSum4(nums, target)
            print('result: %s' % result)
            print('-='*20+'-')

__  -n __ '__main__':
    Solution().test()

    