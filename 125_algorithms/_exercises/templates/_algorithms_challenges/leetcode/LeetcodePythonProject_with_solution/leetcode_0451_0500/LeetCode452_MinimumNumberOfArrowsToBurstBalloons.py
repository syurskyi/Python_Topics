'''
Created on Apr 20, 2017

@author: MT
'''

class Solution(object):
    ___ findMinArrowShots(self, points):
        __ n.. points: r.. 0
        points.s..(key=l.... x: (x[1], x[0]))
        count = 0
        maxLen = float('-inf')
        ___ point __ points:
            __ point[0] > maxLen:
                maxLen = point[1]
            ____:
                count += 1
        r.. l..(points)-count
    
    ___ test(self):
        testCases = [
            [[10,16], [2,8], [1,6], [7,12]],
        ]
        ___ points __ testCases:
            print('points: %s' % points)
            result = self.findMinArrowShots(points)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
