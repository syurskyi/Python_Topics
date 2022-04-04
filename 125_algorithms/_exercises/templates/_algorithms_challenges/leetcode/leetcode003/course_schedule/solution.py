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

c_ Solution(o..
    ___ canFinish  numCourses, prerequisites
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
        queue    # list
        finished_courses    # list
        prq_graph = {x: s..() ___ x __ r..(numCourses)}
        ___ c, p __ prerequisites:
            prq_graph[c].add(p)

        # Add nodes with no prerequisites
        ___ c __ prq_graph:
            __ n.. prq_graph[c]:
                queue.a..(c)

        # For each of the remaining node, remove its prerequisites in queue;
        # if node has no prerequisites, add it to queue, and repeat
        w.... queue:
            u = queue.p.. 0)
            ___ v, prqs __ prq_graph.i..:
                __ u __ prqs:
                    prqs.remove(u)
                    __ n.. prqs:
                        queue.a..(v)
            finished_courses.a..(u)

        r.. l..(finished_courses) __ numCourses

s = Solution()
print(s.canFinish(1, []
print(s.canFinish(3, [[1, 0], [0, 1]]
