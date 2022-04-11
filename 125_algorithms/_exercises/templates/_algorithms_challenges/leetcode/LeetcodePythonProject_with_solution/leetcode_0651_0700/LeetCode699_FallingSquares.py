'''
Created on Oct 26, 2017

@author: MT
'''
c_ Interval(o..
    ___ - , start, end, height
        start start
        end end
        height height

c_ Solution(o..
    ___ fallingSquares  positions
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res    # list
        intervals    # list
        h 0
        ___ pos __ positions:
            cur Interval(pos[0], pos[0]+pos[1], pos[1])
            h m..(h, getHeight(intervals, cur
            res.a..(h)
        r.. res
    
    ___ getHeight  intervals, cur
        preMaxHeight 0
        ___ i __ intervals:
            __ i.end <_ cur.start: _____
            __ i.start >_ cur.end: _____
            preMaxHeight m..(preMaxHeight, i.height)
        cur.height += preMaxHeight
        intervals.a..(cur)
        r.. cur.height
    
    ___ test
        testCases [
            [[1, 2], [2, 3], [6, 1]],
            [[100, 100], [200, 100]],
            [[6, 1], [9, 2], [2, 4]],
        ]
        ___ positions __ testCases:
            print('positions: %s' % positions)
            result fallingSquares(positions)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
