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


class Solution:
    ___ canFinish(self, numCourses, prerequisites):
        """
        Determine whether the graph is cyclic
        Marked twice -> cycle

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        V = [[] ___ _ __ xrange(numCourses)]
        ___ edge __ prerequisites:
            V[edge[0]].a..(edge[1])

        visited = [False ___ _ __ xrange(numCourses)]  # visited and fine (cleared)
        marked = [False ___ _ __ xrange(numCourses)]  # marked during one dfs
        ___ i __ xrange(numCourses):
            __ n.. visited[i]:
                __ self.dfs_have_cycle(V, i, visited, marked):
                    r.. False

        r.. True

    ___ dfs_have_cycle(self, V, i, visited, marked):
        __ marked[i]:
            r.. True

        marked[i] = True

        ___ neighbor __ V[i]:
            __ n.. visited[neighbor] a.. self.dfs_have_cycle(V, neighbor, visited, marked):
                r.. True

        # clean up
        marked[i] = False
        visited[i] = True
        r.. False


__ __name__ __ "__main__":
    ... Solution().canFinish(2, [[1, 0], [0, 1]]) __ False