'''
Created on Apr 10, 2019

@author: tongq
'''

c_ Solution(o..):
    ___ shortestPathLength  graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = l..(graph)
        queue    # list
        hashset = set()
        
        ___ i __ r..(n):
            tmp = (1 << i)
            hashset.add((tmp, i, 0))
            queue.a..((tmp, i, 1))
        
        w.... queue:
            curr = queue.pop(0)
            __ curr[0] __ (1 << n)-1:
                r.. curr[2]-1
            ____:
                neighbors = graph[curr[1]]
                ___ v __ neighbors:
                    bitMask = curr[0]
                    bitMask |= (1<<v)
                    t = (bitMask, v, 0)
                    __ t n.. __ hashset:
                        queue.a..((bitMask, v, curr[2]+1))
                        hashset.add(t)
        r.. -1
    
    ___ test
        testCases = [
            [[1,2,3],[0],[0],[0]],
            [[1],[0,2,4],[1,3,4],[2],[1,2]],
        ]
        ___ graph __ testCases:
            result = shortestPathLength(graph)
            print('result: %s' % result)

__ _____ __ _____
    Solution().test()
