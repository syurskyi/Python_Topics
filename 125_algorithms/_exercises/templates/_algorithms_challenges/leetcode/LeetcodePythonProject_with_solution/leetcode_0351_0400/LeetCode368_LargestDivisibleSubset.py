'''
Created on Mar 28, 2017

@author: MT
'''

class Solution(object):
    ___ largestDivisibleSubset(self, nums):
        __ n.. nums: r.. []
        nums.sort()
        n = l..(nums)
        idx = [-1]*n
        dp = [1]*n
        maxLen = 0
        maxInd = 0
        ___ i __ r..(n):
            ___ j __ r..(i-1, -1, -1):
                __ nums[i]%nums[j] __ 0:
                    __ dp[i]<dp[j]+1:
                        dp[i] = dp[j]+1
                        idx[i] = j
            __ dp[i] > maxLen:
                maxLen = dp[i]
                maxInd = i
        ind = maxInd
        res    # list
        while ind != -1:
            res.insert(0, nums[ind])
            ind = idx[ind]
        r.. res
    
    ___ test(self):
        testCases = [
            [1, 2, 3],
            [1, 2, 3, 8],
            [1, 2, 4, 8],
            [5, 7],
            [4, 8, 10, 240],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.largestDivisibleSubset(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
