#!/usr/bin/python3
"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

For example, given a 3-ary tree:

We should return its max depth, which is 3.

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""


# Definition for a Node.
c_ Node:
    ___ - , val, children):
        val = val
        children = children


c_ Solution:
    ___ maxDepth  root: "Node") __ i..:
        __ n.. root:
            r.. 0

        max_child_depth = m..([
            maxDepth(child)
            ___ child __ root.children
        ] o. [0])
        
        r.. max_child_depth + 1
