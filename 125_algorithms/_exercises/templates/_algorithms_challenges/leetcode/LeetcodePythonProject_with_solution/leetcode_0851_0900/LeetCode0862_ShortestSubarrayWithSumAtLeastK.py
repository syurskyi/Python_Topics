'''
Created on Sep 17, 2019

@author: tongq
'''
class Solution(object):
    ___ shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        arr, k = A, K
        n = l..(arr)
        arr2 = [0]*(n+1)
        ___ i __ r..(n):
            arr2[i+1] = arr2[i] + arr[i]
        d    # list
        res = n+1
        ___ i __ r..(n+1):
            w.... d a.. arr2[i] - arr2[d[0]] >= k:
                res = m..(res, i-d.pop(0))
            w.... d a.. arr2[i] <= arr2[d[-1]]:
                d.pop()
            d.a..(i)
        r.. res __ res <= n ____ -1
    
    ___ test(self):
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
        ___ a, k __ testCase:
            res = self.shortestSubarray(a, k)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
