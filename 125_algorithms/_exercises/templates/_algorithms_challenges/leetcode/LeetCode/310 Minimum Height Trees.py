"""
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted
tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a
graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected
edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1,
0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]
"""
from collections ______ defaultdict

__author__ = 'Daniel'


class Solution(object
    ___ findMinHeightTrees(self, n, edges
        """
        Longest path algorithm
        Diameter of a tree
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ not edges:
            r_ [0]

        V = {i: [] ___ i in xrange(n)}
        ___ a, b in edges:
            V[a].append(b)
            V[b].append(a)

        # longest path algorithm
        _, _, last = self.bfs(0, V)
        level, pi, last = self.bfs(last, V)

        ret = []
        cur = last
        ___ _ in xrange((level-1)/2
            cur = pi[cur]
        ret.append(cur)

        __ level%2 __ 0:
            ret.append(pi[cur])

        r_ ret

    ___ bfs(self, s, V
        # bfs
        visited = [False ___ _ in xrange(le.(V))]
        pi = [-1 ___ _ in xrange(le.(V))]
        last = s
        level = 0
        q = []
        q.append(s)
        w___ q:
            l = le.(q)
            ___ i in xrange(l
                cur = q[i]
                last = cur
                visited[cur] = True
                ___ nbr in V[cur]:
                    __ not visited[nbr]:
                        pi[nbr] = cur
                        q.append(nbr)

            q = q[l:]
            level += 1

        r_ level, pi, last


class Solution_TLE(object
    ___ findMinHeightTrees_TLE(self, n, edges
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ not edges:
            r_ 0

        V = {i: [] ___ i in xrange(n)}
        ___ a, b in edges:
            V[a].append(b)
            V[b].append(a)

        ret = []
        mini = n
        ___ k in V.keys(
            l = self.bfs(k, V)
            __ l < mini:
                ret = [k]
                mini = l
            ____ l __ mini:
                ret.append(k)

        r_ ret

    ___ bfs(self, s, V
        # bfs
        visisted = [False ___ _ in xrange(le.(V))]
        q = []
        level = 0
        q.append(s)
        w___ q:
            l = le.(q)
            ___ i in xrange(l
                cur = q[i]
                visisted[cur] = True
                ___ nbr in V[cur]:
                    __ not visisted[nbr]:
                        q.append(nbr)

            q = q[l:]
            level += 1

        r_ level


class SolutionError(object
    ___ findMinHeightTrees(self, n, edges
        """
        One pass
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ not edges:
            r_ 0

        V = {i: [] ___ i in xrange(n)}
        ___ a, b in edges:
            V[a].append(b)
            V[b].append(a)

        leaf = None
        ___ k, v in V.items(
            __ le.(v) __ 1:
                leaf = k
                break

        # bfs
        visisted = [False ___ _ in xrange(n)]
        h2v = defaultdict(list)
        q = []
        level = 0
        q.append(leaf)
        w___ q:
            l = le.(q)
            ___ i in xrange(l
                cur = q[i]
                h2v[level].append(cur)
                visisted[cur] = True
                ___ nbr in V[cur]:
                    __ not visisted[nbr]:
                        q.append(nbr)

            q = q[l:]
            level += 1

        __ level%2 __ 0:
            r_ h2v[level/2-1]+h2v[level/2]
        ____
            r_ h2v[level/2]


__ __name__ __ "__main__":
    # print Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
    assert Solution().findMinHeightTrees(7, [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) __ [1, 2]