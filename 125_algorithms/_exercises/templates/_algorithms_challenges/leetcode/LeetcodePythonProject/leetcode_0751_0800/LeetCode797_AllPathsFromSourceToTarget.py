'''
Created on Apr 18, 2018

@author: tongq
'''
class Solution(object
    ___ allPathsSourceTarget(self, graph
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = le.(graph)
        queue = [[0]]
        res = []
        w___ queue:
            path = queue.pop(0)
            __ path[-1] __ n-1:
                res.append(list(path))
            ____
                ___ node in graph[path[-1]]:
                    queue.append(path + [node])
        r_ res
    
    ___ test(self
        testCases = [
            [[1,2], [3], [3], []],
        ]
        ___ graph in testCases:
            result = self.allPathsSourceTarget(graph)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
