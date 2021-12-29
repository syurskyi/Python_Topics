'''
Created on May 9, 2017

@author: MT
'''

class Solution(object):
    ___ findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sumVal = sum(nums)
        __ sumVal < S or (sumVal+S)%2 != 0:
            return 0
        target = (sumVal+S)//2
        return self.helper(nums, target)
    
    ___ helper(self, nums, target):
        dp = [0]*(target+1)
        dp[0] = 1
        for num in nums:
            for i in range(target, -1, -1):
                __ i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]
    
    ___ test(self):
        testCases = [
            [
                [1, 1, 1, 1, 1],
                3,
            ],
            [
                [1,2,7,9,981],
                1000000000,
            ],
        ]
        for nums, S in testCases:
            print('nums: %s' % nums)
            print('S: %s' % S)
            result = self.findTargetSumWays(nums, S)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
