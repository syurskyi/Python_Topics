'''
Created on Oct 26, 2017

@author: MT
'''
c_ Interval(object):
    ___ - , start, end, height):
        start = start
        end = end
        height = height

c_ Solution(object):
    ___ fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res    # list
        intervals    # list
        h = 0
        ___ pos __ positions:
            cur = Interval(pos[0], pos[0]+pos[1], pos[1])
            h = max(h, getHeight(intervals, cur))
            res.a..(h)
        r.. res
    
    ___ getHeight(self, intervals, cur):
        preMaxHeight = 0
        ___ i __ intervals:
            __ i.end <= cur.start: _____
            __ i.start >= cur.end: _____
            preMaxHeight = max(preMaxHeight, i.height)
        cur.height += preMaxHeight
        intervals.a..(cur)
        r.. cur.height
    
    ___ test
        testCases = [
            [[1, 2], [2, 3], [6, 1]],
            [[100, 100], [200, 100]],
            [[6, 1], [9, 2], [2, 4]],
        ]
        ___ positions __ testCases:
            print('positions: %s' % positions)
            result = fallingSquares(positions)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
