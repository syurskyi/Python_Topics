'''
Created on Apr 12, 2017

@author: MT
'''

class Solution(object
    ___ canPartition(self, nums
        sumVal = sum(nums)
        __ sumVal%2 != 0:
            r_ False
        target = sumVal//2
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for i in range(target, -1, -1
                __ i-num >= 0 and dp[i-num]:
                    dp[i] = True
        r_ dp[-1]
    
    ___ test(self
        testCases = [
            [1, 2, 5],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.canPartition(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
