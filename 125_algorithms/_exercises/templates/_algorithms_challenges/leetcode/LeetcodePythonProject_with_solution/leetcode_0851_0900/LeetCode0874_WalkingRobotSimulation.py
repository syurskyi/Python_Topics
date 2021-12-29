'''
Created on Oct 7, 2019

@author: tongq
'''
class Solution(object):
    ___ robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pos = [0, 0]
        res = 0
        d = 0
        hashset = set()
        for ob in obstacles:
            hashset.add(tuple(ob))
        for c in commands:
            __ c in (-1, -2):
                d = self.calDirection(d, c)
            else:
                for _ in range(c):
                    __ (pos[0] + dirs[d][0], pos[1] + dirs[d][1]) not in hashset:
                        pos = [pos[0] + dirs[d][0], pos[1] + dirs[d][1]]
            res = max(res, pos[0]**2 + pos[1]**2)
        return res
    
    ___ calDirection(self, d, c):
        __ c == -2:
            d -= 1
        elif c == -1:
            d += 1
        d %= 4
        return d
    
    ___ test(self):
        testCases = [
            [
                [4,-1,3],
                [],
            ],
        ]
        for commands, obstacles in testCases:
            res = self.robotSim(commands, obstacles)
            print('res: %s' % res)

__ __name__ == '__main__':
    Solution().test()
