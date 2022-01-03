'''
Created on Aug 20, 2017

@author: MT
'''

c_ Solution(object):
    ___ removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        __ n.. boxes: r.. 0
        n = l..(boxes)
        dp = [[[0]*n ___ _ __ r..(n)] ___ _ __ r..(n)]
        r.. helper(dp, boxes, 0, n-1, 1)
    
    ___ helper(self, dp, boxes, i, j, k):
        __ i > j:
            r.. 0
        ____ i __ j:
            r.. k*k
        ____ dp[i][j][k] != 0:
            r.. dp[i][j][k]
        ____:
            tmp = helper(dp, boxes, i+1, j, 1) + k*k
            ___ m __ r..(i+1, j+1):
                __ boxes[i] __ boxes[m]:
                    tmp = max(tmp, helper(dp, boxes, i+1, m-1, 1)+\
                              helper(dp, boxes, m, j, k+1))
            dp[i][j][k] = tmp
            r.. tmp
    
    ___ test
        testCases = [
            [1, 3, 2, 2, 2, 3, 4, 3, 1],
        ]
        ___ boxes __ testCases:
            print('boxes: %s' % boxes)
            result = removeBoxes(boxes)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
