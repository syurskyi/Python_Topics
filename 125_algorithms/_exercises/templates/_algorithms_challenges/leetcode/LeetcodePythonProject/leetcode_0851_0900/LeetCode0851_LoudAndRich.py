'''
Created on Sep 9, 2019

@author: tongq
'''
class Solution(object
    ___ loudAndRich(self, richer, quiet
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        n = le.(quiet)
        richer2 = {}
        ___ i in range(n
            richer2[i] = []
        ___ v in richer:
            richer2[v[1]].append(v[0])
        res = [-1 ___ i in range(n)]
        ___ i in range(n
            self.dfs(i, quiet, richer2, res)
        r_ res
    
    ___ dfs(self, i, quiet, richer2, res
        __ (res[i] >= 0
            r_ res[i]
        res[i] = i
        ___ j in richer2[i]:
            __ quiet[res[i]] > quiet[self.dfs(j, quiet, richer2, res)]:
                res[i] = res[j]
        r_ res[i]
    
    ___ test(self
        testCase = [
            [
                [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],
                [3,2,5,4,6,1,7,0],
            ],
        ]
        ___ richer, quiet in testCase:
            res = self.loudAndRich(richer, quiet)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
