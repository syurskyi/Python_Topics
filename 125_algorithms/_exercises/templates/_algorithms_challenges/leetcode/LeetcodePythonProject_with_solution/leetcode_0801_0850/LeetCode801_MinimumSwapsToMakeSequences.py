'''
Created on Apr 19, 2018

@author: tongq
'''
c_ Solution(object):
    ___ minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        arr1, arr2 = A, B
        n = l..(arr1)
        dp = [[0]*2 ___ _ __ r..(n)]
        dp[-1][0] = 0
        dp[-1][1] = 1
        ___ i __ r..(n-2, -1, -1):
            __ arr1[i] < arr1[i+1] a.. arr2[i] < arr2[i+1]:
                __ arr1[i] < arr2[i+1] a.. arr2[i] < arr1[i+1]:
                    dp[i][0] = m..(dp[i+1][0], dp[i+1][1])
                    dp[i][1] = m..(dp[i+1][0]+1, dp[i+1][0]+1)
                ____:
                    dp[i][0] = dp[i+1][0]
                    dp[i][1] = dp[i+1][1]+1
            ____:
                dp[i][0] = dp[i+1][1]
                dp[i][1] = dp[i+1][0]+1
        r.. m..(dp[0][0], dp[0][1])
    
    # My solution DFS is TLE
    ___ minSwap_own_slow(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        arr1, arr2 = A, B
        res = float('inf')
        helper(arr1, arr2, 0, 0)
        r.. res
        
    ___ helper(self, arr1, arr2, i, cur):
        __ i __ l..(arr1):
            res = m..(res, cur)
            r..
        __ i __ 0 o. (arr1[i] > arr2[i-1] a.. arr2[i] > arr1[i-1]):
            arr1[i], arr2[i] = arr2[i], arr1[i]
            helper(arr1, arr2, i+1, cur+1)
            arr1[i], arr2[i] = arr2[i], arr1[i]
        __ i __ 0 o. (arr1[i] > arr1[i-1] a.. arr2[i] > arr2[i-1]):
            helper(arr1, arr2, i+1, cur)
    
    ___ test
        testCases = [
            [
                [1,3,5,4],
                [1,2,3,7],
            ],
            [
                [3,3,8,9,10],
                [1,7,4,6,8],
            ],
        ]
        ___ arr1, arr2 __ testCases:
            print('arr1: %s' % arr1)
            print('arr2: %s' % arr2)
            result = minSwap(arr1, arr2)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
