#!/usr/bin/python3
"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two
independent subsets A and B such that every edge in the graph has one node in A
and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for
which the edge between nodes i and j exists.  Each node is an integer between 0
and graph.length - 1.  There are no self edges or parallel edges: graph[i] does
not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.


Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in
graph[j].
"""
____ c.. _______ d..


c_ Solution:
    ___ isBipartite  graph: L..[L..[i..]]) __ b..
        """
        coloring the graph
        dfs coloring
        """
        G graph
        color d..(i..)
        ___ k __ r..(l..(G:
            __ k n.. __ color:
                color[k] 0
                __ n.. dfs(G, k, color
                    r.. F..
            # if colored, don't vist

        r.. T..

    ___ dfs  G, u, color
        ___ nbr __ G[u]:
            __ nbr __ color:
                __ color[nbr] __ color[u]:
                    r.. F..
            ____
                color[nbr] 1 - color[u]  # can be (0, 1) or (-1, 1)
                __ n.. dfs(G, nbr, color
                    r.. F..

        r.. T..


c_ SolutionError:
    ___ isBipartite  graph: L..[L..[i..]]) __ b..
        G graph
        A, B s..(), s..()
        visited d..(b..)
        ___ k __ r..(l..(G:
            __ n.. visited[k]:
                __ n.. dfs(G, visited, k, A, B, T..
                    r.. F..

        r.. T..

    ___ dfs  G, visited, u, A, B, is_A
        visited[u] T..
        __ is_A:
            A.add(u)
        ____
            B.add(u)

        ___ nbr __ G[u]:
            __ nbr __ A __ is_A ____ B:
                r.. F..
            __ n.. visited[nbr]:
                __ n.. dfs(G, visited, nbr, A, B, F..
                    r.. F..

        r.. T..
