'''
Created on Apr 29, 2018

@author: tongq
'''
class Solution(object
    ___ largestTriangleArea(self, points
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0
        n = le.(points)
        ___ i __ range(n
            ___ j __ range(n
                ___ k __ range(n
                    res = ma.(res, self.getArea(points[i], points[j], points[k]))
        r_ res
    
    ___ getArea(self, p1, p2, p3
        r_ 0.5*abs(p1[0]*p2[1] \
                       +p2[0]*p3[1] \
                       +p3[0]*p1[1] \
                       -p2[0]*p1[1] \
                       -p3[0]*p2[1] \
                       -p1[0]*p3[1])
    
    ___ test(self
        testCases = [
            [[0,0],[0,1],[1,0],[0,2],[2,0]],
            [[4,6],[6,5],[3,1]],
        ]
        ___ points __ testCases:
            print('points: %s' % points)
            result = self.largestTriangleArea(points)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
