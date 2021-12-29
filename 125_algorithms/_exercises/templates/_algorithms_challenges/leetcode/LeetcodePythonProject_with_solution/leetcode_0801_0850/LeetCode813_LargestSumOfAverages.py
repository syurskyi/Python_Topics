'''
Created on Apr 29, 2018

@author: tongq
'''
class Solution(object):
    ___ largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        arr, k = A, K
        n = l..(arr)
        memo = [[0.0]*(n+1) ___ _ __ r..(n+1)]
        cur = 0.0
        ___ i __ r..(n):
            cur += arr[i]
            memo[i+1][1] = cur/(i+1)
        r.. self.search(n, k, arr, memo)
    
    ___ search(self, n, k, arr, memo):
        __ memo[n][k] > 0:
            r.. memo[n][k]
        __ n < k:
            r.. 0
        cur = 0.0
        ___ i __ r..(n-1, -1, -1):
            cur += arr[i]
            memo[n][k] = max(memo[n][k], self.search(i, k-1, arr, memo)+cur/(n-i))
        r.. memo[n][k]
    
    ___ test(self):
        testCases = [
            [
                [9,1,2,3,9],
                3
            ],
        ]
        ___ arr, k __ testCases:
            print('arr: %s' % arr)
            print('k: %s' % k)
            result = self.largestSumOfAverages(arr, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
