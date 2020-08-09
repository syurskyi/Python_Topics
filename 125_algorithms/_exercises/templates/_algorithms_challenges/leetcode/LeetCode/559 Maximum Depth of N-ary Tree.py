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
class Node:
    ___ __init__(self, val, children
        self.val = val
        self.children = children


class Solution:
    ___ maxDepth(self, root: "Node") -> int:
        __ not root:
            r_ 0

        max_child_depth = max([
            self.maxDepth(child)
            ___ child in root.children
        ] or [0])
        
        r_ max_child_depth + 1
