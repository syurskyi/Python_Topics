'''
Created on Aug 20, 2017

@author: MT
'''

class Solution(object
    ___ removeBoxes(self, boxes
        """
        :type boxes: List[int]
        :rtype: int
        """
        __ not boxes: r_ 0
        n = le.(boxes)
        dp = [[[0]*n ___ _ in range(n)] ___ _ in range(n)]
        r_ self.helper(dp, boxes, 0, n-1, 1)
    
    ___ helper(self, dp, boxes, i, j, k
        __ i > j:
            r_ 0
        ____ i __ j:
            r_ k*k
        ____ dp[i][j][k] != 0:
            r_ dp[i][j][k]
        ____
            tmp = self.helper(dp, boxes, i+1, j, 1) + k*k
            ___ m in range(i+1, j+1
                __ boxes[i] __ boxes[m]:
                    tmp = max(tmp, self.helper(dp, boxes, i+1, m-1, 1)+\
                              self.helper(dp, boxes, m, j, k+1))
            dp[i][j][k] = tmp
            r_ tmp
    
    ___ test(self
        testCases = [
            [1, 3, 2, 2, 2, 3, 4, 3, 1],
        ]
        ___ boxes in testCases:
            print('boxes: %s' % boxes)
            result = self.removeBoxes(boxes)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
