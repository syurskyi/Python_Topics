'''
Created on Apr 20, 2018

@author: tongq
'''
class Solution(object):
    ___ eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = l..(graph)
        outdegrees = [0]*n
        inlinks = [[] ___ i __ r..(n)]
        ___ i __ r..(n):
            outdegrees[i] = l..(graph[i])
        ___ i __ r..(n):
            ___ j __ graph[i]:
                inlinks[j].a..(i)
        queue    # list
        ___ i __ r..(n):
            __ outdegrees[i] __ 0:
                queue.a..(i)
        res    # list
        while queue:
            i = queue.pop(0)
            res.a..(i)
            ___ j __ inlinks[i]:
                outdegrees[j] -= 1
                __ outdegrees[j] __ 0:
                    queue.a..(j)
        res.sort()
        r.. res
    
    ___ eventualSafeNodes_own_TLE(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = l..(graph)
        isCycle = [False]*n
        ___ i __ r..(n):
            visited = set()
            self.getIsCycle(i, i, graph, visited, isCycle)
        r.. [i ___ i __ r..(n) __ n.. isCycle[i]]
    
    ___ getIsCycle(self, i, start, graph, visited, isCycle):
        __ start __ visited o. isCycle[start]:
            isCycle[i] = True
            r..
        visited.add(start)
        ___ nextVal __ graph[start]:
            self.getIsCycle(i, nextVal, graph, visited, isCycle)
        visited.remove(start)
    
    ___ test(self):
        testCases = [
            [[1,2],[2,3],[5],[0],[5],[],[]],
            [[],[0,2,3,4],[3],[4],[]],
        ]
        ___ graph __ testCases:
            print('graph: %s' % graph)
            result = self.eventualSafeNodes(graph)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
