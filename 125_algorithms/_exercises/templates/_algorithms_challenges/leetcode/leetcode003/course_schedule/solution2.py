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

class Solution(object):
    ___ canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        Detect if course prerequisites graph has a cycle.
        """

        self.unvisited = set(r..(numCourses))
        self.visiting = set()
        self.visited = set()
        self.graph = {x: set() ___ x __ r..(numCourses)}
        ___ c, p __ prerequisites:
            self.graph[p].add(c)

        ___ u __ r..(numCourses):
            __ u __ self.unvisited:
                __ self.visit(u) __ False:
                    r.. False
        r.. True

    ___ visit(self, u):
        __ u __ self.visiting:
            r.. False
        ____ u __ self.unvisited:
            self.unvisited.remove(u)
            self.visiting.add(u)
            ___ v __ self.graph[u]:
                __ self.visit(v) __ False:
                    r.. False
            self.visiting.remove(u)
            self.visited.add(u)

s = Solution()
print(s.canFinish(1, []))
print(s.canFinish(3, [[1, 0], [0, 1]]))
with open('test.txt') as f:
    args = f.read().s..
    arg0 = int(args[0][:-1])
    arg1 = eval(args[1])
    print(s.canFinish(arg0, arg1))
