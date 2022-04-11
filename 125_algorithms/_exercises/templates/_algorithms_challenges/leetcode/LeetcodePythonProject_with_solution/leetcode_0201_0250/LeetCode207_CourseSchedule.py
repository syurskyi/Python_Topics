'''
Created on Feb 18, 2017

@author: MT
'''

c_ Solution(o..
    ___ canFinishBFS  numCourses, prerequisites
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph [[] ___ _ __ r..(numCourses)]
        degree [0]*numCourses
        queue    # list
        count 0
        ___ prereq __ prerequisites:
            degree[prereq[0]] += 1
            graph[prereq[1]].a..(prereq[0])
        print('degree: %s' % (degree
        ___ i __ r..(numCourses
            __ degree[i] __ 0:
                queue.a..(i)
                count += 1
        w.... queue:
            course queue.p.. 0)
            ___ pointer __ graph[course]:
                degree[pointer] -_ 1
                __ degree[pointer] __ 0:
                    queue.a..(pointer)
                    count += 1
        print('graph:  %s' % (graph
        print('degree: %s' % (degree
        __ count __ numCourses:
            r.. T..
        ____
            r.. F..
    
    ___ canFinishDFS  numCourses, prerequisites
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph [[] ___ _ __ r..(numCourses)]
        visited [F..]*numCourses
        ___ i, prereq __ e..(prerequisites
            graph[prereq[1]].a..(prereq[0])
        ___ i __ r..(numCourses
            __ n.. dfs(graph, visited, i
                r.. F..
        r.. T..
    
    ___ dfs  graph, visited, course
        __ visited[course]:
            r.. F..
        ____
            visited[course] T..
        ___ precourse __ graph[course]:
            __ n.. dfs(graph, visited, precourse
                r.. F..
        visited[course] F..
        r.. T..
    
    ___ test
        testCases [
            (2, [[1, 0]]),
            (5, [[0, 1], [1, 2], [2, 3]]),
            (6, [[0, 2], [2, 1], [1, 3]]),
            (5, [[0, 1], [1, 2], [2, 3], [4, 1], [4, 2], [4, 0], [1, 4]]),
            (3, [[0, 1], [1, 0], [2, 0]]),
        ]
        ___ numCourses, prerequisites __ testCases:
            print('numCourses: %s' % (numCourses
            print('prerequisites: %s' % (prerequisites
            result canFinishDFS(numCourses, prerequisites)
            print('DFS Result: %s' % (result
            result canFinishBFS(numCourses, prerequisites)
            print('BFS Result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()