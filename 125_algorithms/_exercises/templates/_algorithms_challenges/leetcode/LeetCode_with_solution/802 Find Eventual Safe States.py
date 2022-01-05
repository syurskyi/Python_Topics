#!/usr/bin/python3
"""
In a directed graph, we start at some node and every turn, walk along a directed
edge of the graph.  If we reach a node that is terminal (that is, it has no
outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually
walk to a terminal node.  More specifically, there exists a natural number K so
that for any choice of where to walk, we must have stopped at a terminal node in
less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length
of graph.  The graph is given in the following form: graph[i] is a list of
labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Illustration of graph

Note:

graph will have length at most 10000.
The number of edges in the graph will not exceed 32000.
Each graph[i] will be a sorted list of different integers, chosen within the
range [0, graph.length - 1].
"""
____ typing _______ List, Set


c_ Solution:
    ___ eventualSafeNodes  graph: List[List[i..]]) __ List[i..]:
        """
        detect cycle in the node
        prune by nodes with no cycle
        """
        visit: List[i..] = [0 ___ _ __ graph]  # 0 not visted, 1 processing, 2 visited
        acyclic: Set[i..] = set()
        ___ u __ r..(l..(graph)):
            __ visit[u] __ 0:
                dfs(graph, u, visit, acyclic)

        r.. [
            u
            ___ u __ r..(l..(graph))
            __ u __ acyclic
        ]

    ___ dfs  graph, cur, visit, acyclic):
        visit[cur] = 1
        ___ nbr __ graph[cur]:
            __ visit[nbr] __ 2:
                __ nbr __ acyclic:
                    _____
                ____:
                    break
            __ visit[nbr] __ 1:
                break
            __ visit[nbr] __ 0 a.. n.. dfs(graph, nbr, visit, acyclic):
                break
        ____:
            acyclic.add(cur)
            visit[cur] = 2
            r.. T..

        visit[cur] = 2
        r.. F..


__ _______ __ _______
    ... Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]) __ [2,4,5,6]
