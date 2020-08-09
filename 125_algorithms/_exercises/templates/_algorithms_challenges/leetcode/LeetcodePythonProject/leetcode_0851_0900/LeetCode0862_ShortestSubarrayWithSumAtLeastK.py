'''
Created on Sep 17, 2019

@author: tongq
'''
class Solution(object
    ___ shortestSubarray(self, A, K
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        arr, k = A, K
        n = le.(arr)
        arr2 = [0]*(n+1)
        ___ i in range(n
            arr2[i+1] = arr2[i] + arr[i]
        d = []
        res = n+1
        ___ i in range(n+1
            w___ d and arr2[i] - arr2[d[0]] >= k:
                res = min(res, i-d.pop(0))
            w___ d and arr2[i] <= arr2[d[-1]]:
                d.pop()
            d.append(i)
        r_ res __ res <= n else -1
    
    ___ test(self
        testCase = [
            [
                [56,-21,56,35,-9],
                61,
            ],
#             [
#                 [84,-37,32,40,95],
#                 167,
#             ],
#             [
#                 [1],
#                 1,
#             ],
#             [
#                 [1,2],
#                 4
#             ],
#             [
#                 [2,-1,2],
#                 3
#             ],
#             [
#                 [77,19,35,10,-14],
#                 19
#             ],
#             [
#                 [-3, 4, 1],
#                 5,
#             ],
        ]
        ___ a, k in testCase:
            res = self.shortestSubarray(a, k)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
