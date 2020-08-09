'''
Created on May 6, 2017

@author: MT
'''

class Solution(object
    ___ PredictTheWinner(self, nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = le.(nums)
        dp = [[0]*n ___ _ in range(n)]
        ___ i in range(n
            dp[i][i] = nums[i]
        ___ l in range(1, n
            ___ i in range(n-l
                j = i+l
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        r_ dp[0][n-1] >= 0
    
    ___ PredictTheWinner_DnC(self, nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.mem = {}
        r_ self.helper(nums, 0, le.(nums)-1) >= 0
    
    ___ helper(self, nums, start, end
        n = le.(nums)
        num = start*n+end
        __ num in self.mem:
            r_ self.mem[num]
        __ start __ end:
            self.mem[num] = nums[start]
            r_ self.mem[num]
        res1 = nums[start]-self.helper(nums, start+1, end)
        res2 = nums[end]-self.helper(nums, start, end-1)
        result = max(res1, res2)
        self.mem[num] = result
        r_ result
    
    ___ test(self
        testCases = [
            [1, 5, 2],
            [1, 5, 233, 7],
        ]
        ___ nums in testCases:
            print('nums: %s' % nums)
            result = self.PredictTheWinner_DnC(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
