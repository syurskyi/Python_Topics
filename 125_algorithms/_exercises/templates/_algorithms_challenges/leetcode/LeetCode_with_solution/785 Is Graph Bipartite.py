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
____ collections _______ defaultdict


class Solution:
    ___ isBipartite(self, graph: List[List[int]]) -> bool:
        """
        coloring the graph
        dfs coloring
        """
        G = graph
        color = defaultdict(int)
        ___ k __ r..(l..(G)):
            __ k n.. __ color:
                color[k] = 0
                __ n.. self.dfs(G, k, color):
                    r.. False
            # if colored, don't vist

        r.. True

    ___ dfs(self, G, u, color):
        ___ nbr __ G[u]:
            __ nbr __ color:
                __ color[nbr] __ color[u]:
                    r.. False
            ____:
                color[nbr] = 1 - color[u]  # can be (0, 1) or (-1, 1)
                __ n.. self.dfs(G, nbr, color):
                    r.. False

        r.. True


class SolutionError:
    ___ isBipartite(self, graph: List[List[int]]) -> bool:
        G = graph
        A, B = set(), set()
        visited = defaultdict(bool)
        ___ k __ r..(l..(G)):
            __ n.. visited[k]:
                __ n.. self.dfs(G, visited, k, A, B, True):
                    r.. False

        r.. True

    ___ dfs(self, G, visited, u, A, B, is_A):
        visited[u] = True
        __ is_A:
            A.add(u)
        ____:
            B.add(u)

        ___ nbr __ G[u]:
            __ nbr __ A __ is_A ____ B:
                r.. False
            __ n.. visited[nbr]:
                __ n.. self.dfs(G, visited, nbr, A, B, False):
                    r.. False

        r.. True
