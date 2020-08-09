'''
Created on Apr 20, 2018

@author: tongq
'''
class Solution(object
    ___ eventualSafeNodes(self, graph
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = le.(graph)
        outdegrees = [0]*n
        inlinks = [[] ___ i in range(n)]
        ___ i in range(n
            outdegrees[i] = le.(graph[i])
        ___ i in range(n
            ___ j in graph[i]:
                inlinks[j].append(i)
        queue = []
        ___ i in range(n
            __ outdegrees[i] __ 0:
                queue.append(i)
        res = []
        w___ queue:
            i = queue.pop(0)
            res.append(i)
            ___ j in inlinks[i]:
                outdegrees[j] -= 1
                __ outdegrees[j] __ 0:
                    queue.append(j)
        res.sort()
        r_ res
    
    ___ eventualSafeNodes_own_TLE(self, graph
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = le.(graph)
        isCycle = [False]*n
        ___ i in range(n
            visited = set()
            self.getIsCycle(i, i, graph, visited, isCycle)
        r_ [i ___ i in range(n) __ not isCycle[i]]
    
    ___ getIsCycle(self, i, start, graph, visited, isCycle
        __ start in visited or isCycle[start]:
            isCycle[i] = True
            r_
        visited.add(start)
        ___ nextVal in graph[start]:
            self.getIsCycle(i, nextVal, graph, visited, isCycle)
        visited.remove(start)
    
    ___ test(self
        testCases = [
            [[1,2],[2,3],[5],[0],[5],[],[]],
            [[],[0,2,3,4],[3],[4],[]],
        ]
        ___ graph in testCases:
            print('graph: %s' % graph)
            result = self.eventualSafeNodes(graph)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
