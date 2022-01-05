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
_______ sys

sys.setrecursionlimit(5000)

c_ Solution(object):
    ___ canFinish  numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        Detect if course prerequisites graph has a cycle.
        """

        unvisited = set(r..(numCourses))
        visiting = set()
        visited = set()
        graph = {x: set() ___ x __ r..(numCourses)}
        ___ c, p __ prerequisites:
            graph[p].add(c)

        ___ u __ r..(numCourses):
            __ u __ unvisited:
                __ visit(u) __ F..:
                    r.. F..
        r.. T..

    ___ visit  u):
        __ u __ visiting:
            r.. F..
        ____ u __ unvisited:
            unvisited.remove(u)
            visiting.add(u)
            ___ v __ graph[u]:
                __ visit(v) __ F..:
                    r.. F..
            visiting.remove(u)
            visited.add(u)

s = Solution()
print(s.canFinish(1, []))
print(s.canFinish(3, [[1, 0], [0, 1]]))
w__ open('test.txt') __ f:
    args = f.read().s..
    arg0 = i..(args[0][:-1])
    arg1 = eval(args[1])
    print(s.canFinish(arg0, arg1))
