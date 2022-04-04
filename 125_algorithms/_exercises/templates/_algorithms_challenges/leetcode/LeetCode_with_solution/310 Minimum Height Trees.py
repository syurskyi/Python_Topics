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
____ c.. _______ d..

__author__ = 'Daniel'


c_ Solution(o..
    ___ findMinHeightTrees  n, edges
        """
        Longest path algorithm
        Diameter of a tree
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ n.. edges:
            r.. [0]

        V = {i: [] ___ i __ x..(n)}
        ___ a, b __ edges:
            V[a].a..(b)
            V[b].a..(a)

        # longest path algorithm
        _, _, last = bfs(0, V)
        level, pi, last = bfs(last, V)

        ret    # list
        cur = last
        ___ _ __ x..((level-1)/2
            cur = pi[cur]
        ret.a..(cur)

        __ level%2 __ 0:
            ret.a..(pi[cur])

        r.. ret

    ___ bfs  s, V
        # bfs
        visited = [F.. ___ _ __ x..(l..(V]
        pi = [-1 ___ _ __ x..(l..(V]
        last = s
        level = 0
        q    # list
        q.a..(s)
        w.... q:
            l = l..(q)
            ___ i __ x..(l
                cur = q[i]
                last = cur
                visited[cur] = T..
                ___ nbr __ V[cur]:
                    __ n.. visited[nbr]:
                        pi[nbr] = cur
                        q.a..(nbr)

            q = q[l:]
            level += 1

        r.. level, pi, last


c_ Solution_TLE(o..
    ___ findMinHeightTrees_TLE  n, edges
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ n.. edges:
            r.. 0

        V = {i: [] ___ i __ x..(n)}
        ___ a, b __ edges:
            V[a].a..(b)
            V[b].a..(a)

        ret    # list
        mini = n
        ___ k __ V.k..:
            l = bfs(k, V)
            __ l < mini:
                ret = [k]
                mini = l
            ____ l __ mini:
                ret.a..(k)

        r.. ret

    ___ bfs  s, V
        # bfs
        visisted = [F.. ___ _ __ x..(l..(V]
        q    # list
        level = 0
        q.a..(s)
        w.... q:
            l = l..(q)
            ___ i __ x..(l
                cur = q[i]
                visisted[cur] = T..
                ___ nbr __ V[cur]:
                    __ n.. visisted[nbr]:
                        q.a..(nbr)

            q = q[l:]
            level += 1

        r.. level


c_ SolutionError(o..
    ___ findMinHeightTrees  n, edges
        """
        One pass
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        __ n.. edges:
            r.. 0

        V = {i: [] ___ i __ x..(n)}
        ___ a, b __ edges:
            V[a].a..(b)
            V[b].a..(a)

        leaf = N..
        ___ k, v __ V.i..:
            __ l..(v) __ 1:
                leaf = k
                _____

        # bfs
        visisted = [F.. ___ _ __ x..(n)]
        h2v = d..(l..)
        q    # list
        level = 0
        q.a..(leaf)
        w.... q:
            l = l..(q)
            ___ i __ x..(l
                cur = q[i]
                h2v[level].a..(cur)
                visisted[cur] = T..
                ___ nbr __ V[cur]:
                    __ n.. visisted[nbr]:
                        q.a..(nbr)

            q = q[l:]
            level += 1

        __ level%2 __ 0:
            r.. h2v[level/2-1]+h2v[level/2]
        ____
            r.. h2v[level/2]


__ _______ __ _______
    # print Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
    ... Solution().findMinHeightTrees(7, [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) __ [1, 2]