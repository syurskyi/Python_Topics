'''
Created on Apr 8, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ canTransform  start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        _______ __
        __ __.sub('X', '', start) != __.sub('X', '', end):
            r.. F..
        p1, p2 = 0, 0
        w.... p1 < l..(start) a.. p2 < l..(end):
            w.... p1 < l..(start) a.. start[p1] __ 'X':
                p1 += 1
            w.... p2 < l..(end) a.. end[p2] __ 'X':
                p2 += 1
            __ p1 __ l..(start) a.. p2 __ l..(end):
                r.. T..
            __ p1 __ l..(start) o. p2 __ l..(end):
                r.. F..
            __ start[p1] != end[p2]:
                r.. F..
            # if the character is 'L', it can only be moved to the left. p1 should be greater or equal to p2.
            __ start[p1] __ 'L' a.. p2 > p1:
                r.. F..
            # if the character is 'R', it can only be moved to the right. p2 should be greater or equal to p1.
            __ start[p1] __ 'R' a.. p1 > p2:
                r.. F..
            p1 += 1
            p2 += 1
        r.. T..
    
    ___ canTransform_another  start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        l, r = 0, 0
        ___ i __ r..(l..(start)):
            __ start[i] __ 'R': r += 1
            __ end[i] __ 'L': l += 1
            __ start[i] __ 'L': l -= 1
            __ end[i] __ 'R': r -= 1
            __ (l < 0 o. r != 0) a.. (l != 0 o. r < 0):
                r.. F..
        __ l __ 0 a.. r __ 0:
            r.. T..
        r.. F..
    
    # The following BFS solution is TLE
    
    ___ canTransform_bfs_TLE  start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        visited = s..([start])
        queue = [start]
        w.... queue:
            s = queue.pop()
            __ s __ end:
                r.. T..
            ___ i __ r..(l..(s)-1):
                __ s[i:i+2] __ ('XL', 'RX'):
                    newS = s[:i]+s[i:i+2][::-1]+s[i+2:]
                    __ newS n.. __ visited:
                        visited.add(newS)
                        queue.a..(newS)
        r.. F..
    
    ___ test
        testCases = [
            [
                "RXXLRXRXL",
                "XRLXXRRLX",
            ],
            [
                "XXRXXLXXXX",
                "XXXXRXXLXX",
            ],
        ]
        ___ start, end __ testCases:
            print('start: %s' % start)
            print('end: %s' % end)
            result = canTransform(start, end)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
