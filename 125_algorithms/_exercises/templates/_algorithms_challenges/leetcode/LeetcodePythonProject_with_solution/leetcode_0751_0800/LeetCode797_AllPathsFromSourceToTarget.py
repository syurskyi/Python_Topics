'''
Created on Apr 18, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ allPathsSourceTarget  graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = l..(graph)
        queue = [[0]]
        res    # list
        w.... queue:
            path = queue.pop(0)
            __ path[-1] __ n-1:
                res.a..(l..(path))
            ____:
                ___ node __ graph[path[-1]]:
                    queue.a..(path + [node])
        r.. res
    
    ___ test
        testCases = [
            [[1,2], [3], [3], []],
        ]
        ___ graph __ testCases:
            result = allPathsSourceTarget(graph)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
