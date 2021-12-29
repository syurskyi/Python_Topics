'''
Created on Apr 1, 2017

@author: MT
'''

class Solution(object):
    ___ combinationSum4(self, nums, target):
        __ not nums: return 0
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(target+1):
            for num in nums:
                __ i+num <= target:
                    dp[i+num] += dp[i]
        return dp[-1]
    
    ___ test(self):
        testCases = [
            ([1, 2, 3], 4),
        ]
        for nums, target in testCases:
            print('nums: %s' % (nums))
            print('target: %s' % target)
            result = self.combinationSum4(nums, target)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()

    