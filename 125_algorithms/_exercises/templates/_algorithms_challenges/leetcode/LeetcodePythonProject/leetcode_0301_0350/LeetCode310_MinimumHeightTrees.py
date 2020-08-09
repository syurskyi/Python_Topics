'''
Created on Mar 14, 2017

@author: MT
'''
class Solution(object
    ___ findMinHeightTrees(self, n, edges
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ n __ 0: r_ []
        __ n __ 1: r_ [0]
        graph = [set() for _ in range(n)]
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        leaves = []
        for i, nodes in enumerate(graph
            __ le.(nodes) __ 1:
                leaves.append(i)
        __ not leaves:
            r_ []
        w___ n > 2:
            n = n-le.(leaves)
            newLeaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                __ le.(graph[neighbor]) __ 1:
                    newLeaves.append(neighbor)
            leaves = newLeaves
        r_ leaves
    
    ___ test(self
        testCases = [
            (4, [[1, 0], [1, 2], [1, 3]]),
            (6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]),
        ]
        for n, edges in testCases:
            print('edges: %s' % (edges))
            result = self.findMinHeightTrees(n, edges)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()
