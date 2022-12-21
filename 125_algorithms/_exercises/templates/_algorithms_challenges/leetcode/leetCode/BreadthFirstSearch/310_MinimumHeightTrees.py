#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    """
    The basic idea is
    "keep deleting leaves layer-by-layer, until reach the root."

    Specifically, first find all the leaves, then remove them.
    After removing, some nodes will become new leaves. So we can
    continue remove them. Eventually, there is only 1 or 2 nodes
    left. If there is only one node left, it is the root. If there
    are 2 nodes, either of them could be a possible root.
    """
    ___ findMinHeightTrees  n, edges
        __ n __ 1:
            r_ [0]

        adj = [[] ___ i __ xrange(n)]
        ___ i, j __ edges:
            adj[i].append(j)
            adj[j].append(i)

        leaves   # list
        ___ i __ xrange(n
            __ l..(adj[i]) __ 1:
                leaves.append(i)

        _____ n > 2:
            n -= l..(leaves)
            new_leaves   # list
            ___ node __ leaves:
                adj_node = adj[node][0]
                adj[adj_node].remove(node)
                __ l..(adj[adj_node]) __ 1:
                    new_leaves.append(adj_node)
            leaves = new_leaves

        r_ leaves

"""
1
[]
2
[0,1]
4
[[1,0],[1,2],[1,3]]
"""
