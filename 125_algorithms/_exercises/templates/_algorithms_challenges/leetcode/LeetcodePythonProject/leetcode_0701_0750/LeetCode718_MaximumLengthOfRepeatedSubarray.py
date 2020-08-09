'''
Created on Oct 30, 2017

@author: MT
'''
class Solution(object
    ___ findLength(self, A, B
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        nums1, nums2 = A, B
        m, n = le.(nums1), le.(nums2)
        maxLen = 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1
            for j in range(n+1
                __ i __ 0 or j __ 0:
                    dp[i][j] = 0
                ____
                    __ nums1[i-1] __ nums2[j-1]:
                        dp[i][j] = dp[i-1][j-1]+1
                        maxLen = max(maxLen, dp[i][j])
        r_ maxLen
    
    ___ test(self
        testCases = [
            [
                [1,2,3,2,1],
                [3,2,1,4,7],
            ],
            [
                [0,0,0,0,0],
                [0,0,0,0,0]
            ],
            [
                [0,0,0,0,1],
                [1,0,0,0,0],
            ],
        ]
        for nums1, nums2 in testCases:
            print('nums1: %s' % nums1)
            print('nums2: %s' % nums2)
            result = self.findLength(nums1, nums2)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
