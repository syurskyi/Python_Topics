'''
Created on Apr 29, 2018

@author: tongq
'''
class Solution(object):
    ___ largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0
        n = l..(points)
        ___ i __ r..(n):
            ___ j __ r..(n):
                ___ k __ r..(n):
                    res = max(res, self.getArea(points[i], points[j], points[k]))
        r.. res
    
    ___ getArea(self, p1, p2, p3):
        r.. 0.5*abs(p1[0]*p2[1] \
                       +p2[0]*p3[1] \
                       +p3[0]*p1[1] \
                       -p2[0]*p1[1] \
                       -p3[0]*p2[1] \
                       -p1[0]*p3[1])
    
    ___ test(self):
        testCases = [
            [[0,0],[0,1],[1,0],[0,2],[2,0]],
            [[4,6],[6,5],[3,1]],
        ]
        ___ points __ testCases:
            print('points: %s' % points)
            result = self.largestTriangleArea(points)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
