'''
Created on Apr 9, 2018

@author: tongq
'''
c_ Solution(o..
    ___ isBipartite  graph
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = l..(graph)
        colors = [-1]*n
        ___ i __ r..(n
            __ colors[i] __ -1 a.. n.. validColor(graph, colors, 0, i
                r.. F..
        r.. T..
    
    ___ validColor  graph, colors, color, node
        __ colors[node] != -1:
            r.. colors[node] __ color
        colors[node] = color
        ___ nextNode __ graph[node]:
            __ n.. validColor(graph, colors, 1-color, nextNode
                r.. F..
        r.. T..
    
    ___ test
        testCases = [
            [[1,3], [0,2], [1,3], [0,2]],
            [[1,2,3], [0,2], [0,1,3], [0,2]],
        ]
        ___ graph __ testCases:
            print('graph: %s' % graph)
            result = isBipartite(graph)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
