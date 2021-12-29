'''
Created on Jun 13, 2019

@author: tongq
'''

class Solution(object):
    ___ rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        xs = s..(set([x ___ x1, y1, x2, y2 __ rectangles ___ x __ [x1, x2]] + [0]))
        x_i = {v: i ___ i, v __ enumerate(xs)}
        count = [0] * l..(x_i)
        L    # list
        ___ x1, y1, x2, y2 __ rectangles:
            L.a..([y1, x1, x2, 1])
            L.a..([y2, x1, x2, -1])
        L.sort()
        cur_y = cur_x_sum = area = 0
        ___ y, x1, x2, sig __ L:
            area += (y-cur_y) * cur_x_sum
            cur_y = y
            ___ i __ r..(x_i[x1], x_i[x2]):
                count[i] += sig
            cur_x_sum = s..(x2-x1 __ c ____ 0 ___ x1, x2, c __ zip(xs, xs[1:], count))
        r.. area % (10**9+7)
    
    ___ test(self):
        testCases = [
            [[0,0,2,2],[1,0,2,3],[1,0,3,1]],
            [[0,0,1000000000,1000000000]],
        ]
        ___ rectangles __ testCases:
            result = self.rectangleArea(rectangles)
            print('result: %s' % result)
            print('-='*30 + '-')

__ __name__ __ '__main__':
    Solution().test()
