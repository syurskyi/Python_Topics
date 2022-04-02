'''
Created on Oct 30, 2017

@author: MT
'''
c_ Solution(o..
    ___ findLength  A, B
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        nums1, nums2 = A, B
        m, n = l..(nums1), l..(nums2)
        maxLen = 0
        dp = [[0]*(n+1) ___ _ __ r..(m+1)]
        ___ i __ r..(m+1
            ___ j __ r..(n+1
                __ i __ 0 o. j __ 0:
                    dp[i][j] = 0
                ____:
                    __ nums1[i-1] __ nums2[j-1]:
                        dp[i][j] = dp[i-1][j-1]+1
                        maxLen = m..(maxLen, dp[i][j])
        r.. maxLen
    
    ___ test
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
        ___ nums1, nums2 __ testCases:
            print('nums1: %s' % nums1)
            print('nums2: %s' % nums2)
            result = findLength(nums1, nums2)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
