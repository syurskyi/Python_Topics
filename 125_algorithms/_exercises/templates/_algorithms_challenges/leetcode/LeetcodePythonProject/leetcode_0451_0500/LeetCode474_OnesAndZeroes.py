'''
Created on Apr 26, 2017

@author: MT
'''

class Solution(object
    ___ findMaxForm(self, strs, m, n
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        l = le.(strs)
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(l+1)]
        for i in range(l+1
            nums = [0, 0]
            __ i > 0:
                s = strs[i-1]
                count0 = s.count('0')
                count1 = le.(s)-count0
                nums = [count0, count1]
            for j in range(m+1
                for k in range(n+1
                    __ i __ 0:
                        dp[i][j][k] = 0
                    ____ j >= nums[0] and k >= nums[1]:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-nums[0]][k-nums[1]]+1)
                    ____
                        dp[i][j][k] = dp[i-1][j][k]
        r_ dp[l][m][n]
    
    ___ findMaxForm_slow(self, strs, m, n
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # Knapsack Problem
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            for i in range(m, -1, -1
                for j in range(n, -1, -1
                    count0 = s.count('0')
                    count1 = le.(s)-count0
                    __ i>=count0 and j>=count1:
                        dp[i][j] = max(dp[i][j], dp[i-count0][j-count1]+1)
        r_ dp[-1][-1]
    
    ___ test(self
        testCases = [
            (
                ["10", "0001", "111001", "1", "0"], 5, 3
            ),
            (
                ["10", "0", "1"], 1, 1
            ),
        ]
        for strs, m, n in testCases:
            result = self.findMaxForm(strs, m, n)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
