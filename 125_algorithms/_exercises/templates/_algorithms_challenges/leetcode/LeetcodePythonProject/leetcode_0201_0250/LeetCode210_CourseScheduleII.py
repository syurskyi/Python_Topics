'''
Created on Feb 19, 2017

@author: MT
'''

class Solution(object
    ___ findOrder(self, numCourses, prerequisites
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] ___ _ in range(numCourses)]
        degree = [0]*numCourses
        ___ p in prerequisites:
            graph[p[1]].append(p[0])
            degree[p[0]]+=1
        queue = []
        ___ num, cnt in enumerate(degree
            __ cnt __ 0:
                queue.append(num)
        res = []
        count = 0
        w___ queue:
            node = queue.pop(0)
            res.append(node)
            count += 1
            ___ node0 in graph[node]:
                degree[node0] -= 1
                __ degree[node0] __ 0:
                    queue.append(node0)
        r_ res __ count __ numCourses else []
    
    ___ test(self
        testCases = [
            [4, [[1,0],[2,0],[3,1],[3,2]]],
            [4, [[1,0],[2,0],[0,2],[3,1]]],
            [2, [[1,0]]],
        ]
        ___ numCourses, prerequisites in testCases:
            print('numCourses: %s' % (numCourses))
            print('prerequisites: %s' % (prerequisites))
            result = self.findOrder(numCourses, prerequisites)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
