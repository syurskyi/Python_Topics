'''
Created on Apr 8, 2018

@author: tongq
'''
class Solution(object
    ___ canTransform(self, start, end
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        ______ re
        __ re.sub('X', '', start) != re.sub('X', '', end
            r_ False
        p1, p2 = 0, 0
        w___ p1 < le.(start) and p2 < le.(end
            w___ p1 < le.(start) and start[p1] __ 'X':
                p1 += 1
            w___ p2 < le.(end) and end[p2] __ 'X':
                p2 += 1
            __ p1 __ le.(start) and p2 __ le.(end
                r_ True
            __ p1 __ le.(start) or p2 __ le.(end
                r_ False
            __ start[p1] != end[p2]:
                r_ False
            # if the character is 'L', it can only be moved to the left. p1 should be greater or equal to p2.
            __ start[p1] __ 'L' and p2 > p1:
                r_ False
            # if the character is 'R', it can only be moved to the right. p2 should be greater or equal to p1.
            __ start[p1] __ 'R' and p1 > p2:
                r_ False
            p1 += 1
            p2 += 1
        r_ True
    
    ___ canTransform_another(self, start, end
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        l, r = 0, 0
        for i in range(le.(start)):
            __ start[i] __ 'R': r += 1
            __ end[i] __ 'L': l += 1
            __ start[i] __ 'L': l -= 1
            __ end[i] __ 'R': r -= 1
            __ (l < 0 or r != 0) and (l != 0 or r < 0
                r_ False
        __ l __ 0 and r __ 0:
            r_ True
        r_ False
    
    # The following BFS solution is TLE
    
    ___ canTransform_bfs_TLE(self, start, end
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        visited = set([start])
        queue = [start]
        w___ queue:
            s = queue.pop()
            __ s __ end:
                r_ True
            for i in range(le.(s)-1
                __ s[i:i+2] in ('XL', 'RX'
                    newS = s[:i]+s[i:i+2][::-1]+s[i+2:]
                    __ newS not in visited:
                        visited.add(newS)
                        queue.append(newS)
        r_ False
    
    ___ test(self
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
        for start, end in testCases:
            print('start: %s' % start)
            print('end: %s' % end)
            result = self.canTransform(start, end)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
