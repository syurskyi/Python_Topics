'''
Created on Apr 14, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ escapeGhosts  ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        maxVal = abs(target[0])+abs(target[1])
        ___ g __ ghosts:
            d = abs(g[0]-target[0])+abs(g[1]-target[1])
            __ d <= maxVal:
                r.. F..
        r.. T..
    
    ___ test
        testCases = [
            
        ]
        ___ ghosts, target __ testCases:
            result = escapeGhosts(ghosts, target)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
