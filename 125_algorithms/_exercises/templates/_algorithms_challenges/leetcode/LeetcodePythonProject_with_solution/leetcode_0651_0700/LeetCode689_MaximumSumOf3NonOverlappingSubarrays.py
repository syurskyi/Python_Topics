'''
Created on Oct 23, 2017

@author: MT
'''
class Solution(object):
    ___ maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = l..(nums)
        dp = [[0]*(n+1) ___ _ __ r..(4)]
        sumVal = 0
        accu = [0]*(n+1)
        ___ i __ r..(n):
            sumVal += nums[i]
            accu[i] = sumVal
        ids = [[0]*(n+1) ___ _ __ r..(4)]
        ___ i __ r..(1, 4):
            ___ j __ r..(k-1, n):
                tmpMax = accu[j] __ j-k<0 ____ accu[j]-accu[j-k]+dp[i-1][j-k]
                __ j >= k:
                    dp[i][j] = dp[i][j-1]
                    ids[i][j] = ids[i][j-1]
                __ j > 0 and tmpMax > dp[i][j-1]:
                    dp[i][j] = tmpMax
                    ids[i][j] = j-k+1
        res = [0]*3
        res[2] = ids[3][n-1]
        res[1] = ids[2][res[2]-1]
        res[0] = ids[1][res[1]-1]
        r.. res
    
    ___ test(self):
        testCases = [
            [
                [1,2,1,2,6,7,5,1],
                2,
            ],
            [
                [7,13,20,19,19,2,10,1,1,19],
                3,
            ],
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = self.maxSumOfThreeSubarrays(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
