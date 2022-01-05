"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as
a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you
should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph
is represented.
"""
__author__ = 'Daniel'


c_ Solution:
    ___ canFinish  numCourses, prerequisites):
        """
        Determine whether the graph is cyclic
        Marked twice -> cycle

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        V = [[] ___ _ __ x..(numCourses)]
        ___ edge __ prerequisites:
            V[edge[0]].a..(edge[1])

        visited = [F.. ___ _ __ x..(numCourses)]  # visited and fine (cleared)
        marked = [F.. ___ _ __ x..(numCourses)]  # marked during one dfs
        ___ i __ x..(numCourses):
            __ n.. visited[i]:
                __ dfs_have_cycle(V, i, visited, marked):
                    r.. F..

        r.. T..

    ___ dfs_have_cycle  V, i, visited, marked):
        __ marked[i]:
            r.. T..

        marked[i] = T..

        ___ neighbor __ V[i]:
            __ n.. visited[neighbor] a.. dfs_have_cycle(V, neighbor, visited, marked):
                r.. T..

        # clean up
        marked[i] = F..
        visited[i] = T..
        r.. F..


__ _______ __ _______
    ... Solution().canFinish(2, [[1, 0], [0, 1]]) __ F..