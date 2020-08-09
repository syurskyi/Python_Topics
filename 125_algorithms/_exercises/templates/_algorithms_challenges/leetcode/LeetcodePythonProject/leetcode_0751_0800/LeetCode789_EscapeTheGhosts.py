'''
Created on Apr 14, 2018

@author: tongq
'''
class Solution(object
    ___ escapeGhosts(self, ghosts, target
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        maxVal = abs(target[0])+abs(target[1])
        for g in ghosts:
            d = abs(g[0]-target[0])+abs(g[1]-target[1])
            __ d <= maxVal:
                r_ False
        r_ True
    
    ___ test(self
        testCases = [
            
        ]
        for ghosts, target in testCases:
            result = self.escapeGhosts(ghosts, target)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
