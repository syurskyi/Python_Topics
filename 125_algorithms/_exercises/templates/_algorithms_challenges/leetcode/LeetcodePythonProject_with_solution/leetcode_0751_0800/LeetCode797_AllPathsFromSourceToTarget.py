'''
Created on Apr 18, 2018

@author: tongq
'''
class Solution(object):
    ___ allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        queue = [[0]]
        res = []
        while queue:
            path = queue.pop(0)
            __ path[-1] == n-1:
                res.append(list(path))
            else:
                for node in graph[path[-1]]:
                    queue.append(path + [node])
        return res
    
    ___ test(self):
        testCases = [
            [[1,2], [3], [3], []],
        ]
        for graph in testCases:
            result = self.allPathsSourceTarget(graph)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
