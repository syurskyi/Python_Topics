'''
Created on Apr 20, 2018

@author: tongq
'''
c_ Solution(o..
    ___ eventualSafeNodes  graph
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n l..(graph)
        outdegrees [0]*n
        inlinks [[] ___ i __ r..(n)]
        ___ i __ r..(n
            outdegrees[i] l..(graph[i])
        ___ i __ r..(n
            ___ j __ graph[i]:
                inlinks[j].a..(i)
        queue    # list
        ___ i __ r..(n
            __ outdegrees[i] __ 0:
                queue.a..(i)
        res    # list
        w.... queue:
            i queue.p.. 0)
            res.a..(i)
            ___ j __ inlinks[i]:
                outdegrees[j] -_ 1
                __ outdegrees[j] __ 0:
                    queue.a..(j)
        res.s..()
        r.. res
    
    ___ eventualSafeNodes_own_TLE  graph
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n l..(graph)
        isCycle [F..]*n
        ___ i __ r..(n
            visited s..()
            getIsCycle(i, i, graph, visited, isCycle)
        r.. [i ___ i __ r..(n) __ n.. isCycle[i]]
    
    ___ getIsCycle  i, start, graph, visited, isCycle
        __ start __ visited o. isCycle[start]:
            isCycle[i] T..
            r..
        visited.add(start)
        ___ nextVal __ graph[start]:
            getIsCycle(i, nextVal, graph, visited, isCycle)
        visited.remove(start)
    
    ___ test
        testCases [
            [[1,2],[2,3],[5],[0],[5],[],[]],
            [[],[0,2,3,4],[3],[4],[]],
        ]
        ___ graph __ testCases:
            print('graph: %s' % graph)
            result eventualSafeNodes(graph)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
