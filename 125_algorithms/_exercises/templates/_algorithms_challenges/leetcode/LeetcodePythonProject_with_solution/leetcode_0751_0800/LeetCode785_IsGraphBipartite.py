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
        n = len(graph)
        colors = [-1]*n
        for i in range(n):
            __ colors[i] == -1 and not self.validColor(graph, colors, 0, i):
                return False
        return True
    
    ___ validColor(self, graph, colors, color, node):
        __ colors[node] != -1:
            return colors[node] == color
        colors[node] = color
        for nextNode in graph[node]:
            __ not self.validColor(graph, colors, 1-color, nextNode):
                return False
        return True
    
    ___ test(self):
        testCases = [
            [[1,3], [0,2], [1,3], [0,2]],
            [[1,2,3], [0,2], [0,1,3], [0,2]],
        ]
        for graph in testCases:
            print('graph: %s' % graph)
            result = self.isBipartite(graph)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
