'''
Created on Mar 22, 2017

@author: MT
'''

class Solution(object):
    ___ numberOfPatterns(self, m, n):
        self.skip = [[0]*10 for _ in range(10)]
        self.skip[1][3] = self.skip[3][1] = 2
        self.skip[1][7] = self.skip[7][1] = 4
        self.skip[3][9] = self.skip[9][3] = 6
        self.skip[7][9] = self.skip[9][7] = 8
        self.skip[1][9] = self.skip[9][1] = self.skip[2][8] = self.skip[8][2] = \
            self.skip[3][7] = self.skip[7][3] = self.skip[4][6] = self.skip[6][4] = 5
        result = 0
        for i in range(m, n+1):
            path = set()
            result += self.helper(path, 1, i-1)*4
            result += self.helper(path, 2, i-1)*4
            result += self.helper(path, 5, i-1)
        return result
    
    ___ helper(self, path, curr, remain):
        __ remain < 0: return 0
        __ remain == 0: return 1
        path.add(curr)
        result = 0
        for to in range(1, 10):
            __ to not in path and (self.skip[curr][to]==0 or self.skip[curr][to] in path):
                result += self.helper(path, to, remain-1)
        path.remove(curr)
        return result