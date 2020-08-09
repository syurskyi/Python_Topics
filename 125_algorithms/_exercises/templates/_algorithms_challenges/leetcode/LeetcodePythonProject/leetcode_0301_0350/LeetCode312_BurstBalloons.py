'''
Created on Mar 15, 2017

@author: MT
'''

class Solution(object
    ___ maxCoins(self, nums
        nums = [1] + nums + [1]
        n = le.(nums)
        dp = [[0]*n for _ in range(n)]
        for k in range(2, n
            for left in range(n-k
                right = left + k
                for i in range(left+1, right
                    dp[left][right] = max(dp[left][right],\
                        nums[left]*nums[i]*nums[right]+\
                        dp[left][i]+\
                        dp[i][right])
        r_ dp[0][-1]
    
    ___ maxCoinsDnC(self, nums
        nums = [1] + nums + [1]
        n = le.(nums)
        memo = [[0]*n for _ in range(n)]
        r_ self.burst(memo, nums, 0, n-1)
    
    ___ burst(self, memo, nums, left, right
        __ left+1 __ right: r_ 0
        __ memo[left][right] > 0:
            r_ memo[left][right]
        result = 0
        for i in range(left+1, right
            result = max(result,\
                nums[left]*nums[i]*nums[right] + \
                self.burst(memo, nums, left, i) +\
                self.burst(memo, nums, i, right))
            memo[left][right] = result
        r_ result
    
    ___ test(self
        testCases = [
            [3, 1, 5, 8],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.maxCoins(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
