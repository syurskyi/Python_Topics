'''
Created on Apr 8, 2018

@author: tongq
'''
class Solution(object):
    ___ canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        _______ re
        __ re.sub('X', '', start) != re.sub('X', '', end):
            r.. False
        p1, p2 = 0, 0
        while p1 < l..(start) and p2 < l..(end):
            while p1 < l..(start) and start[p1] __ 'X':
                p1 += 1
            while p2 < l..(end) and end[p2] __ 'X':
                p2 += 1
            __ p1 __ l..(start) and p2 __ l..(end):
                r.. True
            __ p1 __ l..(start) o. p2 __ l..(end):
                r.. False
            __ start[p1] != end[p2]:
                r.. False
            # if the character is 'L', it can only be moved to the left. p1 should be greater or equal to p2.
            __ start[p1] __ 'L' and p2 > p1:
                r.. False
            # if the character is 'R', it can only be moved to the right. p2 should be greater or equal to p1.
            __ start[p1] __ 'R' and p1 > p2:
                r.. False
            p1 += 1
            p2 += 1
        r.. True
    
    ___ canTransform_another(self, start, end):
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
            __ (l < 0 o. r != 0) and (l != 0 o. r < 0):
                r.. False
        __ l __ 0 and r __ 0:
            r.. True
        r.. False
    
    # The following BFS solution is TLE
    
    ___ canTransform_bfs_TLE(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        visited = set([start])
        queue = [start]
        while queue:
            s = queue.pop()
            __ s __ end:
                r.. True
            ___ i __ r..(l..(s)-1):
                __ s[i:i+2] __ ('XL', 'RX'):
                    newS = s[:i]+s[i:i+2][::-1]+s[i+2:]
                    __ newS n.. __ visited:
                        visited.add(newS)
                        queue.a..(newS)
        r.. False
    
    ___ test(self):
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
            result = self.canTransform(start, end)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
