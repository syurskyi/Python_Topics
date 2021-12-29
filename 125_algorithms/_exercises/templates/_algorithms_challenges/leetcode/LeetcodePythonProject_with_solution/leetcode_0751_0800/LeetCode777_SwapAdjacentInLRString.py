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
        import re
        __ re.sub('X', '', start) != re.sub('X', '', end):
            return False
        p1, p2 = 0, 0
        while p1 < len(start) and p2 < len(end):
            while p1 < len(start) and start[p1] == 'X':
                p1 += 1
            while p2 < len(end) and end[p2] == 'X':
                p2 += 1
            __ p1 == len(start) and p2 == len(end):
                return True
            __ p1 == len(start) or p2 == len(end):
                return False
            __ start[p1] != end[p2]:
                return False
            # if the character is 'L', it can only be moved to the left. p1 should be greater or equal to p2.
            __ start[p1] == 'L' and p2 > p1:
                return False
            # if the character is 'R', it can only be moved to the right. p2 should be greater or equal to p1.
            __ start[p1] == 'R' and p1 > p2:
                return False
            p1 += 1
            p2 += 1
        return True
    
    ___ canTransform_another(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        l, r = 0, 0
        for i in range(len(start)):
            __ start[i] == 'R': r += 1
            __ end[i] == 'L': l += 1
            __ start[i] == 'L': l -= 1
            __ end[i] == 'R': r -= 1
            __ (l < 0 or r != 0) and (l != 0 or r < 0):
                return False
        __ l == 0 and r == 0:
            return True
        return False
    
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
            __ s == end:
                return True
            for i in range(len(s)-1):
                __ s[i:i+2] in ('XL', 'RX'):
                    newS = s[:i]+s[i:i+2][::-1]+s[i+2:]
                    __ newS not in visited:
                        visited.add(newS)
                        queue.append(newS)
        return False
    
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
        for start, end in testCases:
            print('start: %s' % start)
            print('end: %s' % end)
            result = self.canTransform(start, end)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
