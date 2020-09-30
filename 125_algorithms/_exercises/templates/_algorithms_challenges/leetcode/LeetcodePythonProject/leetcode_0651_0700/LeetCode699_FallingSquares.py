'''
Created on Oct 26, 2017

@author: MT
'''
class Interval(object
    ___ __init__(self, start, end, height
        self.start = start
        self.end = end
        self.height = height

class Solution(object
    ___ fallingSquares(self, positions
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res =   # list
        intervals =   # list
        h = 0
        ___ pos __ positions:
            cur = Interval(pos[0], pos[0]+pos[1], pos[1])
            h = ma.(h, self.getHeight(intervals, cur))
            res.append(h)
        r_ res
    
    ___ getHeight(self, intervals, cur
        preMaxHeight = 0
        ___ i __ intervals:
            __ i.end <= cur.start: continue
            __ i.start >= cur.end: continue
            preMaxHeight = ma.(preMaxHeight, i.height)
        cur.height += preMaxHeight
        intervals.append(cur)
        r_ cur.height
    
    ___ test(self
        testCases = [
            [[1, 2], [2, 3], [6, 1]],
            [[100, 100], [200, 100]],
            [[6, 1], [9, 2], [2, 4]],
        ]
        ___ positions __ testCases:
            print('positions: %s' % positions)
            result = self.fallingSquares(positions)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
