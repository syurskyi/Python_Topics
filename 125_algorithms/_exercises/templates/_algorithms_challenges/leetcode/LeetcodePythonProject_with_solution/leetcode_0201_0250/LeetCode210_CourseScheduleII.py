'''
Created on Feb 19, 2017

@author: MT
'''

c_ Solution(object):
    ___ findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] ___ _ __ r..(numCourses)]
        degree = [0]*numCourses
        ___ p __ prerequisites:
            graph[p[1]].a..(p[0])
            degree[p[0]]+=1
        queue    # list
        ___ num, cnt __ e..(degree):
            __ cnt __ 0:
                queue.a..(num)
        res    # list
        count = 0
        w.... queue:
            node = queue.pop(0)
            res.a..(node)
            count += 1
            ___ node0 __ graph[node]:
                degree[node0] -= 1
                __ degree[node0] __ 0:
                    queue.a..(node0)
        r.. res __ count __ numCourses ____ []
    
    ___ test
        testCases = [
            [4, [[1,0],[2,0],[3,1],[3,2]]],
            [4, [[1,0],[2,0],[0,2],[3,1]]],
            [2, [[1,0]]],
        ]
        ___ numCourses, prerequisites __ testCases:
            print('numCourses: %s' % (numCourses))
            print('prerequisites: %s' % (prerequisites))
            result = findOrder(numCourses, prerequisites)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
