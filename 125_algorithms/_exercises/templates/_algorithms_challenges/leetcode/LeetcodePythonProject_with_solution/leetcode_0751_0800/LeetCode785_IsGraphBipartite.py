'''
Created on Apr 9, 2018

@author: tongq
'''
class Solution(object):
    ___ isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = l..(graph)
        colors = [-1]*n
        ___ i __ r..(n):
            __ colors[i] __ -1 and n.. self.validColor(graph, colors, 0, i):
                r.. False
        r.. True
    
    ___ validColor(self, graph, colors, color, node):
        __ colors[node] != -1:
            r.. colors[node] __ color
        colors[node] = color
        ___ nextNode __ graph[node]:
            __ n.. self.validColor(graph, colors, 1-color, nextNode):
                r.. False
        r.. True
    
    ___ test(self):
        testCases = [
            [[1,3], [0,2], [1,3], [0,2]],
            [[1,2,3], [0,2], [0,1,3], [0,2]],
        ]
        ___ graph __ testCases:
            print('graph: %s' % graph)
            result = self.isBipartite(graph)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
