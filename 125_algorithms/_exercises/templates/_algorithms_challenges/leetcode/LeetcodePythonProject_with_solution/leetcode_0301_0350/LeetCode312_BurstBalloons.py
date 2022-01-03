'''
Created on Mar 15, 2017

@author: MT
'''

c_ Solution(object):
    ___ maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = l..(nums)
        dp = [[0]*n ___ _ __ r..(n)]
        ___ k __ r..(2, n):
            ___ left __ r..(n-k):
                right = left + k
                ___ i __ r..(left+1, right):
                    dp[left][right] = max(dp[left][right],\
                        nums[left]*nums[i]*nums[right]+\
                        dp[left][i]+\
                        dp[i][right])
        r.. dp[0][-1]
    
    ___ maxCoinsDnC(self, nums):
        nums = [1] + nums + [1]
        n = l..(nums)
        memo = [[0]*n ___ _ __ r..(n)]
        r.. burst(memo, nums, 0, n-1)
    
    ___ burst(self, memo, nums, left, right):
        __ left+1 __ right: r.. 0
        __ memo[left][right] > 0:
            r.. memo[left][right]
        result = 0
        ___ i __ r..(left+1, right):
            result = max(result,\
                nums[left]*nums[i]*nums[right] + \
                burst(memo, nums, left, i) +\
                burst(memo, nums, i, right))
            memo[left][right] = result
        r.. result
    
    ___ test
        testCases = [
            [3, 1, 5, 8],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = maxCoins(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
