'''
Created on Feb 18, 2017

@author: MT
'''

class Solution(object
    ___ canFinishBFS(self, numCourses, prerequisites
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] ___ _ in range(numCourses)]
        degree = [0]*numCourses
        queue = []
        count = 0
        ___ prereq in prerequisites:
            degree[prereq[0]] += 1
            graph[prereq[1]].append(prereq[0])
        print('degree: %s' % (degree))
        ___ i in range(numCourses
            __ degree[i] __ 0:
                queue.append(i)
                count += 1
        w___ queue:
            course = queue.pop(0)
            ___ pointer in graph[course]:
                degree[pointer] -= 1
                __ degree[pointer] __ 0:
                    queue.append(pointer)
                    count += 1
        print('graph:  %s' % (graph))
        print('degree: %s' % (degree))
        __ count __ numCourses:
            r_ True
        ____
            r_ False
    
    ___ canFinishDFS(self, numCourses, prerequisites
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] ___ _ in range(numCourses)]
        visited = [False]*numCourses
        ___ i, prereq in enumerate(prerequisites
            graph[prereq[1]].append(prereq[0])
        ___ i in range(numCourses
            __ not self.dfs(graph, visited, i
                r_ False
        r_ True
    
    ___ dfs(self, graph, visited, course
        __ visited[course]:
            r_ False
        ____
            visited[course] = True
        ___ precourse in graph[course]:
            __ not self.dfs(graph, visited, precourse
                r_ False
        visited[course] = False
        r_ True
    
    ___ test(self
        testCases = [
            (2, [[1, 0]]),
            (5, [[0, 1], [1, 2], [2, 3]]),
            (6, [[0, 2], [2, 1], [1, 3]]),
            (5, [[0, 1], [1, 2], [2, 3], [4, 1], [4, 2], [4, 0], [1, 4]]),
            (3, [[0, 1], [1, 0], [2, 0]]),
        ]
        ___ numCourses, prerequisites in testCases:
            print('numCourses: %s' % (numCourses))
            print('prerequisites: %s' % (prerequisites))
            result = self.canFinishDFS(numCourses, prerequisites)
            print('DFS Result: %s' % (result))
            result = self.canFinishBFS(numCourses, prerequisites)
            print('BFS Result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()