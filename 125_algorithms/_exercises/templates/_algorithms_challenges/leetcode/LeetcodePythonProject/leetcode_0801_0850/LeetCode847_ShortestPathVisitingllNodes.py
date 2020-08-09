'''
Created on Apr 10, 2019

@author: tongq
'''

class Solution(object
    ___ shortestPathLength(self, graph
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = le.(graph)
        queue = []
        hashset = set()
        
        for i in range(n
            tmp = (1 << i)
            hashset.add((tmp, i, 0))
            queue.append((tmp, i, 1))
        
        w___ queue:
            curr = queue.pop(0)
            __ curr[0] __ (1 << n)-1:
                r_ curr[2]-1
            ____
                neighbors = graph[curr[1]]
                for v in neighbors:
                    bitMask = curr[0]
                    bitMask |= (1<<v)
                    t = (bitMask, v, 0)
                    __ t not in hashset:
                        queue.append((bitMask, v, curr[2]+1))
                        hashset.add(t)
        r_ -1
    
    ___ test(self
        testCases = [
            [[1,2,3],[0],[0],[0]],
            [[1],[0,2,4],[1,3,4],[2],[1,2]],
        ]
        for graph in testCases:
            result = self.shortestPathLength(graph)
            print('result: %s' % result)

__ __name__ __ '__main__':
    Solution().test()
