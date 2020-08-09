"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0, and to take course 0 you should also have finished course
1. So it is impossible.
"""

class Solution(object
    ___ canFinish(self, numCourses, prerequisites
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        Topological sort
        """
        # An implementation of
        # https://en.wikipedia.org/wiki/Topological_sorting#Algorithms
        #
        # Graph in which each node has its prerequisite courses as a
        # adjacency list
        queue = []
        finished_courses = []
        prq_graph = {x: set() ___ x in range(numCourses)}
        ___ c, p in prerequisites:
            prq_graph[c].add(p)

        # Add nodes with no prerequisites
        ___ c in prq_graph:
            __ not prq_graph[c]:
                queue.append(c)

        # For each of the remaining node, remove its prerequisites in queue;
        # if node has no prerequisites, add it to queue, and repeat
        w___ queue:
            u = queue.pop(0)
            ___ v, prqs in prq_graph.items(
                __ u in prqs:
                    prqs.remove(u)
                    __ not prqs:
                        queue.append(v)
            finished_courses.append(u)

        r_ le.(finished_courses) __ numCourses

s = Solution()
print(s.canFinish(1, []))
print(s.canFinish(3, [[1, 0], [0, 1]]))
